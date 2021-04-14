import sql_interface as sql

while True:

    stc = input("What is your query? \n")
    print(stc)
    if stc == "":
        sql.close()
        break
    elif stc.split()[0].lower() == "select": 
        res = sql.pandas_select(stc)
        print(res)
    else:
        res = sql.sql_query(stc)
        print(res)
        

