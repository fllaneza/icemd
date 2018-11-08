# EC2
* **ec2_modelling.ipynb**: Notebook donde se realiza un proceso de modelización habitual con la librería de Machine Learning de Python sci-kit learn. 

* **app.py**: aplicación Hello World realizada con Flask. Para levantarla, llamar al script desde la terminal con el siguiente comando:
```
sudo python app.py
```
y a continuación visitar la IP de la máquina (X.X.X.X) en el navegador web.

* **app_rl.py**: aplicación realizada con Flask para consumir el modelo construido en *ec2_modelling.ipynb* con peticiones HTTP-POST. Para levantarla, llamar al script desde la terminal con el siguiente comando:
```
sudo python app_rl.py
```
y a continuación realizar una petición con el siguiente comando:
```
curl --data '{"CRIM":0.10574,"ZN":0.0,"INDUS":27.74,"CHAS":0.0,"NOX":0.609,"RM":5.983,"AGE":98.8,"DIS":1.8681,"RAD":4.0,"TAX":711.0,"PTRATIO":20.1,"B":390.11,"LSTAT":18.07}' http://X.X.X.X/predict
```
