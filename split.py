import os 

videoname='RaceHorses_832x480_30'
path = f'./data/new/{videoname}'
f_in = './data/RaceHorses_832x480_30.yuv'
f_size = int(832*480*3/2)
with open(f_in, 'rb') as fd_in:
    for i in range (3):
        if not os.path.isdir(path):
            os.mkdir(path)

        f_out = f'./data/new/{videoname}/RaceHorses_832x480_30_{i}.yuv'

        with open(f_out, 'wb') as fd_out:
            # for i in range(100):
            j = i*100
            temp = i*100
            while j < temp+100:
                data = fd_in.read(f_size)
                fd_out.write(data)
                j+=1