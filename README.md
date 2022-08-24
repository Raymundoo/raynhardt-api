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
virtualenv -p python3 raynhardt-api-jwt
```

#### 2.2 Levantamos el entorno

El siguiente path es en donde instale mi entorno en su caso deberan poner el path en donde instalaron su entorno

```
source /var/waps/entornos/raynhardt-api-jwt/bin/activate
```

#### 2.3 Nos posicionamos en la raiz del proyecto clonado anteriormente e instalamos los requerimientos

```
pip install -r requirements.txt
```

## 3. Correr el proyecto

```
python manage.py runserver
```

## 4. Hosteamos el proyecto

```
sudo nano /etc/hosts
```

pegamos lo siguiente

```
127.0.0.1       raynhardtapi.net
```

## 5. Ingresamos al nevegador con ***http://raynhardtapi.net:8000/*** para comprobar que el proyecto este corriendo

## 6. Creamos un usuario el cual nos servira para que el proyecto

## 7. Instalar el proyecto que funcionara como cliente https://github.com/Raymundoo/api-cliente

## EDITADO
