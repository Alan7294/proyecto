import asyncio
import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from config.conexionDB import get_conexion

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
router = APIRouter(prefix="/turno", tags=["Turno"])

class Turno(BaseModel):
    nombre_turno: str

@router.get("/")
async def listar_turnos(conn=Depends(get_conexion)):
    consulta = """
        SELECT id_turno, nombre_turno
        FROM turno
        ORDER BY id_turno
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            turnos = await cursor.fetchall()
            if not turnos:
                return {"mensaje": "No hay turnos registrados"}
            return turnos
    except Exception as e:
        print(f"Error al listar turnos: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar turnos")

@router.get("/{id_turno}")
async def obtener_turno(id_turno: int, conn=Depends(get_conexion)):
    consulta = """
        SELECT id_turno, nombre_turno
        FROM turno
        WHERE id_turno = %s
    """
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_turno,))
            turno = await cursor.fetchone()
            if not turno:
                raise HTTPException(status_code=404, detail="Turno no encontrado")
            return turno
    except Exception as e:
        print(f"Error al consultar turno: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar turno")

@router.post("/")
async def insertar_turno(turno: Turno, conn=Depends(get_conexion)):
    consulta = """
        INSERT INTO turno(nombre_turno)
        VALUES (%s)
        RETURNING id_turno
    """
    parametros = (turno.nombre_turno,)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            nuevo_id = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Turno registrado exitosamente", "id_turno": nuevo_id["id_turno"]}
    except Exception as e:
        print(f"Error al insertar turno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo registrar el turno")

@router.put("/{id_turno}")
async def actualizar_turno(id_turno: int, turno: Turno, conn=Depends(get_conexion)):
    consulta = """
        UPDATE turno
        SET nombre_turno = %s
        WHERE id_turno = %s
        RETURNING id_turno
    """
    parametros = (turno.nombre_turno, id_turno)
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, parametros)
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Turno no encontrado")
            actualizado = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Turno actualizado correctamente", "id_turno": actualizado["id_turno"]}
    except Exception as e:
        print(f"Error al actualizar turno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo actualizar el turno")

@router.delete("/{id_turno}")
async def eliminar_turno(id_turno: int, conn=Depends(get_conexion)):
    consulta = "DELETE FROM turno WHERE id_turno = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_turno,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Turno no encontrado")
            await conn.commit()
            return {"mensaje": "Turno eliminado correctamente"}
    except Exception as e:
        print(f"Error al eliminar turno: {e}")
        raise HTTPException(status_code=400, detail="No se pudo eliminar el turno")

app.include_router(router)
