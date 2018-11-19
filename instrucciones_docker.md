# Instrucciones para ejecutar el API de Flask con Docker

**1.** Construir la imagen Docker a partir del archivo de texto dockerfile
```
sudo docker build -t [NOMBRE DEL DOCKER]:[VERSIÓN] .
```
*Ejemplo:* 
```
sudo docker build -t icemd_app/boston:v0 .
```

## 2.

       

**2.** Una vez construida la imagen, para instanciar un contenedor en tiempo de ejecución se utiliza el siguiente comando:
```
sudo docker run -p [PUERTO DEL HOST]:[PUERTO DEL DOCKER] -v [RUTA LOCAL]:[RUTA DEL DOCKER] [NOMBRE DEL DOCKER]:[VERSIÓN]
```
*Ejemplo:*
```
sudo docker run -p 9999:9999 icemd_app/boston:v0
```


