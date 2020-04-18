from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)
app.debug = True


# setting debug as active

@app.route('/formularz', methods=['POST'])
def formularz():
    # dane z formularzy znajdują się w obiekcie request.form
    # informacja o typie żądania jest w request.method
    wiek = request.form['wiek']
    imie = request.form['imie']
    return witaj(imie, wiek)


# jedna funkcja może być dostęp na pod kilkoma adresami
# wtedy dodajemy kilka dekoratorów
@app.route('/witaj-czlowieku')
@app.route('/witaj-czlowieku/<imie>')
@app.route('/witaj-czlowieku/<imie>/<path:wiek>')
def witaj(imie='Łukasz', wiek=18):
    imie = imie.capitalize()

    # we flasku print nie wyświetla nic użytkownikowi
    # odkłada się on w consoli w postaci logów
    print(f"Hej {imie}, masz {wiek} lat")

    # generowanie adresów do funkcji
    print(url_for('witaj', imie='Ewa')) #DOBRZE
    print('/witaj-czlowieku/Ewa') # ZLE

    # do szablonu/templatki możemy przekazać dowolną ilość danych pod dowolnymi nazwami parametrów
    return render_template('index.html', t_imie=imie, t_wiek=wiek)

# uruchomienie serwera flask
app.run()
