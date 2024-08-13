from Tables.table_create import table_create as tc
import Tables.constant as con
def main():
    cursor,connection  = tc.createCursor(con.dbname)
    #tc.createTables(cursor)
    #tc.insertVisitor(cursor,connection)
    res = cursor.execute('select * from visitor')
    #names = list(map(lambda x: x[0], res.description))
    #print(names)
    print(res.fetchall())
