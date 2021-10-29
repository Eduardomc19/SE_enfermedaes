!pip install experta
from experta import *

lista_enferm = []
Enferm_sintomas = []
sintomas_map = {}
d_desc_map = {}
d_tratamiento_map = {}

def preprocess():
    global lista_enferms, Enferm_sintomas, sintomas_map, d_desc_map, d_tratamiento_map
    enferms = open("enferms.txt")
    enferms_t = enferms.read()
    lista_enferms = enferms_t.split("\n")
    enferms.close()
    for enferm in lista_enferms:
        enferm_s_file = open("Sintomas enfermedad/" + enferm + ".txt")
        enferm_s_data = enferm_s_file.read()
        s_list = enferm_s_data.split("\n")
        Enferm_sintomas.append(s_list)
        sintomas_map[str(s_list)] = enferm 
        enferm_s_file.close()
        enferm_s_file = open("Descripcion enfermedad/" + enferm + ".txt")
        enferm_s_data = enferm_s_file.read()
        d_desc_map[enferm] = enferm_s_data
        enferm_s_file.close()
        enferm_s_file = open("Tratamiento/" + enferm + ".txt")
        enferm_s_data = enferm_s_file.read()
        d_tratamiento_map[enferm] = enferm_s_data 
        enferm_s_file.close()
def identify_disease (*arguments): 
    lista_sintomas = []
    for sintoma in arguments:
        lista_sintomas.append(sintoma)
    # Handle key error
    return sintomas_map[str(lista_sintomas)]

def get_detalles(enferm):
    return d_desc_map[enferm]

def get_tratamiento(enferm):
    return d_tratamiento_map[enferm]

def if_not_matched(enferm):
        print("")
        id_enferm = enferm
        enferm_detalles = get_detalles (id_enferm)
        tratamiento = get_tratamiento (id_enferm)
        print("")
        print("La enfermedad más probable que tienes es %s\n" %(id_enferm))
        print("A continuación se ofrece una breve descripción de la enfermedad: \n") 
        print (enferm_detalles+"\n")
        print("Los medicamentos y procedimientos comunes sugeridos por otros médicos reales son:")
        print (tratamiento+"\n")

class Greetings (KnowledgeEngine):
  @DefFacts()
  def _initial_action(self):
    print("")
    print("¡Hola! Soy el Dr. Simio, estoy aquí para ayudarlo a mejorar su salud.") 
    print("Para eso tendrás que responder algunas preguntas sobre tus condiciones")
    print("¿Siente alguno de los siguientes síntomas?")
    print("")
    yield Fact(action="busca_enferm")

@Rule (Fact (action='busca_enferm'), NOT(Fact(jaqueca=W())), salience = 1) 
def sintoma_0(self): 
    self.declare (Fact(jaqueca=input("Jaqueca: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(dolor_espalda=W())), salience = 1) 
def sintoma_1(self):
    self.declare (Fact(dolor_espalda=input("Dolor de espalda: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(dolor_pecho=W())), salience = 1) 
def sintoma_2(self):
    self.declare(Fact(dolor_pecho=input("Dolor de pecho: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(tos=W())), salience = 1) 
def sintoma_3(self):
    self.declare (Fact(tos=input("Tos: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(desmayo=W())), salience = 1)
def sintoma_4(self): 
    self.declare(Fact(desmayo=input("Desmayo: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(fatiga=W())), salience = 1)
def sintoma_5(self): 
    self.declare(Fact(fatiga=input("Fatiga: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(ojos_cansados=W())), salience = 1)
def sintoma_6(self): 
    self.declare(Fact (ojos_cansados=input("Ojos cansados: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(baja_temperatura=W())), salience = 1) 
def sintoma_7(self):
    self.declare(Fact(baja_temperatura=input("Baja temperatura: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(dolor_garganta=W())), salience = 1)
def sintoma_8(self):
    self.declare (Fact(dolor_garganta=input("Dolor de garganta: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(fiebre=W())), salience = 1)
def sintoma_9(self): 
    self.declare(Fact(fiebre=input("Fiebre: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(nausea=W())), salience=1) 
def sintoma_10(self):
    self.declare(Fact(nausea=input("Nausea: ")))

@Rule (Fact (action='busca_enferm'), NOT(Fact(diarrea=W())), salience = 1) 
def sintoma_11(self):
    self.declare(Fact (diarrea=input("Diarrea: ")))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="yes"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="yes"), Fact(fiebre="yes"), Fact(nausea="yes"), Fact(diarrea="yes"))      
def enferm_0(self): 
    self.declare(Fact(enferm="Influenza"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="yes"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="yes"), Fact(baja_temperatura="no"), Fact(dolor_garganta="yes"), Fact(fiebre="yes"), Fact(nausea="no"), Fact(diarrea="yes"))
def enferm_1(self): 
    self.declare(Fact(enferm="Covid"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="yes"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_2(self): 
    self.declare(Fact(enferm="Artritis"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="no"), Fact(dolor_pecho="yes"), Fact(tos="yes"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="yes"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_3(self):
    self.declare(Fact(enferm="Tuberculosis"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="no"), Fact(dolor_pecho="yes"), Fact(tos="yes"), Fact(desmayo="no"), Fact(fatiga="no"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="yes"), Fact(fiebre="no"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_4(self): 
    self.declare(Fact(enferm="Asma"))

@Rule (Fact(action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="no"), Fact(dolor_pecho="yes"), Fact(tos="yes"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="yes"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_5(self): 
    self.declare(Fact(enferm="Neumonia"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="yes"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_6(self): 
    self.declare(Fact(enferm="Epilepsia"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="no"), Fact(dolor_pecho="yes"), Fact(tos="no"), Fact(desmayo="yes"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="yes"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="yes"), Fact(diarrea="no"))
def enferm_7(self):
    self.declare(Fact(enferm="Enfermedad del corazón"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="no"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="yes"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="no"), Fact(diarrea="no"))
def enferm_8(self): 
    self.declare(Fact(enferm="Diabetes"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="no"), Fact(fatiga="no"), Fact(ojos_cansados="yes"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="yes"), Fact(diarrea="no"))
def enferm_9(self): 
    self.declare(Fact(enferm="Glaucoma"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="no"), Fact(fatiga="yes"), Fact(ojos_cansados="yes"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="no"), Fact(diarrea="yes"))
def enferm_10(self): 
    self.declare(Fact(enferm-"Hipertiroidismo"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="yes"), Fact(fatiga="yes"), Fact(ojos_cansados="no"), Fact(baja_temperatura="no"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="yes"), Fact(diarrea="no"))
def enferm_11(self):
    self.declare(Fact(enferm="Golpe de calor"))

@Rule (Fact (action='busca_enferm'), Fact(jaqueca="yes"), Fact(dolor_espalda="no"), Fact(dolor_pecho="no"), Fact(tos="no"), Fact(desmayo="yes"), Fact(fatiga="no"), Fact(ojos_cansados="no"), Fact(baja_temperatura="yes"), Fact(dolor_garganta="no"), Fact(fiebre="no"), Fact(nausea="no"), Fact(vision_borrosa="no"))
def enferm_12(self): 
    self.declare(Fact(enferm="Hipotermia"))

@Rule (Fact (action='busca_enferm'), Fact(enferm=MATCH.enferm), salience = -998) 
def enferm(self, enferm): 
    print("")
    id_enferm = enferm
    enferm_detalles = get_detalles (id_enferm) 
    tratamiento = get_tratamiento (id_enferm)
    print("")
    print("La enfermedad más probable que tienes es %s\n" %(id_enferm)) 
    print("A continuación se ofrece una breve descripción de la enfermedad:\n")
    print(enferm_detalles+"\n")
    print("Los medicamentos y procedimientos comunes sugeridos por otros médicos reales son:")
    print(tratamiento+"\n")

@Rule (Fact (action='busca_enferm'),
      Fact (jaqueca=MATCH.jaqueca), 
      Fact (dolor_espalda=MATCH.dolor_espalda),
      Fact (dolor_pecho=MATCH.dolor_pecho),
      Fact (tos=MATCH.tos),
      Fact (desmayo=MATCH.desmayo), 
      Fact (dolor_garganta=MATCH.dolor_garganta),
      Fact (fatiga=MATCH.fatiga), 
      Fact (baja_temperatura=MATCH.baja_temperatura),
      Fact (fiebre=MATCH.fiebre), 
      Fact (ojos_cansados=MATCH.ojos_cansados),
      Fact (nausea=MATCH.nausea),
      Fact (diarrea=MATCH.diarrea),NOT(Fact(enferm=MATCH.enferm)), salience = -998)

def not_matched(self, jaqueca, dolor_espalda, dolor_pecho, tos, desmayo, dolor_garganta, fatiga, ojos_cansados, baja_temperatura, fiebre, nausea, diarrea):
    print("\nNo encontré ninguna enfermedad que coincida con sus síntomas exactos") 
    lis = [jaqueca, dolor_espalda, dolor_pecho, tos, desmayo, dolor_garganta, fatiga, ojos_cansados, baja_temperatura, fiebre, nausea, diarrea]
    max_count = 0 
    max_enferm = ""
    for key,val in sintomas_map.items():
        count = 0
        temp_list = eval(key)
        for j in range(0,len(lis)):
            if (temp_list[j] == lis[j] and lis[j] == "yes"):
                count = count + 1
        if count > max_count:
            max_count = count
            max_enferm = val
    if_not_matched(max_enferm)

if __name__ == "__main__":
    preprocess()
    engine = Greetings() 
    while (1):
        engine.reset() # Prepara el motor para la ejecución.
        engine.run() # Ejecutado 
        print("¿Le gustaría diagnosticar algunos otros síntomas?")
        if input() == "no":
            exit()
        