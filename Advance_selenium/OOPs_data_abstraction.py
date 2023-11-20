class TV:
    def __init__(self):
        self.__channel = 0  # Private variable to store the channel

    def change_channel(self, new_channel):
        if 0 <= new_channel <= 100:
            self.__channel = new_channel
            print(f'channel changed to {self.__channel}')
        else:
            print('Invalid channel')



my_tv = TV()
my_tv.change_channel(100)
my_tv.show_channel()



