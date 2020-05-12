def song_decoder(song):
    my_list = ' '.join(song.strip("WUB").split("WUB"))
    temp_str = ' '
    for element in my_list:
        if element != ' ':
            temp_str+= ' ' + element
            
    return temp_str

print("WUBHellWUBYoWUBWUBYouWUB")