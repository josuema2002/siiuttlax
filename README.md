# Se usa [AdminLTE](https://appseed.us/generator/adminlte/) Django

Se usa una plantilla de [AdminLTE](https://appseed.us/product/adminlte/django/) Django

## Requerimientos

  * Tener postgresql instalado
  * Tener Python 3.6 o superior instalado

## ✨ Como obtenerlo ✨

> Descarga el codigo de la rama `titulacion`

```bash
$ # Get the code
$ cd SIIUTTLAX_V2
```

<br />

### Crear base de datos

Abrir la aplicación de pgAdmin4 en Server -> Postgres -> Database -> "Click derecho" -> "Create" -> "Database"

El nombre de la base de datos es "titulacion"

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />


## Como usarlo

### 👉 Crear 2 nuevos usuarios
Uno sera el jefe area y otro el alumno

```
create user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`
```	
### Asignar roles a los usuarios

```	
En pgAdmin4, dirigirse a Server -> Postgres -> Database -> titulacion -> Schema -> public -> Tables -> auth_user -> "Click derecho" -> "View/EditData" -> "All Rows" 

Busque el campo "is_superuser" y a uno dejelo en "True" (jefe de area) y el otro en "False" (alumno)

Ahora dirigirse a Server -> Postgres -> Database -> titulacion -> Schema -> public -> Tables -> home_student -> "Click derecho" -> "View/EditData" -> "All Rows" 

y cree un nuevo alumno, en el campo "id_user_student_id" ponga el id del usuario creado anteriormente que dejo en "False"
```

### Usar en el navegador

```
Si ya ejecuto el comando "py manage.py runserver" en el navegador, entonces podemos usar el app en el navegador, si no, entonces ejecutarlo en el terminal.

En el navegador, dirigirse a `http://localhost:8000/login` para iniciar sesion (inicie como alumno o jefe de area) y vera diferentes vistas.

```

<br />
