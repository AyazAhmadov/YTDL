from cx_Freeze import setup, Executable

files = ['assets/']

target = Executable(
    script='main.py',
    base='Win32GUI',
    icon='assets/icon.ico'
)

setup(
    name='YTDL',
    version='1.0',
    author='Ayaz Ahmadov',
    options={'build_exe': {'include_files': files}},
    executables=[target]
)