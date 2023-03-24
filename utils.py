from classes import Vacancy, HH, Superjob


def vacancy_to_json(keyword):
    hh_list = HH(keyword).answer
    vac_dict = {'items':[]}
    for vac in range(500):
        vacancy_hh = Vacancy(hh_list[vac]['name'], hh_list[vac]['alternate_url'],
                             hh_list[vac]['snippet']['requirement'], hh_list[vac]['salary'])
        vac_dict['items'].append({'id': vac})
        vac_dict['items'][vac]['vacancy'] = vacancy_hh.to_json()

    return vac_dict

vac_list = vacancy_to_json('python')
print(vac_list)