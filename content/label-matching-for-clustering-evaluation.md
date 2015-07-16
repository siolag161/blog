Title: Label matching for clustering evaluation
Date: 11:20 Fri 10 Jul 2015
Tags: dev, code, python, clustering
Category: dev
Author: pdt
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
it would yield a value of `0.0`!! but in reality it perfectly agrees on how to group objects in categories. So
we got it totally wrong.

# Label matching
The naive way is to consider all the label permutations possible for
**CT** and compares it with **GT** and pick the one that minimizes the error.
Look at the example above. In the `(2)` clustering, if we change the label `1`
to `0` while fixing the rest labeling, we can see that we now have a
better result, in term of similarity to `(1)`. It would not suffice however, under
<!-- our conditions (the 2 label sets must match) we have to also assign `0` to `1` -->.
if we continue and assign `0` to `1` we can get even a better labeling.

<!-- But by how much did we improve? -->

<!-- Let's say we have 2 clustering `C1` and `C2`, -->
<!-- Indeed, one way to measure the distance between 2 clusterings is to count the  -->

<!-- We first define a cost function `f(c1, c2)` -->
In reality we can do better than the brute force approach. Our problem is actually
equivalent to the [assigment problem](https://en.wikipedia.org/wiki/Assignment_problem#Algorithms_and_generalizations)
in which we assign labels to labels. We need to compute the cost matrix, however.
This is the complement of the gain matrix whose element `(i,j)` is the number of
items that is classified as `i`in the first labeling and as `j` in the second one.

# Demonstration using [Hungarian solver](https://en.wikipedia.org/wiki/Hungarian_algorithm)
Here is a gist for matching label of a clustering obtained by `K-means` to the
ground truth, on the famous `Iris` dataset using the Hungarian algorithm,
also called Munkres.

We need the `numpy`, `scipy` and the [Munkres package](https://github.com/bmc/munkres)

[[gist:siolag161:dc6e42b64e1bde1f263b]]
