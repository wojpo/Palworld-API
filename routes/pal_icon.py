from starlette.responses import FileResponse


async def get_pal_icon(Pal :str):

    image_path = f"static/{Pal}_menu.webp"
    return FileResponse(image_path, media_type="image/webp")