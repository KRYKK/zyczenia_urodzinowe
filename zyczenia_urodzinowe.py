import datetime

# STALE
ROK = datetime.datetime.now().year


# zmienne
imie_nadawcy = input("Podaj swoje imię: ")
tekst_przywitania = ("Cześć {}!")
zyczenia = ("""
Wszystkiego najlepszego z okazji Twoich {} urodzin!
Szczęścia i pomyślności. Spełniaj swoje marzenia !

Ściskam Cię mocno,
{} """)

# przetwarzanie
print(tekst_przywitania.format(imie_nadawcy))
print("""
Jestem programem do tworzenia życzeń urodzinowych. 
Podaj kilka informacji, a wyślę życzenia do Twojego bliskiego :) 
""")

imie_jubilata = str(input("Podaj imię jubilata: "))
rok_urodzenia = int(input("Podaj rok urodzenia jubilata: "))
ROZNICA = ROK - rok_urodzenia

print("Poniżej proponowana treść życzeń: ")
print(tekst_przywitania.format(imie_jubilata))
print(zyczenia.format(ROZNICA, imie_nadawcy))

