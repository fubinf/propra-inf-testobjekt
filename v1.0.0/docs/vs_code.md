# VS Code

Hier werden Konfigurationen in VS Code Dokumentiert

## launch

Mit Hilfe eines Launch-Setup kann die Anwendung in VS Code automatisiert gestartet werden.
TODO_Ruhe: Schritte erläutern

 ```JSON
 {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Testobjekt 1.0.0",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "v1.0.0/app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
}
 ```
