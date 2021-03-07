"""

body od 0 do 10 a platí:

Pokud má zakázka méně než 5 bodů, šance na získání je malá.
Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
Pokud má zakázka více bodů, šance na získání je vysoká.

Body přidělují podle následujících kritérií:

Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.

Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje, u velkých občas ano.
Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.

Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod).
Ostatním zemím dej 0.

Konference: Firma loni pořádala odbornou konferenci pro zákazníky.
Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.

Newsletter: Firma též rozesílá newsletter o svém produktu.
Pokud zákazník newsletter odebírá, přičti 1 bod.

Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False.
Funkce vrátí šanci na získání zakázky jako řetězec.

"""
industry = input("V jaké odvětví zákazník podniká?: ")
turnover = int(input("Uveďte výši obratu zákazníka v EUR: "))
country = input("V jaké zemi se zákazníkovi daří nejvíce? (zadejte název v 1.pádu): ")
conference_optional = input("Zúčastnil se zákazník naší konference? (ano/ne): ")
newsletter_optional = input("Odebírá zákazník náš newsletter? (ano/ne): ")

def get_chance(industry, turnover, country, conference=False, newsletter=False):
    count = 0
    conference = False
    newsletter = False
    
    if industry == "automotive":
        count += 3
    elif industry == "retail":
        count += 2
    
    if turnover in range(10, 1001, 1):
        count += 3
    elif turnover >= 1001:
        count += 1
        
    if country in {"Česko", "Slovensko"}:
        count += 3
    elif country in {"Německo", "Francie"}:
        count += 2

    if conference_optional == "ano":
        conference = True
        if conference:
            count += 1

    if newsletter_optional == "ano":
        newsletter = True
        if newsletter:
            count += 1
      
    if count in [6, 7, 8]:
        chance = "střední"
    elif count in [9, 10]:
        chance = "vysoká"
    else:
        chance = "nízká"
    
    return chance


print(f"Šance na získání této zakázky je: {get_chance(industry, turnover, country, conference=False, newsletter=False)}")
