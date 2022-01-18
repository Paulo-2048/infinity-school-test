from mysql.connector import Error


class UserConection:
    def __init__(self, conecction):
        self.conecction = conecction

    def insertUser(self, user):
        try:
            sql = 'INSERT INTO user (name, email, password, date, acess) VALUES (%s, %s, %s, %s, %s)'
            command = self.conecction.cursor()
            command.execute(sql, (user.name, user.email,
                            user.password, user.date, user.acess))
            self.conecction.commit()
            return True
        except Error as e:
            print(e)
            pass

    def listing(self):
        try:
            sql = 'SELECT * FROM  user'
            command = self.conecction.cursor()
            command.execute(sql)
            rows = command.fetchall()
            return rows
        except Error as e:
            print(e)
            pass

    def delete_data(self, idCode):
        try:
            sql = 'DELETE from user WHERE iduser = %s;'
            command = self.conecction.cursor()
            command.execute(sql, (idCode,))
            self.conecction.commit()
            return True
        except Error as e:
            print(e)
            pass

    def update_data(self, column, value, idCode):
        try:
            if column == 1:
                sql = 'UPDATE user SET name = %s WHERE iduser = %s ;'
                command = self.conecction.cursor()
                command.execute(sql, (value, idCode))
                self.conecction.commit()
            if column == 2:
                sql = 'UPDATE user SET email = %s WHERE iduser = %s ;'
                command = self.conecction.cursor()
                command.execute(sql, (value, idCode))
                self.conecction.commit()
            if column == 3:
                sql = 'UPDATE user SET acess = %s WHERE iduser = %s;'
                command = self.conecction.cursor()
                command.execute(sql, (int(value), idCode))
                self.conecction.commit()
            return True
        except Error as e:
            print(e)
            pass

    def ver_acess(self, email, senha):
        try:
            sql = f'SELECT * FROM user where email = "{email}" and password = "{senha}"'
            command = self.conecction.cursor()
            command.execute(sql)
            rows = command.fetchall()
            return rows
        except Error as e:
            print(e)
            pass