
# LAB-3.2

## 1. Crear una rama e integrar Poetry
1. Crear una nueva rama en el  repositorio

```
git checkout -b poetry-integration

```
2. Instalamos Poetry
```
curl -sSL https://install.python-poetry.org | python3 -

```

3. Comprobamos que se ha instalado correctamente (ver siguiente paso)
4. Inicializar un nuevo proyecto con Poetry

```
poetry init

```
   ![image](https://github.com/user-attachments/assets/b5e58cd0-5667-4aa1-9b9f-72e33a93e591)
   
6. Agregar dependencias necesarias con Poetry
  ![image](https://github.com/user-attachments/assets/1ac1428a-8de6-426b-b01d-8a995748088a)

8. Configurar un script básico y  probamos el entorno Poetry
Creamos un main.py:
![image](https://github.com/user-attachments/assets/580311bb-bb52-4156-b13f-0b824cb3ba44)

## Crear una rama e integrar Projen
1. Crear una nueva rama en el repositorio

![image](https://github.com/user-attachments/assets/1a8bc326-c22f-4c49-b1d8-48e37dda8be2)

2. Instalar Projen

```
npm install -g projen

```

![image](https://github.com/user-attachments/assets/9f3badb0-d03a-4ab3-a87b-68c67277a9a3)

3. Inicializar un nuevo proyecto con Projen
![image](https://github.com/user-attachments/assets/055bb6e8-b8e6-4cc5-9950-07d112616e55)

4. Añadimos un main.ts básico en src

![image](https://github.com/user-attachments/assets/785b4121-4248-4fa7-86ae-43d462930dd1)


5. Construir el proyecto y probar

![image](https://github.com/user-attachments/assets/4c4cd302-b56f-4fcf-a219-7fe8dc35f6fe)


![image](https://github.com/user-attachments/assets/53a35fac-4de5-4a9b-b00d-286372ee3e19)

## Generar el archivo comparison.md en la rama main
1. Cambiar a la rama main
   ```
   git checkout main

   ```
![image](https://github.com/user-attachments/assets/e0f9a51f-0907-4d7b-8882-dab3ff1ecc05)

![image](https://github.com/user-attachments/assets/384a789e-6a81-424b-a4b6-c32b532f1d7b)

