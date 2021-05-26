#form os import listdir
model = load_vgg16_model()
#去除模型最后一层
model.layers.pop
#Model是一个构造函数，model.input是去掉最后一层网络的网络输入（不变），outputs原网络去掉最后一层的网络结构之后再取最后一层作为输出。此时我们就有一个新的模型。
model =Model(inputs = model.inputs, outputs = model.layers[-1].output)
#构造一个特征的字典
features = dict()
#对于给定文件夹调用python自带的listdir方法，去文件夹中寻找所有的文件，返回所有的文件名，然后利用for循环遍历所有的文件名
for fn in listdir(directory):
    fn = directory + '/' + fn #fn只是文件名，需要将路径directory加在前面作为下一个函数的输入
    #arr返回的是一个三维的数组分别代表的是长宽已经通道数，因为是彩色的图片所以通道数为3
    arr = load_img_as_np_array(fn, target_size  = (224,224))#vggs16输入的图像大小为224，224，所以我们在读入图像的时候需要进行设置
    # 改变数组的形态，增加一个维度（批处理输入的维度），神经网络需要输入四个维度，在原维度前增加一个维度，用来指代训练时批处理的维度，
    arr = arr.reshape ((1,arr.shape[0],arr.shape[1],arr.shape[2]))
    #预处理图像作为VGG模型的输入
    arr = preprocess_input(arr)
    #计算特征
    feature = model.predict(arr,verbose = 0)

    id = fn 去掉文件后缀，同时去掉文件路径
    features[id] = feature

