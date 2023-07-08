import sqlite3
import filters
import config
import generic

TABLE_NAME="winner"
COL_ID="id"
COL_YEAR="year"
COL_CATEGORY="category"
COL_NAME="name"
COL_SHOW="show"

def drop_winner_table(db=config.DB_NAME):
    generic.drop_table(TABLE_NAME,db)

def create_winner_table(db=config.DB_NAME):
    print("create_winner_table()")
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    sql = f"""
      create table if not exists {TABLE_NAME} (
      {COL_ID} integer primary key,
      {COL_YEAR} integer,
      {COL_CATEGORY} text not null,
      {COL_NAME} text not null,
      {COL_SHOW} text not null)
      """
    print("sql=" + sql)
    cursor.execute(sql)
    connection.commit()
    connection.close()


def insert_winner(values,db=config.DB_NAME):
    print(f"insert_winner(values={values},db={db})")
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    sql = f"""
      insert into {TABLE_NAME} ({COL_YEAR}, {COL_CATEGORY}, {COL_NAME}, {COL_PERFORMING})
      values (:{COL_YEAR}, :{COL_CATEGORY}, :{COL_NAME}, :{COL_SHOW})
      """
    params = {
        COL_YEAR: filters.dbInteger(values[COL_YEAR]),
        COL_CATEGORY: filters.dbString(values[COL_CATEGORY]),
        COL_NAME: filters.dbString(values[COL_NAME]), 
        COL_SHOW: filters.dbString(values[COL_SHOW]) }
    cursor.execute(sql,params)
    connection.commit()
    connection.close()
    return cursor.lastrowid

def select_winner_by_id(id,db=config.DB_NAME):
    print("select_actor_by_id()")
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    sql = f"""
      select {COL_YEAR}, {COL_NAME} from {TABLE_NAME}
      where ({COL_ID} = :{COL_ID})
      """

    print('sql='+sql)
    params = {COL_ID: filters.dbInteger(id)}
    cursor.execute(sql,params)
    response=cursor.fetchone()
    if response != None:
        return {
            COL_ID : filters.dbInteger(id),
            COL_YEAR: response[0],
            COL_NAME: response[1]
        }
    else:
        return None
    connection.close()

#def test_winner():
#     db="WINNERS"
#     drop_actor_table(db)
#     create_actor_table(db)
#     id1=insert_actor({
#         'year': '1990', 
#         'last': '',
#         'performing': 'The Music Man'},db) 
#     id2=insert_actor({
#         'first': 'Sutton', 
#         'last': 'Foster',
#         'performing': 'The Music Man'},db)
#     row1=select_actor_by_id(id1,db)
#     row2=select_actor_by_id(id2,db)
#     rowNone=select_actor_by_id(32984057,db)
#     if rowNone != None:
#         raise ValueError('not none')
#     if row1['id'] != id1:
#         raise ValueError('id1 id wrong:' + str(row1['ID']))
#     if row1['first'] != 'Hugh':
#         raise ValueError('id1 first name wrong.')
#     if row2['last'] != 'Foster':
#         raise ValueError('id2 last name wrong.')
