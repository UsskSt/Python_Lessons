from random import randrange
def get_jokes(n):
    joke_list = []
    for joke in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "столб", "монитор"]
adv = ["сегодня", "вчера", "затра", "позавчера", "ночью", "днем", "послезавтра"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "красный", "грустный"]

get_jokes(7)