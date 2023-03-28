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
                             sj_list[vac]['candidat'], sj_list[vac]['payment_to'])
        vac_dict['items'].append({'id': vac + 500})
        vac_dict['items'][vac + 500]['vacancy'] = vacancy_sj.to_json()

    return vac_dict

def sorting(vacancy_json):
    vac_list = vacancy_json['items']
    vac_sorted = sorted(vac_list, key=lambda vacancy: vacancy['vacancy']['salary'], reverse=True)
    return {'items':vac_sorted}

def get_top_10(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        top_10 = sorting(data)['items'][0:10]
    return top_10

# vac_list = vacancy_to_json('python')
# # print(vac_list['items'][0])
# vac_srez = vac_list['items']
# print(vac_srez)
# vac = sorted(vac_srez, key=lambda vacancy: vacancy['vacancy']['salary'], reverse=True)
# print(vac)
# a=Connector()
# a.data_file = 'python'
# a.insert(vacancy_to_json('python'))
# with open('aaa.json', 'w+', encoding="utf-8") as file:
#     f=json.dumps([1, 'simple', 'list'])
#     file.write(f)
# a=Connector()
# a.data_file = 'aaa'
# a.insert(vacancy_to_json('python'))
# a.insert(sorting(vacancy_to_json('python')))
# print(a.select({'salary':200000}))
# a.delete({'salary':500000})
# print(a.select({'salary':500000}))
# print(get_top_10('aaa'))
