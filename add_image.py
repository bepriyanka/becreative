import os

a=os.listdir('/home/soumya/Downloads/becreative-master/images')


for i in enumerate(a):
...      print('<div class="item"><div class="animate-box"><a href="images/%s" class="image-popup fh5co-board-img"><img src="images/%s" alt="Free HTML5 Bootstrap template"></a><div class="fh5co-desc">%s</div></div></div>' %(i[1],i[1],i[1][:-4]))

