# Formación ICEMD

En este repositorio se encuentra la información para realizar la parte práctica de la formación. 
Está divida en varias secciones:

* **S3**: contiene los notebooks con los scripts de Python para aprender a manejar las funcionalidades básicas de S3

* **EC2**: contiene los notebooks con los scripts de Python para aprender a realizar un modelo de Machine Learning y disponibilizarlo como API 

* **EMR**: contiene los paths de S3 para lanzar un step de Hive en EMR

La idea es usar una instancia EC2 para correr los códigos. Los pasos a seguir son los siguientes:   

**1.** Levantar una instancia EC2 y conectarse a ella por SSH como vimos en clase. Por ejemplo: 
```
sudo ssh -i file.pem ubuntu@ec2-18-202-243-222.eu-west-1.compute.amazonaws.com
```
**2.** Instalar el gestor de paquetes conda con los siguientes comandos:    
```
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
**3.** Clonar este repositorio y meterse en su directorio: 
```
git clone https://github.com/fllaneza/icemd.git
cd icemd
```
**4.** Construir un entorno Conda con las especificaciones del fichero mediante este comando y activar dicho entorno: 
```
conda create --name entorno_icemd --file conda_env_spec_f.txt.txt
source activate entorno_icemd
```
**5.** Lanzar Jupyter notebook con los siguientes comandos:
```
jupyter notebook --generate-config
sed -ie "s/#c.NotebookApp.ip = 'localhost'/#c.NotebookApp.ip = '*'/g" ~/.jupyter/jupyter_notebook_config.py
jupyter notebook --ip=0.0.0.0
```
**6.** Saldra una dirección url en la terminal para conectarse a Jupyter. Copiarla desde el :8888/?token= en adelante, pegarla en el navegador web y añadirle la IP de la instancia (de la forma X.X.X.X) tal que así:
```
X.X.X.X:8888/?token=...
```
**7.** Jupyter Notebook desplegará su interfaz. Acceder a las carpetas **S3** y **EC2** para realizar las prácticas.

