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
curl -H "Content-Type: application/json" -d "@query.json" -X POST http://127.0.0.1:5000/predict
```
