import subprocess
import platform
import time

def ping_host(ip: str) -> bool:
    # Determino il comando ping in base al sistema operativo
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    
    try:
        # Eseguo il comando ping
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        
        # Controllo il risultato del comando ping
        if response.returncode == 0:
            return True  # Host Online
        else:
            return False  # Host Offline
    except subprocess.TimeoutExpired:
        return False  # Timeout (Considero l'host offline)

def main():
    # Chiedo all'utente di inserire gli indirizzi IP
    hosts = input("Inserisci gli indirizzi IP degli host da monitorare, separati da spazio: ").split()
    
    while True:
        for ip in hosts:
            print(f"Verifica dello stato per l'host {ip}...")
            if ping_host(ip):
                print(f"L'host {ip} è online.")
            else:
                print(f"L'host {ip} è offline.")
            time.sleep(1)  # Pausa per non sovraccaricare la rete
        
        # Controllo per inserire nuovi host/interrompere il loop
        command = input("\nPremi 'q' e invio per uscire,\n'n' per inserire nuovi host,\no solo invio per monitorare nuovamente gli IP inseriti: ").strip().lower()
        if command == 'n':
            # Chiedo all'utente di inserire i nuovi indirizzi IP da monitorare
            hosts = input("Inserisci gli indirizzi IP degli host da monitorare, separati da spazio: ").split()
        elif command == 'q':
            print("Interruzione del monitoraggio.")
            break

if __name__ == "__main__":
    main()

