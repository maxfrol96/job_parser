from classes import Vacancy, HH, Superjob
from connector import Connector
import json

def vacancy_to_json(keyword):
    hh_list = HH(keyword).answer
    sj_list =Superjob(keyword).answer
    vac_dict = {'items':[]}
    for vac in range(500):
        vacancy_hh = Vacancy(hh_list[vac]['name'], hh_list[vac]['alternate_url'],
                             hh_list[vac]['snippet']['requirement'], hh_list[vac]['salary'])
        vac_dict['items'].append({'id': vac})
        vac_dict['items'][vac]['vacancy'] = vacancy_hh.to_json()
    for vac in range(500):
        vacancy_sj = Vacancy(sj_list[vac]['profession'], sj_list[vac]['link'],
                             'f', sj_list[vac]['payment_to'])
        vac_dict['items'].append({'id': vac + 500})
        vac_dict['items'][vac + 500]['vacancy'] = vacancy_sj.to_json()

    return vac_dict

# vac_list = vacancy_to_json('python')
# # print(vac_list['items'][0])
# vac_srez = vac_list['items']
# print(vac_srez)
# vac = sorted(vac_srez, key=lambda vacancy: vacancy['vacancy']['salary'], reverse=True)
# print(vac)
a=Connector()
a.data_file = 'aaa'
a.insert(vacancy_to_json('python'))
# with open('aaa.json', 'w+', encoding="utf-8") as file:
#     f=json.dumps([1, 'simple', 'list'])
#     file.write(f)
