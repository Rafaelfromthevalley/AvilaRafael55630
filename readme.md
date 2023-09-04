# Proyecto Petter - Guía Rápida

## Objetivo Funcional

El proyecto Petter es una aplicación web que tiene como objetivo principal facilitar la gestión de cuidadores de mascotas, dueños de mascotas y sus mascotas. El objetivo funcional principal de la aplicación es permitir a los dueños de mascotas encontrar y contactar a cuidadores de mascotas (pet sitters) de manera sencilla y eficiente. Esto les brinda la oportunidad de contratar a personas calificadas y confiables para el cuidado de sus animales de compañía.

## Orden de Prueba de Funcionalidades

A continuación, se presenta un resumen de las principales funcionalidades de la aplicación:

### Modelos

#### Modelo `CuidadorMascotas`
- **nombre:** Campo de texto para almacenar el nombre del cuidador.
- **correo_electronico:** Campo de correo electrónico para registrar la dirección de correo electrónico del cuidador.
- **telefono:** Campo de texto para almacenar el número de teléfono del cuidador.
- **biografia:** Campo de texto largo para describir la biografía o información relevante sobre el cuidador.
- **entrenamiento_cuidado_perros:** Campo booleano que indica si el cuidador tiene entrenamiento específico para el cuidado de perros.

#### Modelo `DuenoMascota`
- **nombre:** Campo de texto para almacenar el nombre del dueño de la mascota.
- **correo_electronico:** Campo de correo electrónico para registrar la dirección de correo electrónico del dueño de la mascota.
- **telefono:** Campo de texto para almacenar el número de teléfono del dueño de la mascota.
- **direccion:** Campo de texto para almacenar la dirección del dueño de la mascota.

#### Modelo `Mascota`
- **nombre:** Campo de texto para almacenar el nombre de la mascota.
- **dueno:** Relación ForeignKey que conecta cada mascota con su dueño correspondiente utilizando el modelo `DuenoMascota`.
- **tipo:** Campo de selección (choice) para especificar el tipo de mascota (p. ej., "canino" o "felino").
- **raza:** Campo de texto para almacenar la raza de la mascota.
- **edad:** Campo entero positivo para almacenar la edad de la mascota.

### Vistas y Controladores

- **CRUD para Cuidadores de Mascotas:** Permite la gestión completa de cuidadores de mascotas, incluyendo agregar, ver, editar y eliminar registros.
- **CRUD para Dueños de Mascotas:** Permite la gestión completa de dueños de mascotas, incluyendo agregar, ver, editar y eliminar registros.
- **CRUD para Mascotas:** Permite la gestión completa de mascotas, incluyendo agregar, ver, editar y eliminar registros.
- **Registro de Usuarios:** Los usuarios pueden registrarse en la plataforma proporcionando información básica.
- **Inicio de Sesión:** Los usuarios registrados pueden iniciar sesión en sus cuentas.
- **Edición de Perfil de Usuario:** Los usuarios pueden editar su información de perfil, incluyendo nombre, apellido, correo electrónico y contraseña.
- **Búsqueda de Cuidadores de Mascotas:** Los usuarios pueden buscar cuidadores de mascotas por nombre.

## Notas Adicionales

- La aplicación utiliza formularios para recopilar y validar la información antes de guardarla en la base de datos.
- Los modelos definidos representan las tablas de la base de datos y están relacionados entre sí.
- Las rutas URL se definen y están vinculadas a las vistas correspondientes.

## IMPORTANTE USUARIO
-  usuario super admin: username: ravila | password: ravila159852

¡Bienvenido a Petter, la plataforma que conecta a los amantes de las mascotas con los mejores cuidadores!