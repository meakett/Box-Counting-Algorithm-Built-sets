import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


#fern1
image1_url = "https://cdn.phototourl.com/free/2026-06-04-e38011d8-b333-467d-a990-75b5ebe2a41f.jpg"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image1_url, headers=headers) #retreives image via URL


# Open image
img1 = Image.open(BytesIO(response.content)).convert("L")

#img1= img1.resize((500, 500))


threshold = 128
img1_array = np.array(img1)
binary = img1_array < threshold

Lx=img1.size[0] #assign variable to image dimensions
Ly=img1.size[1]

# Show binary image
plt.figure(figsize=(6,6))
plt.imshow(binary, cmap="binary")
plt.title("Binary Image")
plt.axis("off")
plt.show()

#the following defines the black or white value of a (i,j)
thresh = 128  # 0 is black, 255 is white, midway point between the two
for i in range (img1.size[1]):
	for j in range(img1.size[0]):
		if img1_array[i,j] > thresh:
			img1_array[i,j] = 255    # white
		else:
			img1_array[i,j] = 0   # black




def count_boxes(image, box_size):   #fuction for applying box counting to image for later determined box sizes
    N=0
    step=box_size
    for i in range(0, Lx, step):
       for j in range(0, Ly, step):
           if (img1_array[i:i+step,j:j+step] == 0).any(): #any white (i,j) in the range will add to box count
               N=N+1 #counts box if it is occupied

    return N

#box width in px
size1=[10,20,30,40,50,60,70,80,90]

N=0
Ns1=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size1:
    N=count_boxes(img1,size)
    Ns1.append(N)

    size_1 = np.array(size1)

size1=Ly/size_1
size1=1/size1
Ns1=np.array(Ns1)
df1=pd.DataFrame() #create table in console

df1['counted boxes']=Ns1 #creates counted boxes column
df1['box size in px']=size_1 # creates box size column
df1['\epsilon']=size1 #creates column with fractional box size
df1['log (N)']= np.log10(Ns1)
df1['log (1/epsilon)']= np.log10(1/size1)



print(df1) #prints

trend1=np.polyfit(np.log10(1/size1), np.log10(Ns1), 1)
slope1=trend1[0]
D1=trend1[0]


plt.plot(np.log10(1/size1),np.log10(Ns1), 'o',color='violet')
plt.plot(np.log10(1/size1), np.polyval(trend1, np.log10(1/size1)),color='cyan')
plt.xlabel('log 1/$\epsilon$')
plt.ylabel('log N')
plt.title('Fern 1 log N VS log 1/$\epsilon$')
print("Dimension=", D1)
print('width=', Lx ,'height=',Ly)

#fern2
image2_url = "https://cdn.phototourl.com/free/2026-06-04-50c4cc1e-e104-4222-bcaf-51fb5ab3ff76.jpg"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image2_url, headers=headers) #retreives image via URL


# Open image
img2 = Image.open(BytesIO(response.content)).convert("L")
#img2= img2.resize((600, 600))


threshold = 128
img2_array = np.array(img2)
binary = img2_array < threshold

Lx=img2.size[0] #assign variable to image dimensions
Ly=img2.size[1]

# Show binary image
plt.figure(figsize=(6,6))
plt.imshow(binary, cmap="binary")
plt.title("Binary Image")
plt.axis("off")
plt.show()


#the following defines the black or white value of a (i,j)
thresh = 128  # 0 is black 255 is white, midway point between the two
for i in range (img2.size[1]):
	for j in range(img2.size[0]):
		if img2_array[i,j] > thresh:
			img2_array[i,j] = 255    # white
		else:
			img2_array[i,j] = 0   # black



def count_boxes(image, box_size):   #fuction for applying box counting to image for later determined box sizes
    N=0
    step=box_size
    for i in range(0, Lx, step):
       for j in range(0, Ly, step):
           if (img2_array[i:i+step,j:j+step] == 0).any(): #any white (i,j) in the range will add to box count
               N=N+1 #counts box if it is occupied

    return N

size2=[10,20,30,40,50,60,70,80,90]
N=0
Ns2=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size2:
    N=count_boxes(img2,size)
    Ns2.append(N)

    size_2 = np.array(size2)

size2=Ly/size_2

size2=1/size2

Ns2=np.array(Ns2)
df2=pd.DataFrame() #create table in console

df2['counnted boxes']=Ns2 #creates counted boxes column
df2['box size in px']=size_2 # creates box size column
df2['epsilon']=size2 #creates fractional box size column
df2['log (N)']=np.log10(Ns2)
df2['log (1/epsilon)']=np.log10(1/size2)


print(df2) #prints

trend2=np.polyfit(np.log10(1/size2), np.log10(Ns2), 1)
slope2=trend2[0]
D2=trend2[0]


plt.plot(np.log10(1/size2),np.log10(Ns2), 'o',color='violet')
plt.plot(np.log10(1/size2), np.polyval(trend2, np.log10(1/size2)),color='cyan')
plt.xlabel('log 1/$\epsilon$')
plt.ylabel('log N')
plt.title('Fern 2 log N VS log 1/$\epsilon$')
plt.show()
print("Dimension=", D2)
print("width=",Lx, "height=",Ly)

#fern3
image3_url = "https://cdn.phototourl.com/free/2026-06-14-e2c70024-e78d-474d-a4c8-1134da881f4b.jpg"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image3_url, headers=headers) #retreives image via URL


# Open image
img3 = Image.open(BytesIO(response.content)).convert("L")
#img2= img2.resize((600, 600))


threshold = 128
img3_array = np.array(img3)
binary = img3_array < threshold

Lx=img3.size[0] #assign variable to image dimensions
Ly=img3.size[1]

# Show binary image
plt.figure(figsize=(6,6))
plt.imshow(binary, cmap="binary")
plt.title("Binary Image")
plt.axis("off")
plt.show()


#the following defines the black or white value of a (i,j)
thresh = 128  # 0 is black 255 is white, midway point between the two
for i in range (img3.size[1]):
	for j in range(img3.size[0]):
		if img3_array[i,j] > thresh:
			img3_array[i,j] = 255    # white
		else:
			img3_array[i,j] = 0   # black



def count_boxes(image, box_size):   #fuction for applying box counting to image for later determined box sizes
    N=0
    step=box_size
    for i in range(0, Lx, step):
       for j in range(0, Ly, step):
           if (img3_array[i:i+step,j:j+step] == 0).any(): #any white (i,j) in the range will add to box count
               N=N+1 #counts box if it is occupied

    return N

size3=[10,20,30,40,50,60,70,80,90]
N=0
Ns3=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size3:
    N=count_boxes(img3,size)
    Ns3.append(N)

    size_3 = np.array(size3)

size3=Ly/size_3

size3=1/size3

Ns3=np.array(Ns3)
df3=pd.DataFrame() #create table in console

df3['counnted boxes']=Ns3 #creates counted boxes column
df3['box size in px']=size_3 # creates box size column
df3['epsilon']=size3 #creates fractional box size column
df3['log (N)']=np.log10(Ns3)
df3['log (1/epsilon)']=np.log10(1/size3)


print(df3) #prints

trend3=np.polyfit(np.log10(1/size3), np.log10(Ns3), 1)
slope3=trend3[0]
D3=trend3[0]


plt.plot(np.log10(1/size3),np.log10(Ns3), 'o',color='violet')
plt.plot(np.log10(1/size3), np.polyval(trend3, np.log10(1/size3)),color='cyan')
plt.xlabel('log 1/$\epsilon$')
plt.ylabel('log N')
plt.title('Fern 3 log N VS log 1/$\epsilon$')
plt.show()
print("Dimension=", D3)
print("width=",Lx, "height=",Ly)

#fern4
image4_url = "https://cdn.phototourl.com/free/2026-06-14-fa0b88f1-b300-4220-a2d5-cd6ad27a7031.png"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image4_url, headers=headers) #retreives image via URL


# Open image
img4 = Image.open(BytesIO(response.content)).convert("L")


threshold = 150
img4_array = np.array(img4)
binary = img4_array < threshold

Lx=img4.size[0] #assign variable to image dimensions
Ly=img4.size[1]

# Show binary image
plt.figure(figsize=(6,6))
plt.imshow(binary, cmap="binary")
plt.title("Binary Image")
plt.axis("off")
plt.show()


#the following defines the black or white value of a (i,j)
thresh = 128  # 0 is black 255 is white, midway point between the two
for i in range (img4.size[1]):
	for j in range(img4.size[0]):
		if img4_array[i,j] > thresh:
			img4_array[i,j] = 255    # white
		else:
			img4_array[i,j] = 0   # black



def count_boxes(image, box_size):   #fuction for applying box counting to image for later determined box sizes
    N=0
    step=box_size
    for i in range(0, Lx, step):
       for j in range(0, Ly, step):
           if (img4_array[i:i+step,j:j+step] == 0).any(): #any white (i,j) in the range will add to box count
               N=N+1 #counts box if it is occupied

    return N

size4=[10,20,30,40,50,60,70,80,90]
N=0
Ns4=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size4:
    N=count_boxes(img4,size)
    Ns4.append(N)

    size_4 = np.array(size4)

size4=Ly/size_4

size4=1/size4

Ns4=np.array(Ns4)
df4=pd.DataFrame() #create table in console

df4['counnted boxes']=Ns4 #creates counted boxes column
df4['box size in px']=size_4 # creates box size column
df4['epsilon']=size4 #creates fractional box size column
df4['log (N)']=np.log10(Ns4)
df4['log (1/epsilon)']=np.log10(1/size4)


print(df4) #prints

trend4=np.polyfit(np.log10(1/size4), np.log10(Ns4), 1)
slope4=trend4[0]
D4=trend4[0]


plt.plot(np.log10(1/size4),np.log10(Ns4), 'o',color='violet')
plt.plot(np.log10(1/size4), np.polyval(trend4, np.log10(1/size4)),color='cyan')
plt.xlabel('log 1/$\epsilon$')
plt.ylabel('log N')
plt.title('Fern 4 log N VS log 1/$\epsilon$')
plt.show()
print("Dimension=", D4)
print("width=",Lx, "height=",Ly)

Ns5=((Ns1+Ns2+Ns3+Ns4)/4)
size5=((size1+size2+size3+size4)/4)

df5=pd.DataFrame() #create table in console

df5['avg boxes']=Ns5 #creates counted boxes column
df5['box size in px']=size_1 # creates box size column
df5[' avg epsilon']=size5 #creates column with fractional box size
df5['log (N)']= np.log10(Ns5)
df5['log (1/epsilon)']= np.log10(1/size5)

print(df5)

trend5=np.polyfit(np.log10(1/size5), np.log10(Ns5), 1)
slope5=trend5[0]
D5=trend5[0]



plt.plot(np.log10(1/size5),np.log10(Ns5), 'o',color='violet')
plt.plot(np.log10(1/size5), np.polyval(trend5, np.log10(1/size5)),color='cyan')
plt.xlabel('log 1/$\epsilon$')
plt.ylabel('log N')
plt.title('Fern avg log N VS log 1/$\epsilon$')
plt.show()
print("Dimension=", D5)
