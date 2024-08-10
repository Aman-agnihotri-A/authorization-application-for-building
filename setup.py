from Tables.table_create import table_create as tc
import Tables.constant as con

cursor = tc.createCursor(con.dbname)
#tc.createTables(cursor)
res = cursor.execute('select * from resident')
names = list(map(lambda x: x[0], res.description))
print(names)