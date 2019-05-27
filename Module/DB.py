import sqlite3
import datetime

try:
    conn = sqlite3.connect('video.db')
    cursor = conn.cursor()
    print('資料庫連接成功!')
except:
    print('資料庫連接失敗!')
    conn.close()

def checkUser(uid):
    try:
        cursor.execute("SELECT * FROM user WHERE uid = '" + uid + "'")
        user = cursor.fetchone()
        return user
    except:
        print("查詢使用者失敗!")

def register(uid, password, name):
    try:
        currentTime = str(datetime.datetime.now())
        cursor.execute("INSERT INTO user VALUES ('" + uid + "','" + password + "','" + name + "','" + currentTime + "')")
        conn.commit()
        print("註冊成功!")
    except:
        print("註冊失敗!")


def login(uid, password):
    user = checkUser(uid)
    if(user != None):
        if(user[1] == password):
            return user
        else:
            return False
    else:
        return False

def getCollection(uid):
    try:
        dataList = []
        rows = cursor.execute("SELECT * FROM video WHERE uid = '" + uid + "'")
        for row in rows:
            data = {}
            data['type'] = row[1]
            data['img'] = row[2]
            data['title'] = row[3]
            data['author'] = row[4]
            data['view'] = row[5]
            data['description'] = row[6]
            data['link'] = row[7]
            dataList.append(data)

        return dataList
    except:
        print("查詢使用者失敗!")

def addCollection(uid, ty, img, title, author, view, des, link):
    # try:
    cursor.execute("SELECT * FROM video WHERE link = '" + link + "'")
    video = cursor.fetchone()
    if(video == None):
        cursor.execute("INSERT INTO video VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (uid, ty, img, title, author, view, des, link))
        conn.commit()
        return True
    else:
        return False
    # except:
    #     print("新增失敗!")

def delCollection(uid, link):
    try:
        cursor.execute("DELETE FROM video WHERE uid = '" + uid + "' and link = '" + link + "'")
        conn.commit()
    except:
        print("刪除失敗!")

