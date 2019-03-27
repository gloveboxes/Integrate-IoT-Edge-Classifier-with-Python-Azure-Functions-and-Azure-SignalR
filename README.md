# Create Python Virtual Environment

In Bash

```bash
python3.6 -m venv .env
source .env/bin/activate
```

In PowerShell
```powershell
py -3.6 -m venv .env
.env\scripts\activate
```

## Opening Python Project

Be sure that the virtual Python environment you created is active and select in Visual Studio Code

## Deploy Function

func azure functionapp publish enviromon-python --build-native-deps