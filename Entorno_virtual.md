## Configuración del Entorno Virtual

1. Verifica la versión de Python actualmente instalada con el siguiente comando:
   ```zsh
   python --version
   ```

2. Comprueba la versión de pip instalada con:
   ```zsh
   pip --version
   ```

3. Si estás utilizando Python 3.12.1, procede a instalar `virtualenv` con:
   ```zsh
   pip install virtualenv
   ```

4. Crea un entorno virtual ejecutando:
   ```zsh
   virtualenv env
   ```

5. Activa el entorno virtual con el comando:
   ```zsh
   .\env\Scripts\activate
   ```

6. Verifica que Python y pip estén correctamente instalados en el entorno virtual:
   ```zsh
   python --version
   pip --version
   ```

7. Para revisar los paquetes instalados en el entorno virtual, utiliza:
   ```zsh
   pip freeze
   ```

8. Guarda los paquetes instalados en un archivo de requisitos con:
   ```zsh
   pip freeze > requirements.txt
   ```

9. Para salir del entorno virtual, ejecuta:
   ```zsh
   .\env\Scripts\deactivate
   ```

10. Finalmente, para instalar las dependencias del proyecto, utiliza:
    ```zsh
    pip install -r requirements.txt
    ```
