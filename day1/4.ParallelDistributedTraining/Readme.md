# Day 1 Distributed deep learning training using TensorFlow and Keras with HorovodRunner
---

The day 1 platform is Azure Databricks.

Topics covered
---
Distributed deep learning training using TensorFlow and Keras with HorovodRunner for MNIST
This lab demonstrates how to train a simple model for MNIST dataset using tensorFlow.keras api. We will first show how to do so on a single node and then adapt the code to distribute the training on Databricks with HorovodRunner.

This guide consists of the following sections:
* Set up checkpoint location
* Run training on single node
* Migrate to HorovodRunner


Instruction notes
---
The notebook runs on CPU or GPU-enabled Apache Spark clusters.
To run the notebook, create a cluster with
* Two workers
* Databricks Runtime 5.4 ML or above
