# Laboratorio 12. Uso de Restconf para acceder a un dispositivos IOS XE <!-- omit in toc -->

- [Parte 1. Construye la red y verifica la conectividad](#parte-1-construye-la-red-y-verifica-la-conectividad)
  - [Paso 1. Inicia las máquinas virtuales.](#paso-1-inicia-las-máquinas-virtuales)
  - [Paso 2. Verifica la conectividad entre las máquinas virtuales](#paso-2-verifica-la-conectividad-entre-las-máquinas-virtuales)
  - [Paso 3. Verifica la conectividad SSH a la máquina virtual CSR1kv](#paso-3-verifica-la-conectividad-ssh-a-la-máquina-virtual-csr1kv)
- [Parte 2. Configura un dispositivo IOS XE para el acceso RESTCONF](#parte-2-configura-un-dispositivo-ios-xe-para-el-acceso-restconf)
  - [Paso 1. Verifica que los demonios RESTCONF estén en ejecución.](#paso-1-verifica-que-los-demonios-restconf-estén-en-ejecución)
  - [Paso 2. Habilita y verifica el servicio RESTCONF](#paso-2-habilita-y-verifica-el-servicio-restconf)
  - [Paso 3. Habilita y verifica el servicio HTTPS](#paso-3-habilita-y-verifica-el-servicio-https)
- [Parte 3. Abre y configura Postman](#parte-3-abre-y-configura-postman)
  - [Paso 1. Abre Postman](#paso-1-abre-postman)
  - [Paso 2. Deshabilita la verificación de certificación SSL](#paso-2-deshabilita-la-verificación-de-certificación-ssl)
- [Parte 4. Utiliza Postman para enviar solicitudes GET](#parte-4-utiliza-postman-para-enviar-solicitudes-get)
  - [Paso 1. Explora la interfaz de usuario de Postman](#paso-1-explora-la-interfaz-de-usuario-de-postman)
  - [Paso 2. Ingresa la URL para un CSR1kv.](#paso-2-ingresa-la-url-para-un-csr1kv)
  - [Paso 3. Ingresa las credenciales de autenticación.](#paso-3-ingresa-las-credenciales-de-autenticación)
  - [Paso 4. Establece JSON como el tipo de datos para enviar y recibir desde el CSR1kv](#paso-4-establece-json-como-el-tipo-de-datos-para-enviar-y-recibir-desde-el-csr1kv)
  - [Paso 5. Envía la solicitud API al CSR1kv.](#paso-5-envía-la-solicitud-api-al-csr1kv)
  - [Paso 6. Utiliza una solicitud GET para recopilar información sobre todas las interfaces en el CSR1kv](#paso-6-utiliza-una-solicitud-get-para-recopilar-información-sobre-todas-las-interfaces-en-el-csr1kv)
  - [Paso 7. Utiliza una solicitud GET para recopilar información sobre una interfaz específica en el CSR1kv](#paso-7-utiliza-una-solicitud-get-para-recopilar-información-sobre-una-interfaz-específica-en-el-csr1kv)
- [Parte 5. Usa Postman para enviar una solicitud PUT](#parte-5-usa-postman-para-enviar-una-solicitud-put)
  - [Paso 1. Duplica y modifica la última solicitud GET](#paso-1-duplica-y-modifica-la-última-solicitud-get)
  - [Paso 2. Configura el cuerpo de la solicitud especificando la información para el nuevo loopback](#paso-2-configura-el-cuerpo-de-la-solicitud-especificando-la-información-para-el-nuevo-loopback)
- [Parte 6. Utiliza un script Python para enviar solicitudes GET](#parte-6-utiliza-un-script-python-para-enviar-solicitudes-get)
  - [Paso 1. Crea el directorio RESTCONF y comienza el script](#paso-1-crea-el-directorio-restconf-y-comienza-el-script)
  - [Paso 2. Crea las variables que serán los componentes de la solicitud](#paso-2-crea-las-variables-que-serán-los-componentes-de-la-solicitud)
- [Parte 7. Utiliza un script Python para enviar una solicitud PUT](#parte-7-utiliza-un-script-python-para-enviar-una-solicitud-put)
  - [Paso 1. Importa módulos y deshabilita las advertencias de SSL](#paso-1-importa-módulos-y-deshabilita-las-advertencias-de-ssl)
  - [Paso 2. Crea las variables que serán los componentes de la solicitud](#paso-2-crea-las-variables-que-serán-los-componentes-de-la-solicitud-1)
  - [Paso 3. Crea una variable para enviar la solicitud y almacenar la respuesta JSON](#paso-3-crea-una-variable-para-enviar-la-solicitud-y-almacenar-la-respuesta-json)
- [Conclusiones y reflexiones](#conclusiones-y-reflexiones)


> Para este laboratorio usamos [esta guía en inglés.](https://itexam24.com/8-3-7-lab-use-restconf-to-access-an-ios-xe-device-answers/)

---
## Parte 1. Construye la red y verifica la conectividad 

### Paso 1. Inicia las máquinas virtuales. 



### Paso 2. Verifica la conectividad entre las máquinas virtuales



### Paso 3. Verifica la conectividad SSH a la máquina virtual CSR1kv



---
## Parte 2. Configura un dispositivo IOS XE para el acceso RESTCONF 

### Paso 1. Verifica que los demonios RESTCONF estén en ejecución. 



### Paso 2. Habilita y verifica el servicio RESTCONF



### Paso 3. Habilita y verifica el servicio HTTPS



---
## Parte 3. Abre y configura Postman 

### Paso 1. Abre Postman



### Paso 2. Deshabilita la verificación de certificación SSL



---
## Parte 4. Utiliza Postman para enviar solicitudes GET 

### Paso 1. Explora la interfaz de usuario de Postman



### Paso 2. Ingresa la URL para un CSR1kv. 



### Paso 3. Ingresa las credenciales de autenticación. 



### Paso 4. Establece JSON como el tipo de datos para enviar y recibir desde el CSR1kv



### Paso 5. Envía la solicitud API al CSR1kv. 



### Paso 6. Utiliza una solicitud GET para recopilar información sobre todas las interfaces en el CSR1kv



### Paso 7. Utiliza una solicitud GET para recopilar información sobre una interfaz específica en el CSR1kv



---
## Parte 5. Usa Postman para enviar una solicitud PUT 

### Paso 1. Duplica y modifica la última solicitud GET



### Paso 2. Configura el cuerpo de la solicitud especificando la información para el nuevo loopback



---
## Parte 6. Utiliza un script Python para enviar solicitudes GET 

### Paso 1. Crea el directorio RESTCONF y comienza el script



### Paso 2. Crea las variables que serán los componentes de la solicitud

---
## Parte 7. Utiliza un script Python para enviar una solicitud PUT

### Paso 1. Importa módulos y deshabilita las advertencias de SSL



### Paso 2. Crea las variables que serán los componentes de la solicitud



### Paso 3. Crea una variable para enviar la solicitud y almacenar la respuesta JSON



---
## Conclusiones y reflexiones

