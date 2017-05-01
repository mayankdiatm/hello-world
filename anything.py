# import
import goslate
gs = goslate.Goslate()
data = raw_input("data : ")
lan_id = raw_input("Translate Language To : ")
print (gs.translate(data , lan_id))
