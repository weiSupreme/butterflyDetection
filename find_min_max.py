import os

############################################## max: 354, 444, 000040.txt  min: 4, 12, 001094.txt
txt_list = os.listdir("annotations_txt/")
min_box = []
max_box = []
min_area = 2500
max_area = 0
min_txt = ''
max_txt = ''

for txt_name in txt_list:
    print txt_name
    txt = open('annotations_txt/'+txt_name, 'r')
    txt_read = txt.readlines()
    flag = 0
    for line in txt_read:
        if flag == 0:
            flag = 1
            continue
        line = line.split(' ')
        xmin = float(line[0])
        ymin = float(line[1])
        xmax = float(line[2])
        ymax = float(line[3])
        area = (xmax - xmin) * (ymax - ymin)
        if area < min_area:
            min_area = area
            min_box = [xmin, ymin, xmax, ymax]
            min_txt = txt_name
        if area > max_area:
            max_area = area
            max_box = [xmin, ymin, xmax, ymax]
            max_txt = txt_name
    txt.close()
print min_box[2] - min_box[0], ' ', min_box[3] - min_box[1], min_txt
print max_box[2] - max_box[0], ' ', max_box[3] - max_box[1], max_txt
