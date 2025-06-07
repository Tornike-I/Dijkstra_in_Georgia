from graph import Node, Edge, Map

if __name__ == "__main__":
    georgia = Map()
    georgia.add_new_node("Tbilisi")
    georgia.add_new_node("Kutaisi")
    georgia.add_connection("Tbilisi", "Kutaisi", 15)
    georgia.add_connection("Gudauri", "Tbilisi", 5)
    georgia.add_connection("Gudauri", "Kutaisi", 25)

    print(georgia)