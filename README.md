# Instalación del proyecto

Se requiere tener python3 y virutalenv instalado para poder crear el entorno del proyecto

## 1. Clonar el repositorio
Posicionarnos en donde clonaremos el entorno
```
git clone https://github.com/Raymundoo/raynhardt-api.git
```

## 2. Instalar el entorno
#### 2.1 Usaremos virtualenv para crear el entorno
```
virtualenv -p python3 raynhardt-api
```
#### 2.2 Levantamos el entorno
El siguiente path es en donde instale mi entorno en su caso deberan poner el path en donde instalaron su entorno
```
source /var/waps/entornos/raynhard/bin/activate
```

#### 2.3 Nos posicionamos en la raiz del proyecto clonado anteriormente e instalamos los requerimientos
```
pip install -r requirements.txt
```

### 3. Correr el proyecto
```
python manage.py runserver
```

### 4. Ingresamos al nevegador la ip ***http://127.0.0.1:8000/*** para comprobar que el proyecto este corriendo
