import bottle
import model

vislice = model.Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/igra/")
def nova_igra():
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    id_igre = vislice.nova_igra()
    novi_url = f"/igra/{id_igre}/"
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)
    bottle.redirect(novi_url)

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)

    return bottle.template("igra.tpl",stanje=trenutno_stanje,igra=trenutna_igra)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_na_igri(id_igre):
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    ugibana = bottle.request.forms.get("crka")
    vislice.ugibaj(id_igre,ugibana)
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)
    return bottle.redirect(f"/igra/{id_igre}/")

@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path,"img")

bottle.run(reloader=True,debug=True)