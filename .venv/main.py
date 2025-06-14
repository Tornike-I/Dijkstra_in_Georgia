from graph import Node, Edge, Map

if __name__ == "__main__":
    georgia = Map()

    georgia.add_connection("Tbilisi", "Kaspi", 12)
    georgia.add_connection("Tbilisi", "Dusheti", 13)
    georgia.add_connection("Tbilisi", "Gurjani", 20)
    georgia.add_connection("Tbilisi", "Signagi", 13)
    georgia.add_connection("Tbilisi", "Marneuli", 8)
    georgia.add_connection("Tbilisi", "Rustavi", 8)
    georgia.add_connection("Dedoplistskaro", "Signagi", 4)
    georgia.add_connection("Gurjani", "Signagi", 3)
    georgia.add_connection("Gurjani", "Kvareli", 3)
    georgia.add_connection("Gurjani", "Telavi", 7)
    georgia.add_connection("Telavi", "Kvareli", 8)
    georgia.add_connection("Telavi", "Rustavi", 18)
    georgia.add_connection("Telavi", "Dusheti", 18)
    georgia.add_connection("Pasanauri", "Dusheti", 8)
    georgia.add_connection("Pasanauri", "Stepantsminda", 11)
    georgia.add_connection("Marneuli", "Rustavi", 4)
    georgia.add_connection("Kaspi", "Dusheti", 9)
    georgia.add_connection("Kaspi", "Gori", 7)
    georgia.add_connection("Gori", "Khashuri", 13)
    georgia.add_connection("Marneuli", "Borjomi", 44)
    georgia.add_connection("Khashuri", "Borjomi", 6)
    georgia.add_connection("Akhalcikhe", "Borjomi", 12)
    georgia.add_connection("Zestaponi", "Borjomi", 13)
    georgia.add_connection("Zestaponi", "Khashuri", 15)
    georgia.add_connection("Akhalcikhe", "Batumi", 41)
    georgia.add_connection("Kobuleti", "Batumi", 5)
    georgia.add_connection("Kobuleti", "Ozurgeti", 6)
    georgia.add_connection("Bakhmaro", "Ozurgeti", 8)
    georgia.add_connection("Samtredia", "Ozurgeti", 12)
    georgia.add_connection("Poti", "Ozurgeti", 10)
    georgia.add_connection("Poti", "Samtredia", 18)
    georgia.add_connection("Vani", "Samtredia", 3)
    georgia.add_connection("Poti", "Senaki", 10)
    georgia.add_connection("Zestaponi", "Ambrolauri", 13)
    georgia.add_connection("Kutaisi", "Ambrolauri", 15)
    georgia.add_connection("Kutaisi", "Zestaponi", 9)
    georgia.add_connection("Senaki", "Samtredia", 7)
    georgia.add_connection("Senaki", "Zugdidi", 9)
    georgia.add_connection("Kutaisi", "Samtredia", 10)
    georgia.add_connection("Kutaisi", "Martvili", 10)
    georgia.add_connection("Senaki", "Martvili", 9)
    georgia.add_connection("Zugdidi", "Martvili", 13)
    georgia.add_connection("Mestia", "Ambrolauri", 24)
    georgia.add_connection("Mestia", "Zugdidi", 32)

    print(georgia.dijkstra("Dedoplistskaro", "Mestia"))