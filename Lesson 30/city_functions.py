def city_country(city_name, country_name, inhabitants=''): #middle='' необязательный параметр
    """Отдает название города и страны"""
    if inhabitants:
        str = city_name + ', ' + country_name + ', ' + inhabitants
    else:
        str = city_name + ', ' + country_name
    return str.title()

print(city_country("Santiago", "Chile", "451000"))