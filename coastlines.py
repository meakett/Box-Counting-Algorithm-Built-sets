mport pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


#Norway
image1_url = "https://cdn.phototourl.com/free/2026-06-03-7b0549d9-b917-4b8a-bb1e-5400dec51392.png"



headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image1_url, headers=headers) #retreives image via URL


# Open image
img1 = Image.open(BytesIO(response.content)).convert("L")

#img1= img1.resize((1000, 1000))


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
size1=[10,30,50,70,90,110,130]

N=0
Ns1=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size1:
    N=count_boxes(img1,size)
    Ns1.append(N)

    size_1 = np.array(size1)

size1=Ly/size_1
size1=1/size1

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
plt.title('Norway log N VS log 1/$\epsilon$')
print("Dimension=", D1)
print('width=', Lx ,'height=',Ly)


#Great Brit

image2_url = "https://cdn.phototourl.com/free/2026-06-03-305945d3-2561-4f9a-a868-3372f5d81350.png"



headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(image2_url, headers=headers) #retreives image via URL


# Open image
img2 = Image.open(BytesIO(response.content)).convert("L")
img2= img2.resize((800, 800))


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

size2=[10,20,30,40,50,60,70]
N=0
Ns2=[]# empty set for N values for each size

#apply count_boxes function to all size values
for size in size2:
    N=count_boxes(img2,size)
    Ns2.append(N)

    size_2 = np.array(size2)

size2=Ly/size_2

size2=1/size2

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
plt.title('Great Britain log N VS log 1/$\epsilon$')
print("Dimension=", D2)
print("width=",Lx, "height=",Ly)

