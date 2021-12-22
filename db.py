import sqlite3


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def if_i_will_stupid():
    connect = sqlite3.connect('cafe_db.db')
    cursor = connect.cursor()

    a = convert_to_binary_data('cafe/блинчики к чаю.png')
    b = convert_to_binary_data('cafe/бодрящее кошачье лакомство.png')
    c = convert_to_binary_data('cafe/кристальные баоцзы.png')
    d = convert_to_binary_data('cafe/миндальный тофу.png')
    e = convert_to_binary_data('cafe/мятное желе.png')
    f = convert_to_binary_data('cafe/обжаренные креветки.png')
    g = convert_to_binary_data('cafe/онигири.png')
    h = convert_to_binary_data('cafe/особая грибная пицца.png')
    i = convert_to_binary_data('cafe/острые хлебцы.png')
    j = convert_to_binary_data('cafe/пиала чая.png')
    k = convert_to_binary_data('cafe/рыба белка.png')
    l = convert_to_binary_data('cafe/рыбный шашлычок.png')
    m = convert_to_binary_data('cafe/сок из волчьих крюков.png')
    n = convert_to_binary_data('cafe/суши с креветками.png')
    o = convert_to_binary_data('cafe/трёхцветное данго.png')
    p = convert_to_binary_data('cafe/циплёнок в медовом соусе.png')
    q = convert_to_binary_data('cafe/шарики с креветкой.png')
    r = convert_to_binary_data('cafe/яблочный напиток.png')
    s = convert_to_binary_data('cafe/ягодный напиток с мятой.png')
    cursor.execute("""INSERT INTO menu(img) VALUES(?), (?), (?), (?), (?), (?), (?),
                   (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?)""",
                   [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s])
    connect.commit()

    cursor.close()


def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данный из blob сохранены в: ", filename, "\n")
