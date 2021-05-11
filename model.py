import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'L'

DATOTEKA_ZA_SHRANJEVANJE = "podatki.json"

class Vislice:
    def __init__(self, zacetne_igre=None, zacetni_id=0):
        self.igre = zacetne_igre or {}
        self.max_id = zacetni_id
    
    def pretvor_v_json_slovar(self):
        slovar_iger = {}

        for id_igre, (igra,stanje) in self.igre.items():
            slovar_iger[id_igre] = (
                igra.pretvor_v_json_slovar(),
                stanje
            )

        return {
            "max_id": self.max_id,
            "igre": slovar_iger
        }

    def zapisi_v_datoteko(self, datoteka):
        with open(datoteka,"w") as out_file:
            json_slovar = self.pretvor_v_json_slovar()
            json.dump(json_slovar,out_file)    
    @classmethod
    def dobi_iz_json_slovarja(cls, slovar):
        slovar_iger = {}
        for id_igre, (igra_slovar,stanje) in slovar["igre"].items():
            slovar_iger[int(id_igre)] = (
                Igra.dobi_iz_json_slovarja(igra_slovar),stanje
            )
        return Vislice(slovar_iger,slovar["max_id"])

    @staticmethod
    def preberi_iz_datoteke(datoteka):
        with open(datoteka,"r") as in_file:
            json_slovar = json.load(in_file)
        return Vislice.dobi_iz_json_slovarja(json_slovar)

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    def nova_igra(self,):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra()

        self.igre[nov_id] = (sveza_igra,ZACETEK)
        return nov_id

    def ugibaj(self, id_igre, crka):
        #najdi
        igra, _ = self.igre[id_igre]
        #posodobi
        novo_stanje = igra.ugibaj(crka)
        #popravi v slovarju
        self.igre[id_igre] = (igra,novo_stanje)

        return novo_stanje

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(crka in self.crke for crka in self.geslo)

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        s=""

        for crka in self.geslo:
            if crka in self.crke:
                s += crka + ' '
            else:
                s += '_ '
        
        return s
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA
        else: 
            self.crke.append(crka)

            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA
    def pretvor_v_json_slovar(self):
        return {
            "geslo": self.geslo,
            "crke": self.crke
        }

    @staticmethod
    def dobi_iz_json_slovarja(slovar):
        return Igra(slovar["geslo"],slovar["crke"])

with open('besede.txt',"r",encoding="utf-8") as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))