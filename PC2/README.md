# Práctica calificada 2

## Preguntas

1. Cada pregunta vale 1.5 puntos
   1. ¿Cómo agregaría la dirección 192.168.121.45 con máscara de red 24 al dispositivo eth1?
   2. ¿Cómo pondría en línea la interfaz la interface enp2s0?
   3. El comando `neigbour` se utiliza para ver la dirección MAC de los dispositivos conectados a su sistema. ¿Cómo añadiría con el comando `ip` la entrada ARP (address resolution protocol) con el IP 192.168.1.50/16 a la interface eth0?
   4. ¿Cómo mostraría solo el enrutamiento de una red específica, por ejemplo 172.17.0.0/20?
   5. ¿Cómo desactivaría completamente el servicio NetworkManager?
2. Describa brevemente las mejores prácticas en la contrucción de una API Rest.
3. Explica por qué el cambio es inevitable en sistemas complejos y proporciona ejemplos (además de la creación de prototipos y la entrega incremental) de actividades de procesos de software que ayuden a predecir cambios y hacer que el software que se está desarrollando sea más resistente al cambio.
4. ¿Cuál es la diferencia entre autorización y autenticación?
5. Describa los beneficios de la automatización de red.
6. ¿Cuáles son las similitudes entre las metodologías Lean y Agile.
7. Describa brevemente el proceso Scrum.

## Solución

1. Cada pregunta vale 1.5 puntos
   1. ¿Cómo agregaría la dirección 192.168.121.45 con máscara de red 24 al dispositivo eth1?
   - 
   2. ¿Cómo pondría en línea la interfaz enp2s0?
   - Con el comando `inconfig enp2s0 up`
   3. El comando `neighbour` se utiliza para ver la dirección MAC de los dispositivos conectados a su sistema. ¿Cómo añadiría con el comando `ip` la entrada ARP (address resolution protocol) con el IP 192.168.1.50/16 a la interface eth0?
   - 
   4. ¿Cómo mostraría solo el enrutamiento de una red específica, por ejemplo 172.17.0.0/20?
   - En Linux, con el comando `traceroute 172.17.0.0/20`
   5. ¿Cómo desactivaría completamente el servicio NetworkManager?
   - 
2. Describa brevemente las mejores prácticas en la contrucción de una API Rest.
- 
3. Explica por qué el cambio es inevitable en sistemas complejos y proporciona ejemplos (además de la creación de prototipos y la entrega incremental) de actividades de procesos de software que ayuden a predecir cambios y hacer que el software que se está desarrollando sea más resistente al cambio.
- 
4. ¿Cuál es la diferencia entre autorización y autenticación?
- La autenticación antecede a la autorización, generalmente. La autenticación es un mecanismo para verificar la identidad de una persona o entidad. La autorización constituye el permiso para acceder a cierto recurso, y generalmente este permiso está asociado a la identidad para que algunas entidades puedan acceder y otras no.
5. Describa los beneficios de la automatización de red.
- La automatización de red libera a los administradores de red mucho del trabajo manual que tendrían realizar sin esta. Esto aporta varios beneficios: menos errores humanos, más tiempo para dedicarlo a tareas más importantes, mayor flexibilidad y escalabilidad de la red, menos gastos operativos y debidos a errores.
6. ¿Cuáles son las similitudes entre las metodologías Lean y Agile.
- 