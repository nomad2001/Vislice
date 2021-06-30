import bottle
import model

vislice = model.Vislice()
COOKIE_SECRET="bnupičgtfhg9rp8gret934t57thzergurg48thfrhreh8"

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/igra/")
def nova_igra():
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    id_igre = vislice.nova_igra()
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)
    bottle.response.set_cookie("ID_IGRE",str(id_igre),path="/",
        secret=COOKIE_SECRET)
    bottle.redirect("/igraj/")

@bottle.get("/igraj/")
def pokazi_igro():
    id_igre=int(
        bottle.request.get_cookie("ID_IGRE",secret=COOKIE_SECRET)
    )
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)

    return bottle.template("igra.tpl",stanje=trenutno_stanje,igra=trenutna_igra)

@bottle.post("/igraj/")
def ugibaj_na_igri():
    id_igre=int(
        bottle.request.get_cookie("ID_IGRE",secret=COOKIE_SECRET)
    )
    vislice = model.Vislice.preberi_iz_datoteke(model.DATOTEKA_ZA_SHRANJEVANJE)
    ugibana = bottle.request.forms.get("crka")
    vislice.ugibaj(id_igre,ugibana)
    vislice.zapisi_v_datoteko(model.DATOTEKA_ZA_SHRANJEVANJE)
    return bottle.redirect("/igraj/")

@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path,"img")

bottle.run(reloader=True,debug=True)