
ResNet:

面对的问题：误差反传的过程中，梯度通常变得越来越小，从而权重的更新量也变小。这个导致远离损失函数的层训练缓慢，随着层数的增加这个现象更加明显。

解决方法：增加跨层的连接。
