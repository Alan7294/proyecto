import asyncio
import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from config.conexionDB import get_conexion

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
router = APIRouter()

class Alumno(BaseModel):
    id_persona: int
    carrera_alumno: int

@router.get("/infoAlumnos")
async def reporte_alumnos(conn=Depends(get_conexion)):
    consulta = """
        SELECT a.id_alumno,
               p.nombre_persona,
               p.apellido_pat,
               p.apellido_mat,
               p.ci,
               p.correo,
               p.fecha_nacimiento,
               c.nombre_carrera

        FROM alumno a
        INNER JOIN persona p ON a.id_persona = p.id_persona
        INNER JOIN carrera c ON a.carrera_alumno = c.id_carrera
        ORDER BY a.id_alumno
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            reporte = await cursor.fetchall()
            if not reporte:
                return {"mensaje": "No hay alumnos registrados en el reporte"}
            return reporte
    except Exception as e:
        print(f"Error al generar reporte de alumnos: {e}")
        raise HTTPException(status_code=400, detail="Error al generar reporte de alumnos")

@router.get("/infoAlumnos/{id_alumno}")
async def reporte_alumno_por_id(id_alumno: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT a.id_alumno,
               p.nombre_persona,
               p.apellido_pat,
               p.apellido_mat,
               p.ci,
               p.correo,
               p.fecha_nacimiento,
               c.nombre_carrera
        FROM alumno a
        INNER JOIN persona p ON a.id_persona = p.id_persona
        INNER JOIN carrera c ON a.carrera_alumno = c.id_carrera
        WHERE a.id_alumno = %s
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_alumno,))
            alumno = await cursor.fetchone()
            if not alumno:
                raise HTTPException(status_code=404, detail="Alumno no encontrado")
            return alumno
    except Exception as e:
        print(f"Error al consultar alumno por id: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar alumno")
  
@router.get("/")
async def listar_alumnos(conn=Depends(get_conexion)):
    consulta = """
        SELECT id_alumno, id_persona, carrera_alumno
        FROM alumno
        ORDER BY id_alumno
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            alumnos = await cursor.fetchall()
            if not alumnos:
                return {"mensaje": "No hay alumnos registrados"}
            return alumnos
    except Exception as e:
        print(f"Error al listar alumnos: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar alumnos")

@router.get("/{id_alumno}")
async def obtener_alumno(id_alumno: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT id_alumno, id_persona, carrera_alumno
        FROM alumno
        WHERE id_alumno = %s
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_alumno,))
            alumno = await cursor.fetchone()
            if not alumno:
                raise HTTPException(status_code=404, detail="Alumno no encontrado")
            return alumno
    except Exception as e:
        print(f"Error al consultar alumno: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar alumno")

@router.post("/")
async def insertar_alumno(alumno: Alumno, conn=Depends(get_conexion)):
    consulta = """
        INSERT INTO alumno(id_persona, carrera_alumno)
        VALUES (%s, %s)
        RETURNING id_alumno
    """
    parametros = (alumno.id_persona, alumno.carrera_alumno)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            nuevo_id = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Alumno registrado exitosamente", "id_alumno": nuevo_id["id_alumno"]}
    except Exception as e:
        print(f"Error al insertar alumno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo registrar el alumno")

@router.put("/{id_alumno}")
async def actualizar_alumno(id_alumno: int, alumno: Alumno, conn=Depends(get_conexion)):
    consulta = """
        UPDATE alumno
        SET id_persona = %s,
            carrera_alumno = %s
        WHERE id_alumno = %s
        RETURNING id_alumno
    """
    parametros = (alumno.id_persona, alumno.carrera_alumno, id_alumno)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Alumno no encontrado")
            actualizado = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Alumno actualizado correctamente", "id_alumno": actualizado["id_alumno"]}
    except Exception as e:
        print(f"Error al actualizar alumno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo actualizar el alumno")

@router.delete("/{id_alumno}")
async def eliminar_alumno(id_alumno: int, conn=Depends(get_conexion)):
    consulta = "DELETE FROM alumno WHERE id_alumno = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_alumno,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Alumno no encontrado")
            await conn.commit()
            return {"mensaje": "Alumno eliminado correctamente"}
    except Exception as e:
        print(f"Error al eliminar alumno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo eliminar el alumno")

app.include_router(router)
