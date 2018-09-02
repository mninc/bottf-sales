import requests
import os
import time
currencies = ["Refined Metal", "Reclaimed Metal", "Scrap Metal"]
added = []
path = "/var/www/bottf-sales/"


def all_same(itera, key):
    first = itera[0]
    for item in itera:
        if item in currencies or (key and item == "Mann Co. Supply Crate Key"):
            return False
        if item != first:
            return False
    return True


while True:
    try:
        time.sleep(2)
        page = requests.get("http://bot.tf/json/stats").json()
        for trade in page["latestTrades"]:
            if "alert-success" in trade["HTML"] and trade["ID"] not in added:
                gaining = []
                losing = []
                added.append(trade["ID"])
                user, bot = trade["HTML"].split("for their")
                items = user.split("</div>")
                first = False
                for item in items:
                    nxt = False
                    for bit in item.split("="):
                        if "title" in bit:
                            nxt = True
                        elif nxt:
                            if not first:
                                print(bit)
                                first = True
                                break
                            else:
                                name = bit[1:-7]
                                gaining.append(name)
                                break
                items = bot.split("</div>")

                for item in items:
                    nxt = False
                    for bit in item.split("="):
                        if "title" in bit:
                            nxt = True
                        elif nxt:
                            if not first:
                                first = True
                                break
                            else:
                                name = bit[1:-7]
                                losing.append(name)
                                break

                if len(losing) == 0 or len(gaining) == 0:
                    continue
                if all_same(losing, True):
                    item = losing[0]
                elif all_same(gaining, True):
                    item = gaining[0]
                elif all_same(losing, False):
                    item = losing[0]
                elif all_same(gaining, False):
                    item = gaining[0]
                else:
                    continue

                if os.path.isfile(path + item + ".html"):
                    with open(path + item + ".html", "r") as f:
                        previous = f.read()
                    if os.stat(path + item + ".html").st_size > 100000:
                        previous = "\n\n".join(previous.split("\n\n")[:-2])
                else:
                    previous = ""
                _losing = {}
                for name in losing:
                    if name in _losing:
                        _losing[name] += 1
                    else:
                        _losing[name] = 1
                _gaining = {}
                for name in gaining:
                    if name in _gaining:
                        _gaining[name] += 1
                    else:
                        _gaining[name] = 1
                losing = []
                gaining = []
                for name, amount in _losing.items():
                    if amount == 1:
                        losing.append(name)
                    else:
                        losing.append(name + " x" + str(amount))
                for name, amount in _gaining.items():
                    if amount == 1:
                        gaining.append(name)
                    else:
                        gaining.append(name + " x" + str(amount))

                surl = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars"
                user = trade["HTML"].find(surl)
                user = trade["HTML"][user + len(surl):]
                user = user[:user.find("_full")]

                response = requests.get("https://steamid.eu/avatar-finder" + user)
                x = response.text
                x = x[x.find("<div class=\"well\">"):]
                y = x.find("/profile/")
                x = x[y + len("/profile/"):]
                x = x[:x.find("\">")]
                user_1 = x

                user = trade["HTML"][trade["HTML"].find("offered"):].find(surl)
                user = trade["HTML"][trade["HTML"].find("offered"):][user + len(surl):]
                user = user[:user.find("_full")]
                response = requests.get("https://steamid.eu/avatar-finder" + user)
                x = response.text
                x = x[x.find("<div class=\"well\">"):]
                y = x.find("/profile/")
                x = x[y + len("/profile/"):]
                x = x[:x.find("\">")]
                user_2 = x

                with open(path + item + ".html", "w") as f:
                    f.write("<a href='/bottf-sales.php?page=" + str(trade["ID"]) + "' >Trade at " + time.strftime("%Y-%m-%d %H:%M") + "</a>")
                    f.write("\n")
                    f.write("Gaining:")
                    f.write("\n")
                    f.write(", ".join(gaining))
                    f.write("\n")
                    f.write("Losing:")
                    f.write("\n")
                    f.write(", ".join(losing))
                    f.write("\n")
                    f.write("\n")
                    f.write(previous)
                with open(path + str(trade["ID"]) + ".html", "w") as f:
                    f.write("<a href='/bottf-sales.php?page=" + str(trade["ID"]) + "' >Trade at " + time.strftime(
                        "%Y-%m-%d %H:%M") + "</a>")
                    f.write("\n")
                    f.write("Gaining:")
                    f.write("\n")
                    f.write(", ".join(gaining))
                    f.write("\n")
                    f.write("Losing:")
                    f.write("\n")
                    f.write(", ".join(losing))
                    f.write("\n")
                    f.write("\n")
                    f.write("Profiles: These have to be found by using their profile image to find their profile.\n")
                    f.write("Because of this profiles may be non-existent or incorrect.\n")
                    if user_1:
                        f.write("<a href='http://backpack.tf/profiles/" + user_1 + "' >User's profile</a>")
                        f.write("\n")
                    if user_2:
                        f.write("<a href='http://backpack.tf/profiles/" + user_2 + "' >Bot's profile</a>")
                        f.write("\n")
                    f.write("\nPretty trade:\n")
                    f.write(trade["HTML"])
    except Exception as e:
        with open(path + "saleserror.html", "w") as f:
            f.write(str(e))

"""            try:
                if os.stat(path + "1.html").st_size > 100000:
                    for i in range(2, 101):
                        if os.path.isfile(path + str(i) + ".html"):
                            pass
                        else:
                            for z in range(1, i):
                                os.rename(path + str(i - z) + ".html",
                                          path + str(i - z + 1) +
                                          ".html")
                            break

                with open(path + "1.html", "a", newline="\n") as f:

                    gaining = []
                    losing = []
                    added.append(trade["ID"])
                    user, bot = trade["HTML"].split("for their")
                    items = user.split("</div>")
                    first = False
                    for item in items:
                        nxt = False
                        for bit in item.split("="):
                            if "title" in bit:
                                nxt = True
                            elif nxt:
                                if not first:
                                    print(bit)
                                    first = True
                                    break
                                else:
                                    name = bit[1:-7]
                                    gaining.append(name)
                                    break
                    items = bot.split("</div>")

                    for item in items:
                        nxt = False
                        for bit in item.split("="):
                            if "title" in bit:
                                nxt = True
                            elif nxt:
                                if not first:
                                    first = True
                                    break
                                else:
                                    name = bit[1:-7]
                                    losing.append(name)
                                    break

                    if
                    f.write("Trade at " + time.strftime("%Y-%m-%d %H:%M"))
                    f.write("\n")
                    f.write("Gaining:")
                    f.write(", ".join(gaining))
                    f.write("\n")
                    f.write("Losing:")
                    f.write("\n")
                    f.write("\n")
                    f.write(", ".join(losing))
                    f.write("\n")
                    f.write("\n")
            except Exception as e:
                print("error")
                print(e)"""