from cowinapi_by_ishaan import FetchData
cowin = FetchData()

#Table format
table = cowin.get_states_table()
print(table)

#Listed
lists = cowin.get_states_list()
print(lists)

#distrcits
districts = cowin.get_districts_dict()
print(distrcits)
