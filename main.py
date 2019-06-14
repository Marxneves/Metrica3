from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)

@app.route("/")
def deputados():
       
   colors = [
    "#0351EC", "#BF3FA9", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

   obj = DadosAbertos()
   list_dep = obj.deputados()
   info = obj.deputado_id(id)
    
   sexos = {}  
   cont = 1
   for dep in list_dep:
        info = obj.deputado_id(dep['id'])
        sexo = info['sexo']
        if sexo in sexos:
             sexos[sexo] += 1
           #  if cont == 20:
            #   break
        else:
          sexos[sexo]  =  1
       # cont += 1
   print(sexos)
   
   labels=sexos.keys()
   values=sexos.values()

   
   return render_template('index.html', title='Quantidade de deputados Homens x Mulheres', max=400, set=zip(values, labels, colors))

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)