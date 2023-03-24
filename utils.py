from classes import Vacancy, HH, Superjob


def vacancy_to_json(keyword):
    hh_list = HH(keyword).answer
    sj_list =Superjob(keyword).answer
    vac_dict = {'items':[]}
    for vac in range(500):
        vacancy_hh = Vacancy(hh_list[vac]['name'], hh_list[vac]['alternate_url'],
                             hh_list[vac]['snippet']['requirement'], hh_list[vac]['salary'])
        vacancy_sj = Vacancy(sj_list[vac]['profession'], sj_list[vac]['link'],
                             sj_list[vac]['candidat'], sj_list[vac]['payment_to'])
        vac_dict['items'].append({'id': vac})
        vac_dict['items'].append({'id': vac+500})
        vac_dict['items'][vac]['vacancy'] = vacancy_hh.to_json()
        vac_dict['items'][vac+500]['vacancy'] = vacancy_sj.to_json()

    return vac_dict

vac_list = vacancy_to_json('python')
print(vac_list)