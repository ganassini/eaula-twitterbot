from request.check_website_status import check_website_status
from tweet.api_request import post_tweet
from time import sleep
from os import system

was_up = True              # True se iniciar o bot com o eaula fora do ar e False se estiver up
times_ran = 1

if __name__ == "__main__":
    while True:
        is_up = check_website_status("https://e-aula.ufpel.edu.br")
        if is_up:
            if was_up:
                pass
            if not was_up:
                post_tweet(up=True)
                was_up = True
        elif not is_up:
            if not was_up:
                pass
            if was_up:
                post_tweet(up=False)
                was_up = False
        for i in range(1, 60):
            print(f"{i}s")
            print(f"{times_ran} execuções")
            sleep(1)
            system('cls')
        times_ran += 1
