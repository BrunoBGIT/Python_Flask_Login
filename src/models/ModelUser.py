from .entities.user import User
from logging import exception


class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql=("SELECT id, username, password, fullname FROM users WHERE username='{}'".format(user.username))
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1], User.check_password(row[2],user.password), row[3])
                return user



            else:
                return None

        except Exception as ex:
            raise Exception(ex)
             
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql=("SELECT id, username, fullname FROM users WHERE id={}".format(id))
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                logged_user=User(row[0],row[1], None, row[2])
                return logged_user
                # Tambien puede ser --> return User(row[0],row[1], None, row[2])



            else:
                return None

        except Exception as ex:
            raise Exception(ex)
             