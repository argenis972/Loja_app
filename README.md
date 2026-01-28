Proyecto unificado: instrucciones rápidas

1) Crear e activatar el virtualenv e instalar dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Ejecutar la API (desde la raíz):

```powershell
uvicorn backend.api.main:app --reload
```

3) Ejecutar tests (desde la raíz):

```powershell
pytest
```

Configura `.env` copiando `.env.example` y ajustando credenciales.
