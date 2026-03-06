import asyncio
import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from config.conexionDB import get_conexion

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
router = APIRouter()

class Docente(BaseModel):
    id_persona: int
    id_especialidad: int

@router.get("/infoDocentes")
async def reporte_docentes(conn=Depends(get_conexion)):
    consulta = """
        SELECT d.id_docente,
               p.id_persona,
               p.nombre,
               p.apellido_pat,
               p.apellido_mat,
               p.ci,
               p.correo,
               p.fecha_nacimiento,
               d.id_especialidad,
               e.nombre_especialidad

        FROM docente d
        INNER JOIN persona p ON d.id_persona = p.id_persona
        INNER JOIN especialidad e ON d.id_especialidad = e.id_especialidad
        ORDER BY d.id_docente
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            reporte = await cursor.fetchall()
            if not reporte:
                return {"mensaje": "No hay docentes registrados en el reporte"}
            return reporte
    except Exception as e:
        print(f"Error al generar reporte de docentes: {e}")
        raise HTTPException(status_code=400, detail="Error al generar reporte de docentes")

@router.get("/infoDocentes/{id_docente}")
async def reporte_docentes(id_docente: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT d.id_docente,
               p.id_persona,
               p.nombre,
               p.apellido_pat,
               p.apellido_mat,
               p.ci,
               p.correo,
               p.fecha_nacimiento,
               d.id_especialidad,
               e.nombre_especialidad

        FROM docente d
        INNER JOIN persona p ON d.id_persona = p.id_persona
        INNER JOIN especialidad e ON d.id_especialidad = e.id_especialidad
        ORDER BY d.id_docente
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            reporte = await cursor.fetchall()
            if not reporte:
                return {"mensaje": "No hay docentes registrados en el reporte"}
            return reporte
    except Exception as e:
        print(f"Error al generar reporte de docentes: {e}")
        raise HTTPException(status_code=400, detail="Error al generar reporte de docentes")
    
@router.get("/")
async def listar_docentes(conn=Depends(get_conexion)):
    consulta = """
        SELECT id_docente, id_persona, id_especialidad
        FROM docente
        ORDER BY id_docente
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            docentes = await cursor.fetchall()
            if not docentes:
                return {"mensaje": "No hay docentes registrados"}
            return docentes
    except Exception as e:
        print(f"Error al listar docentes: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar docentes")

@router.get("/{id_docente}")
async def obtener_docente(id_docente: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT id_docente, id_persona, id_especialidad
        FROM docente
        WHERE id_docente = %s
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_docente,))
            docente = await cursor.fetchone()
            if not docente:
                raise HTTPException(status_code=404, detail="Docente no encontrado")
            return docente
    except Exception as e:
        print(f"Error al consultar docente: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar docente")

@router.post("/")
async def insertar_docente(docente: Docente, conn=Depends(get_conexion)):
    consulta = """
        INSERT INTO docente(id_persona, id_especialidad)
        VALUES (%s, %s)
        RETURNING id_docente
    """
    parametros = (docente.id_persona, docente.id_especialidad)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            nuevo_id = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Docente registrado exitosamente", "id_docente": nuevo_id["id_docente"]}
    except Exception as e:
        print(f"Error al insertar docente: {e}")
        raise HTTPException(status_code=400, detail="No se pudo registrar el docente")

@router.put("/{id_docente}")
async def actualizar_docente(id_docente: int, docente: Docente, conn=Depends(get_conexion)):
    consulta = """
        UPDATE docente
        SET id_persona = %s,
            id_especialidad = %s
        WHERE id_docente = %s
        RETURNING id_docente
    """
    parametros = (docente.id_persona, docente.id_especialidad, id_docente)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Docente no encontrado")
            actualizado = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Docente actualizado correctamente", "id_docente": actualizado["id_docente"]}
    except Exception as e:
        print(f"Error al actualizar docente: {e}")
        raise HTTPException(status_code=400, detail="No se pudo actualizar el docente")

@router.delete("/{id_docente}")
async def eliminar_docente(id_docente: int, conn=Depends(get_conexion)):
    consulta = "DELETE FROM docente WHERE id_docente = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_docente,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Docente no encontrado")
            await conn.commit()
            return {"mensaje": "Docente eliminado correctamente"}
    except Exception as e:
        print(f"Error al eliminar docente: {e}")
        raise HTTPException(status_code=400, detail="No se pudo eliminar el docente")

app.include_router(router)
