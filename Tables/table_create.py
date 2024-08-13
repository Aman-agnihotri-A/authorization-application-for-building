import sqlite3
class table_create:
    def createCursor(dbname):
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        return cur,con

    def createTables(cur):
        cur.execute("CREATE TABLE admin(ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME TEXT NOT NULL, LAST_NAME TEXT NOT NULL, PHONE_NO INT NOT NULL, ADDRESS TEXT, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
        cur.execute("CREATE TABLE resident(ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME TEXT NOT NULL, LAST_NAME TEXT NOT NULL, PHONE_NO INT NOT NULL, FLAT_NO TEXT NOT NULL, ADDRESS TEXT, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
        cur.execute("CREATE TABLE securitygaurd(ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME TEXT NOT NULL, LAST_NAME TEXT NOT NULL, PHONE_NO INT NOT NULL, CURRENT_ADDRESS TEXT NOT NULL, PERMANENT_ADDRESS TEXT, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
        cur.execute("CREATE TABLE visitor(ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME TEXT NOT NULL, LAST_NAME TEXT NOT NULL, VISIT_PURPOSE TEXT NOT NULL, PHONE_NO INT NOT NULL, VISIT_FLAT TEXT NOT NULL)")
    
    def insertAdmin(cur,con):
        cur.execute("""INSERT INTO admin
                          (first_name,last_name,phone_no, address, username, password) 
                           VALUES 
                          ('aman','agnihotri',8839868871,'AD Crystal','aman','aman')""")
        con.commit()
        cur.execute("""INSERT INTO admin
                          (first_name,last_name,phone_no, address, username, password) 
                           VALUES 
                          ('shani','agnihotri',7000061628,'AD Crystal','shani','shani')""")
        con.commit()
    def insertResident(cur,con):
        cur.execute("""INSERT INTO resident
                          (first_name,last_name,phone_no, flat_no, address, username, password) 
                           VALUES 
                          ('ram niwas','agnihotri',8660672149, '102','AD Crystal','ram','ram')""")
        con.commit()
        cur.execute("""INSERT INTO resident
                          (first_name,last_name,phone_no, flat_no, address, username, password) 
                           VALUES 
                          ('falguna','reddy',123456789, '401','AD Crystal','abc','abc')""")
        con.commit()
    def insertSecurityGaurd(cur,con):
        cur.execute("""INSERT INTO securitygaurd
                          (first_name,last_name,phone_no, current_address, permanent_address, username, password) 
                           VALUES 
                          ('Vishal','kumar',8660675649, 'nepal','AD Crystal','vishal','vishal')""")
        con.commit()
    def insertVisitor(cur,con):
        cur.execute("""INSERT INTO visitor
                          (first_name,last_name, visit_purpose, phone_no, visit_flat) 
                           VALUES 
                          ('Vishal','kumar','delivery',8660675649,'102' )""")
        con.commit()