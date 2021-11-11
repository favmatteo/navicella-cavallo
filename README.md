# Navicella Cavallo
## Il miglior gioco in circolazione
Navicella cavallo è un gioco 2D basato sullo stile dei giochi space shooter

![Una partita a Navicella Cavallo](https://i.imgur.com/TFerhsL.png)

## Come installare Navicella Cavallo su ambienti Linux

Ubuntu e derivate:

```sh
# Aggiorna prima il sistema
sudo apt update && sudo apt upgrade

# Installa python, pip e git
sudo apt install python3 python3-pip git

# ora che hai pip installa la libreria grafica pygame
pip install pygame

# scarica il codice ed eseguilo
git clone https://github.com/favmatteo/navicella-cavallo.git
cd navicella-cavallo
python3 main.py
```

Fedora:

```sh
# Aggiorna prima il sistema
sudo dnf upgrade

# Installa python, pip e git
sudo dnf install python3 python3-pip git

# ora che hai pip installa la libreria grafica pygame
pip install pygame

# scarica il codice ed eseguilo
git clone https://github.com/favmatteo/navicella-cavallo.git
cd navicella-cavallo
python3 main.py
```

Arch Linux:
_Il pacchetto al momento non si trova ancora nell'Arch User Repository (AUR)_

```sh
# Aggiorna il sistema e scarica i pacchetti neccesari, in caso siano già presenti puoi reinstallarli 
sudo pacman -Syu python python-pip git

# ora che hai pip installa la libreria grafica pygame
pip install pygame

# scarica il codice ed eseguilo
git clone https://github.com/favmatteo/navicella-cavallo.git
cd navicella-cavallo
python3 main.py
```

## Come installare Navicella Cavallo su Windows:
1. Esegui [questo script](https://pastebin.com/bLYxq1HT) (salvandolo in un file powershell es. test_python.ps1) per verificare se Python è installato sul tuo pc
  - Verifica l'output dello script
    - Se restituisce un output simile a 'Python was not found', vuol dire che nel tuo PC
      python non è installato, o è installato ma non in maniera corretta (controlla che python e pip si trovano nelle variabili
      d'ambiente del sistema!)
    - Se restituisce un output contenente una versione di Python superiore o uguale alla 3.0, allora procedi al punto 3, altrimenti
      installa Python3 dal sito ufficiale o dal Microsoft Store, come è descritto nel punto 2
2. Installa python dal [sito ufficiale](https://www.python.org/) o dal [Microsoft Store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7#activetab=pivot:overviewtab)
   - Nota sull'installazione: qualsiasi versione di Python3 dovrebbe andare bene, per stare sul sicuro consiglio Python3.8 o Python3.9, poichè testate da me.
3. Scarica l'intero pacchetto, premendo [qui](https://github.com/favmatteo/navicella-cavallo/archive/refs/heads/main.zip), ed estrailo in un percorso a tuo piacimento
4. Apri il CMD - se sei su Windows 11 va bene anche Windows Terminal - e digita ``` pip install pygame ```
5. Una volta fatto ciò spostati sul percorso in cui si trova i file di gioco con ``` cd path/to/folder ```
6. Avvia il gioco con ```python main.py ```
7. Divertiti!
