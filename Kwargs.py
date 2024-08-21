def hello(**kwargs):
    print('Hello',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')

hello(title='Mr.',first='Isaac',middle='Peter',last='Ang')