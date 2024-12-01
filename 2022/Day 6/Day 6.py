def marker(message, marker_length):
    i=0
    while i < len(message)-marker_length+1:
        marker = message[i:i+marker_length]
        unique = set(marker)
        if len(list((filter(lambda x: marker.count(x) == 1, marker)))) == marker_length:
            break
        i+=1
    return i+marker_length
with open("input.txt") as f:
    data = f.read()
    print(marker(data,4))

