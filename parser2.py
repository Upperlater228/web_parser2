import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def parse_page(url):
    try:
        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Парсинг заголовка страницы
        title = soup.title.string if soup.title else "Заголовок не найден"
        print(f"\nЗаголовок страницы: {title}")
        
        # Парсинг всех разделов (h1-h6)
        print("\nСписок разделов страницы:")
        sections = []
        for level in range(1, 7):
            headings = soup.find_all(f'h{level}')
            for heading in headings:
                section_text = heading.get_text().strip()
                sections.append(f"H{level}: {section_text}")
                print(f"H{level}: {section_text}")
        
        # Сохранение результатов
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"parse_result_{timestamp}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"Заголовок: {title}\n\n")
            f.write("Разделы страницы:\n")
            f.write("\n".join(sections))
        
        print(f"\nДанные сохранены в файл: {filename}")
        return filename
        
    except requests.exceptions.RequestException as e:
        print(f"\nОшибка запроса: {e}")
        return None

def git_operations():
    """Инструкция по работе с Git"""
    print("\nЧтобы закоммитить изменения и отправить на GitHub:")
    print("1. Инициализируйте репозиторий (если еще не сделано):")
    print("   git init")
    print("2. Добавьте файлы в коммит:")
    print("   git add .")
    print("3. Создайте коммит:")
    print('   git commit -m "Добавлен парсер страниц с сохранением разделов"')
    print("4. Создайте репозиторий на GitHub и подключите его:")
    print("   git remote add origin https://github.com/ваш-логин/название-репозитория.git")
    print("5. Отправьте изменения:")
    print("   git push -u origin master")

if __name__ == "__main__":
    url = input("Введите URL для парсинга: ")
    result_file = parse_page(url)
    
    if result_file:
        git_operations()
        