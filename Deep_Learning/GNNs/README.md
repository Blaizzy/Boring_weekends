Before we begin I want to give credits and congrats to the authors of:
 - [GNNs in 2020 by Siraj Raval(the first video I watched after you come back and I have to hell of a come back brother!!!)](https://www.youtube.com/watch?v=bA261BF0bdk)
 - [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/pdf/1901.00596.pdf)(A really great paper, please check it out)
 - [DGL](https://docs.dgl.ai/tutorials/basics/1_first.html)(Great library, with great examples and docs. Great lib to take a look under-the-hood of GNNs)
 - [Pytorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html#id2)(Great libray, great examples and very simplified. Which makes it great for beginners). <br>
 
The people behind these projects did a fenomenal work.<br>
Special thanks to **Shirui Pan** one of the authors of the paper (A comprehensive Survey...) for reading my article and let me know. And to **Siraj Raval** for making the video, the video was the beginning of my curiosity and interest in GNN, also the first video I watched after he come back and I have to say that was a hell of a come back brother!!!)
 
# Graph Neural Networks(GNNs)
![alt text](https://hackernoon.com/drafts/pmhp31xm.png)

Recently, many studies on extending deep learning approaches for graph data have emerged, which gave birth to GNNs. GNNs have similar properties as its DL counterparts, capable of doing regression, classification, generating data for empty nodes, edges and so much more that we are yet to find out. The field is still at its beginning stages, who knows what we could do in a few years and a couple of thousand papers from now...

### **NOTE**: The [notebook](https://colab.research.google.com/drive/16T8JY_XG949m-dLSm-AMJvlXwN-VdjUK#scrollTo=aHclveU5wEZ5) in this repo was developed taking into account you read my article [Can Graph Neural Networks Solve Real-World Problems ](https://hackernoon.com/can-graph-neural-networks-solve-real-world-problems-7hd636dn) or have some previous domain knowledge. If you don't know about GNNs please take a minute and read my article, it will help you get a better understanding.

![alt text](https://media.giphy.com/media/WoWm8YzFQJg5i/giphy.gif)

In this nodebook we are going to take 2 GNNs libraries built atop of Pytorch:
 - DGL
 - Pytorch Geometric(Under Development...)
 
And we are going to look at too task:
 - Node classification
 - Graph Classification
 
# Node classification(Cluster formation)
Here we will binary node classification to predict whether a node is going to be in the cluster 1 or cluster 2 represented by node 0 and 33 which.
A typical example of friend recommendation system, just like facebook does to you. 

Credits for the dataset and example to DGL(Deep Graph Library) library [website](https://docs.dgl.ai/tutorials/basics/1_first.html).

![alt text](http://snap.stanford.edu/gnnexplainer/files/explainer-introduction.jpg)
*Image credits to: http://snap.stanford.edu/gnnexplainer/*


# Graph Classifiction

We will work on Mini Graph Classification Dataset that has 8 classes of different graphs. 
![alt text](https://s3.us-east-2.amazonaws.com/dgl.ai/tutorial/batch/dataset_overview.png)
*Image credits: DGL Docs - > https://https://docs.dgl.ai/tutorials/basics/1_first.html*

As I refered in the article: [Can Graph Neural Networks Solve Real-World Problems ](https://https://hackernoon.com/can-graph-neural-networks-solve-real-world-problems-7hd636dn)
this example here is just a teaser to what we could do with Graph Neural Networks(GNNs).
We could easily train a graph classifier on a dataset of drugs vs protein to a relatevily good accuracy that can predict whether a molecular structure is a drug or not. 
I strongly believe this will catapult drug discovery to a whole new level since machines can hidden patterns within large amounts of data that us humans can't or simply would take us long to do.

**I'm working on a application of this technique on a real-world case scenario, it took me long and it was hard to find but I finally found a website with graph datasets related to health. Stay tunned for that example.**

Credits of this tutorial to DGL [website](https://https://docs.dgl.ai/tutorials/basics/1_first.html).
