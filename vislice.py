import bottle
import model

vislice = model.Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    novi_url = f"/igra/{id_igre}/"
    bottle.redirect(novi_url)

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]


    return bottle.template("igra.tpl",stanje=trenutno_stanje,igra=trenutna_igra)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_na_igri(id_igre):
    ugibana = bottle.request.forms.get("crka")
    vislice.ugibaj(id_igre,ugibana)

    return bottle.redirect(f"/igra/{id_igre}/")

@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path,"img")

bottle.run(reloader=True,debug=True)