from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

def generate_vgg16():
    # 搭建VGG16网络结构
    # ;return:VGG16网络结构
    input_shape  = (224,224,3)
    model = Sequential([
        Conv2D(64,(3,3),input_shape = input_shape,padding = 'same',activation = 'relu'),
        #64指滤波器filter数量,3-64,3指的是滤波器的长和宽都是3,第一层Conv需要指定输入图像的大小input_shape,padding:输入和输出之间长和宽的关系，激活函数 relu
        Conv2D(64, (3, 3),padding = 'same',  activation='relu'),
        MaxPooling2D(pool_size = (2,2), strides = (2,2)),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),#maxpool层加上全连接层FC必须在中间加上Flatten层
        Flatten(),
        Dense(4096,activation = 'relu'),
        Dense(4096,activation = 'relu'),
        Dense(1000,activation = 'softmax')
    ])#线性的网络结构,[]里是列表，用，分隔列表之间的元素
    return model

if __name__ == '__main__':#用于检测此脚本代码的运行情况，而在其他脚本调用此脚本时，该语句后的脚本将不会有运行
    model = generate_vgg16()
    model.summary()#将模型的综述打印出来

