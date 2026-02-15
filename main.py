
---

## 💡 Исправленная версия основной логики

```python
import time
from datetime import datetime

now = datetime.now()
start_time = datetime(now.year, now.month, now.day, 9, 0)
finish_time = datetime(now.year, now.month, now.day, 16, 20)

print(start_time)
print(finish_time)

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'  # системный путь
# hosts_path = 'hosts.txt'  # для тестирования

redirect_url = '127.0.0.1'  # исправлено: redirest_url → redirect_url
blocked_sites = ['vk.com', 'www.vk.com', 'youtube.com', 'www.youtube.com']

try:
    while True:
        now = datetime.now()
        
        if start_time < now < finish_time:
            print('Доступ закрыт!')
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for site in blocked_sites:
                    if site not in content:
                        file.write(f'{redirect_url} {site}\n')
        else:
            print('Доступ открыт!')
            with open(hosts_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if not any(site in line for site in blocked_sites):
                        file.write(line)
                file.truncate()
        
        time.sleep(5)

except KeyboardInterrupt:
    print('\nСкрипт остановлен пользователем.')