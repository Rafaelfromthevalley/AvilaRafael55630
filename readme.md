# Proyecto Petter - Guía Rápida

Este proyecto Petter es una aplicación web para gestionar cuidadores de mascotas, dueños de mascotas y sus mascotas. Aquí se presenta una guía rápida para ayudarte a navegar por el proyecto y comprender dónde encontrar las diferentes funcionalidades.

## Orden de Prueba de Funcionalidades

1. **Agregar Cuidador**: Para agregar un nuevo cuidador de mascotas, ve a la url agregar_cuidador/. Llena el formulario con la información requerida y haz clic en "Guardar". El cuidador se guardará en la base de datos y se redirigirá a la página de inicio.

2. **Agregar Dueño**: Para agregar un nuevo dueño de mascotas, ve a la url agregar_dueno/. Llena el formulario y haz clic en "Guardar". El dueño se guardará y se redirigirá a la página de inicio.

3. **Agregar Mascota**: Para agregar una mascota, ve a la url agregar_mascota/.Completa el formulario con la información requerida y haz clic en "Guardar". La mascota se registrará y se redirigirá a la página de inicio.

4. **Buscar Cuidador por Nombre**: Para buscar un cuidador por nombre, ve a la url buscar_cuidador/. Ingresa el nombre del cuidador en el formulario y haz clic en "Buscar". Se mostrará una lista de cuidadores que coinciden con el nombre.

5. **Reiniciar Búsqueda**: En la página de búsqueda de cuidadores, puedes hacer clic en "Reiniciar Búsqueda" para eliminar los resultados de la búsqueda actual y comenzar de nuevo.

6. **Ver Información de Cuidadores**: Los resultados de la búsqueda mostrarán la información detallada de los cuidadores encontrados, incluyendo nombre, correo electrónico, teléfono, biografía y si tienen entrenamiento en el cuidado de perros.

## Notas Adicionales

- La aplicación utiliza formularios para recopilar y validar la información antes de guardarla en la base de datos.
- Los modelos definidos representan las tablas de la base de datos y están relacionados entre sí.
- Las rutas URL se definen y están vinculadas a las vistas correspondientes.