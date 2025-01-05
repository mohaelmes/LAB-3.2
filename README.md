# LAB-2.8

## 1.  Crear un fichero .env con la configuración y variables de entorno

En la raíz del proyecto, creamos un archivo .env que contendrá las variables de entorno.

![image](https://github.com/user-attachments/assets/93554d10-3dd0-4c87-8f21-9685fbce4546)

Modificamos app.py para cargar las variables desde el archivo .env al inicio del archivo (ver paso 2)  

## 2: Crear el archivo secrets.yaml con un usuario y contraseña falsos

![image](https://github.com/user-attachments/assets/f5e99494-2e8b-48ca-b331-d63b36fc4090)

Para aseguranos de que este archivo no se suba al repositorio, lo añadimos al archivo .gitignore
![image](https://github.com/user-attachments/assets/63217487-b3a8-4e65-86ec-4b4b6f84b27b)


## 3.  Cifrar el archivo secrets.yaml con SOPS y PGP
Instalamos las dependencias necesarias:

![image](https://github.com/user-attachments/assets/13cd24e2-4488-467d-8f43-8e7c6cdceefc)


En mi caso instalé sops con brew:
![image](https://github.com/user-attachments/assets/f19577a9-5c05-41af-af44-8261d488205c)


Para cifrar el archivo secrets.yaml con la clave PGP, utilizamos el siguiente comando:

```
sops -e --pgp /pgp/sops_functional_tests_key.asc secrets.yaml > secrets.enc.yaml
```
