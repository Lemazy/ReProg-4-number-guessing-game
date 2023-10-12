{
    "name": "Python Dev Container",
    "image": "python:3.10",
    "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "visualstudioexptteam.vscodeintellicode",
    ],
    "settings": {
        "python.pythonPath": "/usr/local/bin/python",
        "python.linting.pylintEnabled": True,
        "python.linting.enabled": True,
    },
    "forwardPorts": [5000],
}
