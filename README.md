# dotfiles

My dotfiles

## Installazione

Con il comando `python install.py` viene avviato lo script per aggiornare automaticamente il sistema ed installare i pacchetti elencati nel file `pacchetti.txt`.<br>
Lo script va migliorato con le seguenti funzioni:

- Setta ZSH come shell di default
- Sposta automaticamente i file di configurazione nella loro giusta posizione
- Effettua varie operazioni aggiuntive per terminare in automatico la configurazione totale (vedi guida di Powerlevel10k e I3+KDE)

Una volta eseguito lo script, i vari file di configurazione vanno spostati nelle loro appropriate cartelle (leggere i vari README).

### Cartelle

- **zsh**: `~/`
- **vim**: `~/`
- **termite**: `~/.config/termite`
- **i3**: `~/.config/i3`

### Pacchetti

Possono essere aggiunti altri pacchetti a quelli gia' presenti nel file `pacchetti.txt`.

I caratteri `*` e `?` posti dopo il nome di un pacchetto portano ad ignorarlo durante il processo di installazione.


Di seguito modi giusti per aggiungere pacchetti:

```
pacchhetto
pacchetto ?
pacchetto *
```

## Guide

Di seguito ci sono un po' di guide relative ad alcuni software necessari a far funzionare il tutto.

- **Powerlevel10k** (tema ZSH con barre fiche): [guida](https://github.com/romkatv/powerlevel10k#arch-linux)
- **I3 + KDE** (cambiare WM di default di Manjaro con I3): [guida](https://github.com/heckelson/i3-and-kde-plasma)
 
