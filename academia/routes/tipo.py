import asyncio
import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from config.conexionDB import get_conexion

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
router = APIRouter()

class TipoUsuario(BaseModel):
    nombre_tipo: str

@router.get("/")
async def listar_tipos(conn=Depends(get_conexion)):
    consulta = "SELECT id_tipo, nombre_tipo FROM tipo_usuario ORDER BY id_tipo"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta)
            tipos = await cursor.fetchall()
            if not tipos:
                return {"mensaje": "No hay tipos de usuario registrados"}
            return tipos
    except Exception as e:
        print(f"Error al listar tipos de usuario: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar tipos de usuario")

@router.get("/{id_tipo}")
async def obtener_tipo(id_tipo: int, conn=Depends(get_conexion)):
    consulta = "SELECT id_tipo, nombre_tipo FROM tipo_usuario WHERE id_tipo = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_tipo,))
            tipo = await cursor.fetchone()
            if not tipo:
                raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
            return tipo
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error al consultar tipo de usuario: {e}")
        raise HTTPException(status_code=400, detail="Error al consultar tipo de usuario")

@router.post("/")
async def insertar_tipo(tipo: TipoUsuario, conn=Depends(get_conexion)):
    consulta = "INSERT INTO tipo_usuario(nombre_tipo) VALUES (%s) RETURNING id_tipo"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (tipo.nombre_tipo,))
            nuevo_id = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Tipo de usuario registrado exitosamente", "id_tipo": nuevo_id["id_tipo"]}
    except Exception as e:
        print(f"Error al insertar tipo de usuario: {e}")
        raise HTTPException(status_code=400, detail="No se pudo registrar el tipo de usuario")

@router.put("/{id_tipo}")
async def actualizar_tipo(id_tipo: int, tipo: TipoUsuario, conn=Depends(get_conexion)):
    consulta = "UPDATE tipo_usuario SET nombre_tipo = %s WHERE id_tipo = %s RETURNING id_tipo"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (tipo.nombre_tipo, id_tipo))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
            actualizado = await cursor.fetchone()
            await conn.commit()
            return {"mensaje": "Tipo de usuario actualizado correctamente", "id_tipo": actualizado["id_tipo"]}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error al actualizar tipo de usuario: {e}")
        raise HTTPException(status_code=400, detail="No se pudo actualizar el tipo de usuario")

@router.delete("/{id_tipo}")
async def eliminar_tipo(id_tipo: int, conn=Depends(get_conexion)):
    consulta = "DELETE FROM tipo_usuario WHERE id_tipo = %s"
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(consulta, (id_tipo,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
            await conn.commit()
            return {"mensaje": "Tipo de usuario eliminado correctamente"}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error al eliminar tipo de usuario: {e}")
        raise HTTPException(status_code=400, detail="No se pudo eliminar el tipo de usuario")

app.include_router(router, prefix="/tipos_usuario", tags=["Tipos de Usuario"])
