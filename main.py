from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularionotas', methods=['POST', 'GET'])
def formularionotas():
    if request.method == 'GET':
        return render_template('formularionotas.html')
    else:
        nota1 = int(request.form.get('numero1'))
        nota2 = int(request.form.get('numero2'))
        nota3 = int(request.form.get('numero3'))
        asistencia = int(request.form.get('numero4'))
        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'
        notas = {
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3,
            'asistencia': asistencia,
            'promedio': promedio,
            'estado': estado
        }
        return render_template('formularionotas.html', notas=notas)


@app.route('/formularionombres', methods=['POST', 'GET'])
def formularionombres():
    if request.method == 'GET':
        return render_template('formularionombres.html')
    else:
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')
        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)
        return render_template('formularionombres.html', nombres=nombres, nombre_largo=nombre_largo, longitud=longitud)

if __name__ == '__main__':
    app.run(debug=True)
