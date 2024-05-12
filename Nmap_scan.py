import subprocess
#Функция для сканирования цели.
def scan(target):
    try:
        result = subprocess.check_output(["nmap", "-sV", target])
        return result
    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении nmap: ", e)
target = input("Введите цель для сканирования: ")
result = scan(target)
print(result)