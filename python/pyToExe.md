## Exporting python to .exe, basicamente haciendolo un daemon ## 

1. Si no tenes intalado pyinstaller, instalarlo
>pip install pyinstaller

2. Abrir el cmd e ir a la carpeta de tu archivo .py y poner el comando
>pyinstaller -F -w archivo.py

Anotaciones:
-F: genera un archivo sin dependencias externas.
-w: No muestres una ventada de consola, osea, el programa se ejecuta pero no le aparece nada al usuario.
