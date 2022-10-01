import dbhelpers as db

def get_homes_by_num_of_rooms(rooms):
    cursor = db.connect_db()
    result = db.execute_statement(
        cursor, 'CALL get_homes_by_num_of_rooms(?)', [rooms])
    db.close_connect(cursor)
    return result

def get_homes_by_city_names(city_name):
    cursor = db.connect_db()
    result = db.execute_statement(
        cursor, 'CALL get_homes_by_city_names(?)', [city_name])
    db.close_connect(cursor)
    return result
def get_homes():
    rooms = input("Rooms")
    results = db.run_statement('CALL get_homes_by_num_of_rooms(?)', [rooms])
    return results

results = get_homes()
print(results)
