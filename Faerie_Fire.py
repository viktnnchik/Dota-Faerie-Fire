from flask import Flask, request, jsonify
import json
import threading
import time
from pyautogui import press

app = Flask(__name__)

def press_key(key, times):
    for _ in range(times):
        press(key)
        time.sleep(0.001)  

@app.route('/', methods=['POST'])
def index():
    try:
        data = request.json
        
        if 'hero' in data:
            hero_data = data['hero']
            if 'health' in hero_data and 'max_health' in hero_data and 'health_percent' in hero_data:
                current_health = hero_data['health']
                max_health = hero_data['max_health']
                health_percentage = hero_data['health_percent']
                
                print(f"Текущий показатель здоровья: {current_health}")
                print(f"Максимальное здоровье: {max_health}")
                print(f"Процент здоровья: {health_percentage}%")
                
                if current_health <= 350:
                    threading.Thread(target=press_key, args=('7', 2)).start()
                
                return "Data received", 200
            else:
                print("Нет данных о здоровье героя.")
                return "No health data available", 400
        else:
            print("Неверный формат данных: отсутствует информация о герое.")
            return "Invalid data format", 400
    except Exception as e:
        print(f"Ошибка: {e}")
        return "Error processing data", 500

if __name__ == '__main__':
    app.run(port=3000, threaded=True)
