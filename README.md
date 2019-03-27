# Create Python Virtual Environment

## Creating your first Python Azure Function

To understand how to create your first Python Azure function then read the "[Create your first Python function in Azure ](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python)" article.

## Solution overview

![solution overview](./docs/resources/python-azure-functions-solution.png)

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