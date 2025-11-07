from core.GameManager import GameManager

# Bu dosya oyunun başlangıç noktasıdır.
# GameManager (tekil oyun yöneticisi) buradan çağrılır.

if __name__ == "__main__":
    game = GameManager.get_instance()  # Tek örnek oluştur
    game.run()  # Oyun döngüsünü başlat