from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def contatena():
    nome='Daniel'
    frase='da a bundinha'
    juncao=f'O {nome} {frase}'

    return render_template(
        'index.html',
        concat=juncao        
    )





if __name__ == "__main__":
    app.run(debug=True)