import random

print ("********************************")
print ("****** ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ *******")
print ("********************************")

secret_number = random.randint(1, 100)
def main():
    secret_number = random.randint(1, 100)


while True:
    try:
        guess = int(input("ป้อนตัวเลขที่ต้องการ : "))
        
        if guess == secret_number:
            print ("ยินดีด้วยคุณทายถูก")
            break
        elif guess < secret_number:
            print ("คุณทายผิด...ตัวเลขที่ป้อนน้อยเกินไป")
        else:
            print("คุณทายผิด...ตัวเลขที่ป้อนมากไป")

    except ValueError:
        print ("โปรดป้อนตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()
