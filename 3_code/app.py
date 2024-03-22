from flask import Flask, render_template, request, session, redirect, make_response, flash, get_flashed_messages
import json



app = Flask(__name__, template_folder='templates')
app.secret_key = "asdasdas"


nabidka = [
    {
        "název": "čoky",
        "cena": 123
    },
    {
        "název": "piko",
        "cena": 823
    },
    {
        "název": "weedenska",
        "cena": 66712783
    },
    {
        "název": "kybl",
        "cena": 60
    },
    {
        "název": "pica",
        "cena": 100
    }
]


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/picy", methods=["GET"])
def picy():
    return render_template("picy.html", nabidka=nabidka)

@app.route("/objednej", methods=["GET","POST"])
def objednej():
    if request.method == "POST":
        nazev = request.form.get("nazev")
        mnozstvi = int(request.form.get("mnozstvi"))
      #  flash(nazev)
      #  flash(mnozstvi)
        celkova_cena = 0
        for pica_z in nabidka:
            if pica_z["název"] == nazev:
                celkova_cena = mnozstvi * pica_z["cena"]
                break
        with open("fakura.txt", "w") as faktura:
            faktura.write(f"Zaplat:{celkova_cena}")
        return redirect("/")
    return render_template("objednej.html")

@app.route("/api/picy", methods=["GET"])
def api_get_picy():
    return make_response(json.dumps(nabidka, ensure_ascii=False), 200)

@app.route("/api/pica", methods=["GET"])
def api_get_pica():
    nazev = request.args.get("jmeno")
    for pica_z in nabidka:
        if pica_z["název"] == nazev:
            return make_response(json.dumps(pica_z, ensure_ascii=False), 200)
    else:
        chyba = {"chyba": "Pica nenalezena"}
        return make_response(json.dumps(chyba, ensure_ascii=False), 404)
    
@app.route("/api/pica", methods=["POST"])
def api_post_pica():
    nazev = request.args.get("jmeno")
    cena = request.args.get("cena")
    if not nazev or not cena:
        chyba = {"chyba": "Nesprávné parametry"}
        return make_response(json.dumps(chyba, ensure_ascii=False), 400)
    else:
        nova_pica = {"název": nazev, "cena": cena}
        nabidka.append(nova_pica)
        uspech = {"uspech": f"Pica {nazev} úspešně vytvořena"}
        return make_response(json.dumps(uspech, ensure_ascii=False), 200)
    
@app.route("/api/pica", methods=["DELETE"])
def api_delete_pica():
    nazev = request.args.get("jmeno")
    for pica_z in nabidka:
        if pica_z["název"] == nazev:
            nabidka.remove(pica_z)
            smazano = {"smazano": f"Pica {nazev} smazána"}
            return make_response(json.dumps(smazano, ensure_ascii=False), 200)
    else:
        chyba = {"chyba": "Pica nenalezena"}
        return make_response(json.dumps(chyba, ensure_ascii=False), 404)

@app.route("/api/pica", methods=["PUT"])
def api_put_pica():
    nazev = request.args.get("jmeno")
    cena = request.args.get("cena")
    for pica_z in nabidka:
        if pica_z["název"] == nazev:
            pica_z["cena"] = cena
            uspech = {"uspech": f"Pica {nazev} úspešně upravena"}
            return make_response(json.dumps(uspech, ensure_ascii=False), 200)
    else:
        chyba = {"chyba": "Pica nenalezena"}
        return make_response(json.dumps(chyba, ensure_ascii=False), 404)

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True)
    