import subprocess

root_sw = 'sudo'
manager = 'yay'
pacs = 'pacchetti.txt'

# -1: no comando
# 0: OK
# 1: errore nel comando

def run_command(command: list, exitOnFail=0) -> int:
    try:
        res = subprocess.run(command)

        if res.returncode != 0:
            print("Ci sono stati dei problemi durante l'operazione: ")
            print(*command)

            if exitOnFail:
                exit(1)

            return 1
        
        return 0
    
    except:
        print("Impossibile eseguire l'operazione: ")
        print(*command)

        if exitOnFail:
            exit(1)

        return -1


def update_base():
    command = [root_sw, 'pacman', '-Syu']

    print("Update Base: ")

    run_command(command, 1)

    print('')


def update_aur():
    global manager
    
    print("Update AUR: ")
    print("Controllo se paru e' installato ...")

    res = run_command(['paru'])

    if res == 1:
        print("Controlla manualmente l'aggiornamento")
        exit(1)

    elif res == 0:
        manager = "paru"
        return

    elif res == -1: # non c'e paru
        run_command(['yay', '-Syu'], 1) # se non riesce muore

        # installa paru
        res = run_command(['yay', '-S', 'paru'])

        if res == 0:
            print("Il gestore pacchetti ora e' paru")
            manager = "paru"
        else:
            print("Continuo ad usare YaY")
            manager = "yay"

    print('')

    return


def load_pacs(pac_file):
    data = []

    with open(pac_file) as file:
        lines = file.readlines()

        for line in lines:
            data.append(line.strip('\n'))

    return data


def install_pacs(packages):
    installed = []
    failed = []
    ignored = []

    print("Installo i pacchetti: \n")

    for pac in packages:
        command = [manager, '-S', pac]

        print(*command)

        # ignora i pacchetti
        if '?' in pac or '*' in pac:
            print('\tIgnorato')

            ignored.append(pac)

            continue

        

        res = run_command(command)

        if res == 0:
            print("Installato")
            installed.append(pac)
        else:
            print("Fallito")
            failed.append(pac)

        print('')

    print(f"Totale pacchetti installati: {len(installed)}")
    print(*installed, sep='\n')
    print('')

    print(f"Totale pacchetti ignorati: {len(ignored)}")
    print(*ignored, sep='\n')
    print('')

    print(f"Totale pacchetti falliti: {len(failed)}")
    print(*failed, sep='\n')
    print('')


def main():
    # aggiorno il sistema
    update_base()
    update_aur()

    packages = load_pacs(pacs)

    install_pacs(packages)


if __name__ == "__main__":
    main()
