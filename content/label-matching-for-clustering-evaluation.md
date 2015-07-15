Title: Label matching for clustering evaluation
Date: 11:20 Fri 10 Jul 2015
Tags: dev, code, python, clustering
Category: dev
Author: pdt
Status: draft
Summary: Task assignment in clustering evaluation

Let's say we perform a cluster analysis on the dataset using a fancy algorithm
and we would like to know whether it performs well. If we're really lucky and
have at disposal the ground truth (GT), we can check if the result we obtained (CT) with
the clustering algorithm are `similar` to the said ground truth. What this means
is that **GT** and **CT** should agree most of the time (relatively speaking) whether to
group two objects in a same group or in two seperate ones. In other words, they should
have a high degree of agreement.

There're several approaches to quantify the degree of agreement. Here since we know
the ground truth, we could use [external measures](https://en.wikipedia.org/wiki/Cluster_analysis#External_evaluation).
Among these, there's this particular method based on `confusion matrix` which is very widely used in classification,
to show how much **CT** is different from **GT**.

# Confustion matrix
How to construct a such confusion matrix from **CT** and **GT**? One common way, from classification, is to
first represent a clustering as an array, mapping each object to the cluster it belongs to, like so:

```python
|0|0|0|1|2|0| (1)
|0|0|1|1|2|2| (2)
```
here we have 2 clusterings of 3 clusters on 6 objects. So we have 2 arrays of the same length and
the same cardinality `T`.

The confusion matrix has then a dimension of `TxT` where each `(i,j)` is
the number that **GT** classifies as `i` while **CT** classifies as `j`.

# Problem of label meaning
The deal with this approach is that it doesn't work as properly in cluster analysis as in classification because
in classification each class has an underlying meaning, such as 'dog' and 'cat', for example; wheareas in clustering
if we any permutation of the classes would do.

For example, if we compute the accuracy for these two clusterings:

```python
|0|0|0|1|1|1| (1)
|1|1|1|0|0|0| (2)
```
it would yield a value of `0.0`!! but in fact it perfectly agrees on how to group objects in categories.

# Label matching
One simple way to solve this is to try to match the labels of the obtained result with the ground truth, so
we can use the above mentioned measures. The naive way is to consider all the label permutations possible for
**CT** and compares it with **GT** and pick the one that maximizes the said measure. We could, of course,
do better by using for example some [assigment tasking algorithm](https://en.wikipedia.org/wiki/Assignment_problem#Algorithms_and_generalizations),
[Hungarian](https://en.wikipedia.org/wiki/Hungarian_algorithm) is one of them.

# Hungarian (or Munkres) for clustering evaluation in Python
For illustrating, I created a simple program in Python performing 



[[gist:kfr2:5580453]]
