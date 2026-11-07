# app.py
from flask import Flask, render_template_string
import platform
import datetime
import time

# Фиксация глобальной метки старта процесса для расчета Uptime
START_TIME = time.time()

app = Flask(__name__)

# Декларативное описание адаптивного HTML5/CSS3 интерфейса в фирменном стиле БГУИР
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps КР - Вариант 13 (Python/GitHub/WSL)</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #2c3e50;
            margin: 0;
            padding: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
        }
        .container {
            background: #ffffff;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            max-width: 600px;
            width: 100%;
            border-top: 6px solid #00875a;
        }
        h1 { color: #00875a; font-size: 24px; border-bottom: 2px solid #eaedf1; padding-bottom: 12px; margin-top: 0; }
        p { font-size: 14px; line-height: 1.5; color: #7f8c8d; }
        .metrics-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .metrics-table td, .metrics-table th { padding: 12px; text-align: left; border-bottom: 1px solid #eaedf1; }
        .metrics-table th { background-color: #f8f9fa; color: #7f8c8d; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
        .label { font-weight: 600; color: #34495e; }
        .value { font-family: 'Courier New', Courier, monospace; background: #eef2f5; padding: 3px 6px; border-radius: 4px; font-size: 13px; font-weight: bold; }
        .status-badge { color: #ffffff; background-color: #00875a; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: bold; }
        .footer { margin-top: 35px; font-size: 11px; color: #bdc3c7; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Автоматизированная система мониторинга (Flask)</h1>
        <p>Интерфейс подтверждает успешное функционирование сквозного процесса CI/CD. Сборка образа и деплой контейнера выполнены автоматически с использованием GitHub Actions на базе WSL2 Self-Hosted раннера согласно модели бранчинга GitLab Flow.</p>
        
        <table class="metrics-table">
            <thead>
                <tr>
                    <th>Параметр системы</th>
                    <th>Текущее значение метрики</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="label">Состояние контейнера</td>
                    <td><span class="status-badge">ACTIVE</span></td>
                </tr>
                <tr>
                    <td class="label">Версия интерпретатора</td>
                    <td><span class="value">{{ py_version }}</span></td>
                </tr>
                <tr>
                    <td class="label">Операционная система</td>
                    <td><span class="value">{{ os_info }}</span></td>
                </tr>
                <tr>
                    <td class="label">Время работы процесса (Uptime)</td>
                    <td><span class="value">{{ uptime }} сек</span></td>
                </tr>
                <tr>
                    <td class="label">Системное время сервера</td>
                    <td><span class="value">{{ current_time }}</span></td>
                </tr>
            </tbody>
        </table>
        <div class="footer">
            УО БГУИР • Факультет ИБ • Кафедра ИКТ • Контрольная работа • 2026
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Динамический сбор низкоуровневых параметров среды выполнения
    py_ver = f"{platform.python_version()} ({platform.python_implementation()})"
    os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
    
    # Расчет текущего аптайма процесса
    current_uptime = round(time.time() - START_TIME, 1)
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return render_template_string(
        HTML_TEMPLATE,
        py_version=py_ver,
        os_info=os_info,
        uptime=current_uptime,
        current_time=server_time
    )

if __name__ == '__main__':
    # Запуск WSGI-сервера на всех интерфейсах внутри контейнера на порту 80
    app.run(host='0.0.0.0', port=80)
