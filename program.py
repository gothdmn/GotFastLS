import os

def gotMaker(fn, dn, esx, cfg, lua, nn, o, ver):
    destination = os.path.join(dn, fn)
    os.makedirs(destination, exist_ok=True)

    client = os.path.join(destination, 'client')
    os.makedirs(client, exist_ok=True)

    server = os.path.join(destination, 'server')
    os.makedirs(server, exist_ok=True)

    clientfp = os.path.join(client, 'client.lua')
    if esx == 'T' or esx == 't':
        with open(clientfp, "w") as clientfile:
            clientfile.write("ESX = exports[\"es_extended\"]:getSharedObject()")

    serverfp = os.path.join(server, 'server.lua')
    if esx == 'T' or esx == 't':
        with open(serverfp, "w") as serverfile:
            serverfile.write("ESX = exports[\"es_extended\"]:getSharedObject()")

    manifestfp = os.path.join(destination, 'fxmanifest.lua')
    with open(manifestfp, "w") as manifestfile:
        manifestfile.write("fx_version 'cerulean'\ngame 'gta5'\nname '" + str(fn) + "'" + "\nauthor '" + str(nn) + "'" +"\ndescription '" + str(o) + " made with GotFastLS'" + "\nversion '" + str(ver) + "'")
        if lua == 'T' or lua == 't':
            manifestfile.write("\n\nlua54 'yes'\n")
        manifestfile.write("\nclient_scripts {\n	'client/client.lua'\n}\nserver_scripts {\n	'server/server.lua'\n}\n")
        if cfg == 'T' or cfg == 't':
            manifestfile.write("\nshared_scripts {\n	'config.lua'\n}")

    if cfg == 'T' or cfg == 't':
        cfgfp = os.path.join(destination, 'config.lua')
        with open(cfgfp, "w") as cfgfile:
            cfgfile.write("Config = {}")

if __name__ == '__main__':
    fn = input('Podaj nazwe foldera: ')
    dn = input('Podaj destynacje: ')
    nn = input('Podaj swój nickname: ')
    o = input('Wpisz opis: ')
    ver = input('Wpisz wersje: ')
    lua = input('Uzyc lua54? [T/N]: ')
    esx = input('Uzyc ESX? [T/N]: ')
    cfg = input('Dodac plik konfiguracyjny? [T/N]: ')
    gotMaker(fn, dn, esx, cfg, lua, nn, o, ver)
