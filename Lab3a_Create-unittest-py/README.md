# Laboratorio 3a: Crear una prueba unitaria de Python

- [Laboratorio 3a: Crear una prueba unitaria de Python](#laboratorio-3a-crear-una-prueba-unitaria-de-python)
  - [Parte 3. Prueba una función de Python con unittest](#parte-3-prueba-una-función-de-python-con-unittest)
    - [Paso 1. Revisa el archivo test\_data.py](#paso-1-revisa-el-archivo-test_datapy)
    - [Paso 2. Crea la función json\_search() que vas a probar](#paso-2-crea-la-función-json_search-que-vas-a-probar)
    - [Paso 3. Crea algunas pruebas unitarias que comprueben si la función funciona según lo previsto](#paso-3-crea-algunas-pruebas-unitarias-que-comprueben-si-la-función-funciona-según-lo-previsto)
    - [Paso 4. Ejecuta la prueba para ver los resultados iniciales](#paso-4-ejecuta-la-prueba-para-ver-los-resultados-iniciales)
    - [Paso 5. Investiga y corrige el primer error en el script recursive\_json\_search.py](#paso-5-investiga-y-corrige-el-primer-error-en-el-script-recursive_json_searchpy)
    - [Paso 6. Vuelve a ejecutar la prueba para comprobar si se han corregido todos los errores del script](#paso-6-vuelve-a-ejecutar-la-prueba-para-comprobar-si-se-han-corregido-todos-los-errores-del-script)
    - [Paso 7. Investiga y corrige el segundo error en el script recursive\_json\_search.py](#paso-7-investiga-y-corrige-el-segundo-error-en-el-script-recursive_json_searchpy)
  - [Conclusiones](#conclusiones)

> Para este laboratorio seguimos [esta guía en inglés.](https://www.ccna6rs.com/3-5-7-lab-create-a-python-unit-test-answers/)

## Parte 3. Prueba una función de Python con unittest

### Paso 1. Revisa el archivo test_data.py

![](sources/2023-04-11-15-43-09.png)

### Paso 2. Crea la función json_search() que vas a probar

Creamos la función recursiva `json_search()`, con la que queremos capturar todos los pares clave-valor que coinciden con una clave dada y que están dentro de un diccionario dado. La estructura anidada del diccionario es lo que motiva que la función sea recursiva: queremos buscar los pares clave-valor en cualquier nivel dentro del diccionario.

![](sources/2023-04-12-23-59-12.png)

### Paso 3. Crea algunas pruebas unitarias que comprueben si la función funciona según lo previsto

Tenemos que asegurarnos de tres cosas: que la función retorne una lista no vacía cuando la clave dada existe en el diccionario, que la función retorne una lista vacía cuando no, y que lo que retorna la función siempre sea una lista.

![](sources/2023-04-13-08-42-10.png)

### Paso 4. Ejecuta la prueba para ver los resultados iniciales

Cuando ejecutamos la prueba, vemos que falla la que espera una lista no vacía dada una clave que existe en el diccionario. 

![](sources/2023-04-13-09-01-45.png)

Pero observamos que el superresumen de las pruebas que aparece al principio (.F.) no coincide con el orden de las pruebas definidas en el archivo _test_json_search.py_, ya que la que falla es la primera de ellas. Entonces, ahora sabemos que las pruebas no necesariamente se ejecutan en el orden en que han sido definidas.

![](sources/2023-04-13-09-02-57.png)

### Paso 5. Investiga y corrige el primer error en el script recursive_json_search.py

La variable `ret_val`, al estar dentro de la función recursiva, se vacía en las llamadas recursivas en la línea `ret_val = []`. La primera solución que se nos puede ocurrir es volverla una variable global. Esto resulve el primer error, como se puede apreciar al ejecutarla con este cambio:

![](sources/2023-04-13-09-21-41.png)

### Paso 6. Vuelve a ejecutar la prueba para comprobar si se han corregido todos los errores del script

Sin embargo, al volver global la variable `ret_val` se introduce otro problema: esta variable se queda con la información que capturó en otras pruebas. Si primero se ejecuta la prueba en la que devuelve una lista no vacía, con información, luego la prueba en la que debe devolver una lista vacía fallará porque la variable que se retorna contiene la información que capturó en la anterior prueba.

![](sources/2023-04-13-09-24-02.png)

### Paso 7. Investiga y corrige el segundo error en el script recursive_json_search.py

Tanto el primer error como el que introdujimos luego se pueden resolver cambiando la definición de la función de forma que la variable `ret_val` vuelva a ser local, pero no se vacíe en las llamadas recursivas. Para ello definimos una función con el mismo nombre que servirá para **envolver** la variable local y una función interna `inner_function()` que contendrá toda la lógica recursiva. No se nos debe olvidar que debemos llamar esta función interna dentro del la función envoltorio.

![](sources/2023-04-13-10-20-16.png)

A propósito, hice el intento de renombrar la `función json_search()` como `inner_function()` para ahorrarme tener que reescribir manualmente las llamadas recursivas, pero se renombró también en el archivo de las pruebas unitarias. Es un comportamiento de VSCode que desconocía y que, obviamente, no era deseado en este caso.

![](sources/2023-04-13-09-37-05.png)

## Conclusiones


