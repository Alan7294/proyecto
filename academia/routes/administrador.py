import asyncio
import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from config.conexionDB import get_conexion

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
router = APIRouter()

class Administrador(BaseModel):
    id_persona: int

@router.get("/infoAdministradores")
async def reporte_administradores(conn=Depends(get_conexion)):
    consulta = """
        SELECT a.id_admin,
               p.id_persona,
               p.nombre,
               p.apellido_pat,
               p.apellido_mat,
               p.ci,
               p.correo,
               p.fecha_nacimiento
        FROM administrador a
        INNER JOIN persona p ON a.id_persona = p.id_persona
        ORDER BY a.id_admin
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            reporte = await cursor.fetchall()
            if not reporte:
                return {"mensaje": "No hay administradores registrados en el reporte"}
            return reporte
    except Exception as e:
        print(f"Error al generar reporte de administradores: {e}")
        raise HTTPException(status_code=400, detail="Error al generar reporte de administradores")

@router.get("/")
async def listar_administradores(conn=Depends(get_conexion)):
    consulta = """
        SELECT id_admin, id_persona
        FROM administrador
        ORDER BY id_admin
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            administradores = await cursor.fetchall()
            if not administradores:
                return {"mensaje": "No hay administradores registrados"}
            return administradores
    except Exception as e:
        print(f"Error al listar administradores: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar administradores")

@router.get("/{id_admin}")
async def obtener_administrador(id_admin: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT id_admin, id_persona
        FROM administrador
        WHERE id_admin = %s
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_admin,))
            administrador = await cursor.fetchone()
            if not administrador:
                raise HTTPException(status_code=404, detail="Administrador no encontrado")
            return administrador
    except Exception as e:
        print(f"Error al consultar administrador: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar administrador")

@router.post("/")
async def insertar_administrador(administrador: Administrador, conn=Depends(get_conexion)):
    consulta = """
        INSERT INTO administrador(id_persona)
        VALUES (%s)
        RETURNING id_admin
    """
    parametros = (administrador.id_persona,)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            nuevo_id = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Administrador registrado exitosamente", "id_admin": nuevo_id["id_admin"]}
    except Exception as e:
        print(f"Error al insertar administrador: {e}")
        raise HTTPException(status_code=400, detail="No se pudo registrar el administrador")

@router.put("/{id_admin}")
async def actualizar_administrador(id_admin: int, administrador: Administrador, conn=Depends(get_conexion)):
    consulta = """
        UPDATE administrador
        SET id_persona = %s
        WHERE id_admin = %s
        RETURNING id_admin
    """
    parametros = (administrador.id_persona, id_admin)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Administrador no encontrado")
            actualizado = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Administrador actualizado correctamente", "id_admin": actualizado["id_admin"]}
    except Exception as e:
        print(f"Error al actualizar administrador: {e}")
        raise HTTPException(status_code=400, detail="No se pudo actualizar el administrador")

@router.delete("/{id_admin}")
async def eliminar_administrador(id_admin: int, conn=Depends(get_conexion)):
    consulta = "DELETE FROM administrador WHERE id_admin = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_admin,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Administrador no encontrado")
            await conn.commit()
            return {"mensaje": "Administrador eliminado correctamente"}
    except Exception as e:
        print(f"Error al eliminar administrador: {e}")
        raise HTTPException(status_code=400, detail="No se pudo eliminar el administrador")

app.include_router(router)
