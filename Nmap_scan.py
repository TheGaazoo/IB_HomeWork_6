import subprocess
def scan(target):
    try:
        result = subprocess.check_output(["nmap", "-sV", target])
        # Декодирование байтовой строки в UTF-8
        result = result.decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении nmap: ", e)
# Распарсим результат nmap
def parse_nmap_result(result):
    # Бьем результат на строки и обрабатываем каждую
    for line in result.split('\n'):
        if "open" in line:
            # Дополнительная обработка для строк, содержащих 'open'
            print(line)
target = input("Введите цель для сканирования: ")
result = scan(target)
print(result) # Печать исходного результата
parse_nmap_result(result) # Печать обработанного результата
