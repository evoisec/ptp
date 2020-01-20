# ptp
Data Science Focused, Hadoop Performance Testing & Measurement Suite - Data Science Workload Emulation, while remaining Close to the Metal - Python Based

Measures the peromance of all key Data Science / Machine Learning Algorithms / Models in a controlled and systematic way

Folder contents:

Data - contains sample datasets, specifically generated for Data Science Wrokloads 

DataGenerators - contains Syntehtic Data Generators implementing formal Mathematical Models emulating data containing Linear and Classification/CLustering Data Relationships/Patterns. This in turm makes the performance testing of Data Science Workloads realistic

Supported Data Science / Machine Learning Models/Algorithms:

Naive Bayes, Decision Trees, Linear Regression, Logistic Regression, Random Forest, Random Forest Classification, Gaussian Mixture Models, K-Means Clustering, Support Vector Machines

Enables the generation of Actionable (Measurement) Information supporting Informed Capacity Planning as well as Predictive Models for Performance Scaling and Cluster Sizing  

There is a lack of modern, business level tools for workload performance testing on Hadoop. Carried on by inertia, the majority of the IT industry is still using archaic, outadted "benchmarks" the majority of which are writtent in Map Reduce (not used almost at all in real projects) and implementing "toy" algorithms / data processing like e.g. "sorting" (as in "TerraSort")

The purpose of this suite is to fill the gap by augmenting (ie provides some innovations) and complementing more modern performance measurement suites (however not maintained on a regular basis / not up to date) such as:

https://github.com/Intel-bigdata/HiBench

https://github.com/palantir/spark-tpcds-benchmark
