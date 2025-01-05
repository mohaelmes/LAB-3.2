<<<<<<< HEAD
# LAB-2.7

## 1. Instalar un linter 
En el entorno virtual, instalamos los linters:
![image](https://github.com/user-attachments/assets/9ae292f8-1206-4b68-b7d5-c0b30fe26133)

## 2. Ejecutar el linter

![image](https://github.com/user-attachments/assets/debc99de-79e9-4ef7-827f-04309a2627b6)


## 3. Instalar y Aplicar Coverage

![image](https://github.com/user-attachments/assets/ef8f587a-2ad5-4bb6-9dfd-4608117a8830)

Lo ejecutamos:
```
coverage run -m pytest
coverage report
coverage html  # Para generar un reporte en formato HTML
```
![image](https://github.com/user-attachments/assets/fa4a3b8b-74ab-44d1-9314-7779bb448e77)

![image](https://github.com/user-attachments/assets/21196234-751c-416d-bfe9-1f9d5c31e292)

![image](https://github.com/user-attachments/assets/99d1983a-e81a-4b60-86a1-b9c05c71cb45)

![image](https://github.com/user-attachments/assets/c3f42efc-8776-458c-9d51-5ee426109536)

![image](https://github.com/user-attachments/assets/41aaa00d-8172-4bcb-ba23-4d0ac55ec860)

Esto crea una carpeta htmlcov con un informe navegable en el archivo index.html.
=======
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

Seguimos los pasos de instalación de sops y gpg:

![image](https://github.com/user-attachments/assets/9a4809a3-9ee5-4e19-9549-80fb421552c8)

Copiamos la clave a nuestro directorio actual:
![image](https://github.com/user-attachments/assets/38ed39b3-50ba-4287-a4c5-6633e86e6a91)

![image](https://github.com/user-attachments/assets/0b51db0b-c09a-45a6-ade7-2b1a4dc2226b)

Verificamos con ls -l si el archivo cifrado:
![image](https://github.com/user-attachments/assets/dbe4590a-e869-492a-a434-eeaf8b856a80)


Con nano podemos ver el archivo:
![image](https://github.com/user-attachments/assets/0411de28-3342-4313-9a85-380f87413b9e)


>>>>>>> 6901a9fd5667f6844e29b2e7fcedbbde9cafd16e


