from Saxophone import *
from SaxophoneFactory import *

f = TenorSaxophoneFactory()

t = TenorSaxophoneFactory.create()

t.play()
print(t.instrument_type())