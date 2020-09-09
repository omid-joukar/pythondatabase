# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sqlite3
class Database:
     @property
     def filename(self):
          return self._filename
     @filename.setter
     def filename(self,filename):
          self._filename = filename
          self._db = sqlite3.connect(filename)
          self._db.row_factory = sqlite3.Row
     @filename.deleter
     def filename(self):
          self.close()
     @property
     def table(self):
         return self._table
     @table.setter
     def table(self,tb):
          self._table = tb
     @table.deleter
     def table(self):
          self._table = 'test'
     def close(self):
          self._db.close()
          del self._filename
     def __init__(self,**kwargs):
          self.filename = kwargs.get('filename')
          self.table = kwargs.get('table')
     def do_sql(self,sql,*params):
          self._db.execute(sql , params)
          self._db.commit()
     def insert(self,row):
          self._db.execute('insert into {} values(? , ?)'.format(self._table),(row['t1'],row['i1']))
     def update(self , row):
          self._db.execute('update {} set i1 = ? where t1= ?'.format(self._table),(row['i1'],row['t1']))
          self._db.commit()
     def delete(self,key):
          self._db.execute('delete from {} where t1=?'.format(self._table) , (key,))
          self._db.commit()
     def __iter__(self):
          cursor = self._db.execute('select * from {}'.format(self._table))
          for row in cursor:
               yield dict(row)
def main():
     db = Database(filename='test.db', table='test')
     print('create table test')
     print('Data base is Created')
     db.do_sql('DROP TABLE IF EXISTS test')
     db.do_sql('CREATE TABLE test(t1 text , i1 int)')
     print('Create Rows')
     db.insert(dict(t1='one', i1=1))
     db.insert(dict(t1='two', i1=2))
     db.insert(dict(t1='three', i1=3))
     db.insert(dict(t1='four', i1=4))
     for row in db:
          print(row)
     print('Update rows')
     db.update(dict(t1='one', i1=101))
     db.update(dict(t1='two', i1=102))
     for row in db:
          print(row)
     print('Delete')
     db.delete('one')
     db.delete('three')
     for row in db:
          print(row)

if __name__=="__main__":main()