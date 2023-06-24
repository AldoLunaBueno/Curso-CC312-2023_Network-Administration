# Laboratorio 11: Uso de NETCONF para acceder a un dispositivo IOS XE <!-- omit in toc -->

- [Parte 1. Inicia las máquinas virtuales y verifica la conectividad](#parte-1-inicia-las-máquinas-virtuales-y-verifica-la-conectividad)
  - [Paso 1. Inicia las máquinas virtuales](#paso-1-inicia-las-máquinas-virtuales)
  - [Paso 2. Verifica la conectividad entre las máquinas virtuales](#paso-2-verifica-la-conectividad-entre-las-máquinas-virtuales)
  - [Paso 3. Verifica la conectividad SSH a la máquina virtual CSR1kv](#paso-3-verifica-la-conectividad-ssh-a-la-máquina-virtual-csr1kv)
- [Parte 2. Usa una sesión NETCONF para recopilar información](#parte-2-usa-una-sesión-netconf-para-recopilar-información)
  - [Paso 1. Verifica si NETCONF se está ejecutando en el CSR1kv](#paso-1-verifica-si-netconf-se-está-ejecutando-en-el-csr1kv)
  - [Paso 2. Accede al proceso NETCONF a través de una terminal SSH](#paso-2-accede-al-proceso-netconf-a-través-de-una-terminal-ssh)
  - [Paso 3. Inicia una sesión NETCONF enviando un mensaje de saludo desde el cliente](#paso-3-inicia-una-sesión-netconf-enviando-un-mensaje-de-saludo-desde-el-cliente)
  - [Paso 4. Envía mensajes RPC a un dispositivo IOS XE](#paso-4-envía-mensajes-rpc-a-un-dispositivo-ios-xe)
  - [Paso 5. Cierra la sesión NETCONF](#paso-5-cierra-la-sesión-netconf)
- [Parte 3. Usa ncclient para conectarte a NETCONF](#parte-3-usa-ncclient-para-conectarte-a-netconf)
  - [Paso 1. Verifica que ncclient esté instalado y listo para usar](#paso-1-verifica-que-ncclient-esté-instalado-y-listo-para-usar)
  - [Paso 2. Crea un script para usar ncclient para conectarte al servicio NETCONF](#paso-2-crea-un-script-para-usar-ncclient-para-conectarte-al-servicio-netconf)
  - [Paso 3. Agrega una función de impresión al script para que se muestren las capacidades NETCONF para ### el CSR1kv](#paso-3-agrega-una-función-de-impresión-al-script-para-que-se-muestren-las-capacidades-netconf-para--el-csr1kv)
- [Parte 4. Usa ncclient para recuperar la configuración](#parte-4-usa-ncclient-para-recuperar-la-configuración)
  - [Paso 1. Usa la función get\_config() para recuperar la configuración en ejecución de R1](#paso-1-usa-la-función-get_config-para-recuperar-la-configuración-en-ejecución-de-r1)
  - [Paso 2. Usa Python para embellecer el XML.](#paso-2-usa-python-para-embellecer-el-xml)
  - [Paso 3. Usa un filtro con get\_config() para recuperar solo un modelo YANG específico](#paso-3-usa-un-filtro-con-get_config-para-recuperar-solo-un-modelo-yang-específico)
- [Parte 5. Usa ncclient para configurar un dispositivo](#parte-5-usa-ncclient-para-configurar-un-dispositivo)
  - [Paso 1. Usa ncclient para editar el nombre de host del CSR1kv](#paso-1-usa-ncclient-para-editar-el-nombre-de-host-del-csr1kv)
  - [Paso 2. Usa ncclient para crear una nueva interfaz loopback en R1](#paso-2-usa-ncclient-para-crear-una-nueva-interfaz-loopback-en-r1)
  - [Paso 3. Intenta crear una nueva interfaz loopback con la misma dirección IPv4](#paso-3-intenta-crear-una-nueva-interfaz-loopback-con-la-misma-dirección-ipv4)
- [Parte 6. Desafío: Modifica el programa utilizado en este laboratorio](#parte-6-desafío-modifica-el-programa-utilizado-en-este-laboratorio)
- [Conclusiones y reflexiones](#conclusiones-y-reflexiones)

> Para este laboratorio usamos [esta guía en inglés.](https://itexamanswers.net/8-3-6-lab-use-netconf-to-access-an-ios-xe-device-answers.html)

---
## Parte 1. Inicia las máquinas virtuales y verifica la conectividad

### Paso 1. Inicia las máquinas virtuales



### Paso 2. Verifica la conectividad entre las máquinas virtuales



### Paso 3. Verifica la conectividad SSH a la máquina virtual CSR1kv



---
## Parte 2. Usa una sesión NETCONF para recopilar información

### Paso 1. Verifica si NETCONF se está ejecutando en el CSR1kv



### Paso 2. Accede al proceso NETCONF a través de una terminal SSH



### Paso 3. Inicia una sesión NETCONF enviando un mensaje de saludo desde el cliente



### Paso 4. Envía mensajes RPC a un dispositivo IOS XE



### Paso 5. Cierra la sesión NETCONF



---
## Parte 3. Usa ncclient para conectarte a NETCONF

### Paso 1. Verifica que ncclient esté instalado y listo para usar



### Paso 2. Crea un script para usar ncclient para conectarte al servicio NETCONF



### Paso 3. Agrega una función de impresión al script para que se muestren las capacidades NETCONF para ### el CSR1kv



---
## Parte 4. Usa ncclient para recuperar la configuración

### Paso 1. Usa la función get_config() para recuperar la configuración en ejecución de R1



### Paso 2. Usa Python para embellecer el XML.



### Paso 3. Usa un filtro con get_config() para recuperar solo un modelo YANG específico



---
## Parte 5. Usa ncclient para configurar un dispositivo

### Paso 1. Usa ncclient para editar el nombre de host del CSR1kv



### Paso 2. Usa ncclient para crear una nueva interfaz loopback en R1



### Paso 3. Intenta crear una nueva interfaz loopback con la misma dirección IPv4



---
## Parte 6. Desafío: Modifica el programa utilizado en este laboratorio

---
## Conclusiones y reflexiones

