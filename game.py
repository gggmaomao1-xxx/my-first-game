import random

def guess_game():
    target = random.randint(1, 100)
    print("1から100の間で数字を当ててみてね！")
    
    attempts = 0
    while True:
        try:
            guess = int(input("数字を入力してね: "))
            attempts += 1
            
            if guess < target:
                print("もっと大きいよ！")
            elif guess > target:
                print("もっと小さいよ！")
            else:
                print(f"おめでとう！{attempts}回目で正解です！")
                break
        except ValueError:
            print("数字を入れてね。")

if __name__ == "__main__":
    guess_game()
