
- Conexión ssh: 
	sudo ssh -i icemd.pem ubuntu@ec2-18-202-243-222.eu-west-1.compute.amazonaws.com

- Subir fichero a EC2: 
	scp -i icemd.pem datos.csv ubuntu@ec2-18-202-243-222.eu-west-1.compute.amazonaws.com
 
- Bajar fichero a EC2:
	scp -r -i icemd.pem ubuntu@ec2-18-202-243-222.eu-west-1.compute.amazonaws.com . 

- Log de instalaciones previas
	 /var/log/cloud-init-output.log 

- Instalar miniconda3
	curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh

- Exportar entorno conda 
	conda list --explicit > spec-file.txt

- Crear entorno conda a partir de spec-file.txt
	conda create --name myenv --file spec-file.txt

- Override sudo
	sudo() { command sudo env PATH="$PATH" "$@"; }

- HTTP Requests 
	@post
	curl --data '{"CRIM":0.10574,"ZN":0.0,"INDUS":27.74,"CHAS":0.0,"NOX":0.609,"RM":5.983,"AGE":98.8,"DIS":1.8681,"RAD":4.0,"TAX":711.0,"PTRATIO":20.1,"B":390.11,"LSTAT":18.07}' http://34.245.186.52/predict
	curl -H "Content-Type: application/json" -d "@query.json" -X POST http://34.245.186.52/predict

