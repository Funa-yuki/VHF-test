import re
import sqlite3
from time import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
h.setFormatter(fmt)
logger.addHandler(h)


# def escape_long_fetch(cur, que, request):
#     fetch = 0
#     for e in cur:
#         fetch += 1
#     cur.execute(que)
#     if fetch > 1:
#         logger.error("two or more result")
#         cur.execute("")

#     ti = int(time())
#     co = sqlite3.connect("access.sqlite3")
#     cu = co.cursor()
#     ip = request.client_ip_addr
#     user = request.client_user_agent
#     query = "insert into access values ('{user}', '{ip}', {time})".format(user=user, ip=ip, time=ti)
#     cu.execute(query)
#     query = "select * from access where ip='{ip}' and time>{time}".format(user=user, ip=ip, time=ti-10)
#     cu.execute(query)
#     fetch = 0
#     for e in cu:
#         fetch += 1
#     if fetch > 3:
#         logger.error("many access")
#         cur.execute("")
#     co.commit()
#     co.close()

#     return cur

# queryを修正する関数（dropとかなくす）


def escape_special_query(cur, query):
    drop_patturn = r"drop"
    turncate_patturn = r"turncate"
    select_patturn = r"select"
    if re.match(drop_patturn, query):
        logger.error("Drop Patturn Detected")
        return ""
    if re.match(turncate_patturn, query):
        logger.error("Turncate Patturn Detected")
        return ""
    if re.match(select_patturn, query):
        cur.execute(query)
        fetch = 0
        for e in cur:
            fetch += 1
        print(fetch)
        cur.__iter__()
        fetch = 0
        for e in cur:
            fetch += 1
        print(fetch)
        if fetch > 1:
            logger.error("two or more result")
            return ""
    return query

# def escape_special_query(cur, query):
#     drop_patturn = r"drop"
#     turncate_patturn = r"turncate"
#     select_patturn = r"select"
#     where_patturn = r"where"
#     comment_patturn = r"--"
#     if re.match(drop_patturn, query):
#         logger.error("Drop Patturn Detected")
#         return ""
#     if re.match(turncate_patturn, query):
#         logger.error("Turncate Patturn Detected")
#         return ""
#     if re.match(select_patturn, query):
#         if not re.search(where_patturn, query):
#             logger.error("No Where Clause Patturn Detected")
#             return ""
#         if re.search(comment_patturn, query):
#             logger.error("Comment Patturn Detected")
#             return ""
#     return query

def reverse_print(s, *args, **kwargs):
    if isinstance(s, str):
        print(s[::-1], *args, **kwargs)
    else:
        print("Not Str")
        print(s, *args, **kwargs)

# is_adminを正しく動かす
# is_adminはlogin試行が正しくできているかの話？
# set_cookieはまたあとで、今回はidとpasswordを毎回調べる
def is_admin(id=None, password=None):
    if id is None or password is None:
        print("Login Required")
        return False
    if id == "admin" and password == "admin_pass":
        return True
    return False

#
def escape_xss_characters(s):
    if isinstance(s, str):
        return "Escape is over :)"
    else:
        return s
