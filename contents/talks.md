---
title: Talks details
author: sfermigier
template: text.html
---

<style>
blockquote p {
    font-style: italic;
    color: #555;
}
h3, h4 {
    margin-top: 30px;
}
</style>

# Talk details

[The detailed schedule](/static/pdf/Schedule-PyParis-2018.pdf) is available as a PDF file.

## At a glance


### Theme: Core Python

- How to use AsyncIO to make the most of a CPU Bound and IO Bound software with Python 3.7 (Rémy Hubscher, ChefClub)
- Porting application from Python 2.x to 3.x (Philippe BOULANGER, INVIVOO)
- Unexpected Dataclasses (Pierre Alexandre SCHEMBRI, NETSACH)

### Theme: Data Science

- (Deep) Machine Learned Model Deployment with ONNX (Xavier Dupré, Microsoft)
- A Short History of Array-based Computing in Python (Wolf Vollprecht, QuantStack)
- Data Science for Industry 4.0 (Alessandro Giassi, Saint-Gobain Recherche Paris)
- Exploring image processing pipelines with scikit-image, joblib, ipywidgets and dash (Emmanuelle Gouillart, Joint Unit CNRS / Saint-Gobain)
- Geospatial data processing for image automatic analysis (Raphaël Delhome, Oslandia)
- Let the AI Do the Talk: Adventures with Natural Language Generation (Marco Bonzanini, Bonzanini Consulting Ltd)
- Machine Learning with Scikit-Learn: quick clusterization of a very large malware dataset (Robert ERRA, EPITA)
- Modern Pandas - Writing effective, readable data pipeline (Hervé MIGNOT, Equancy)
- Pyodide: scientific Python compiled in WebAssembly, and application (Roman Yurchak,  )
- Scikit-learn: news on making even better machine learning (Gael Varoquaux, Inria &amp; Tom Dupré de la Tour, Telecom Paristech)
- Segmentation of 3-D materials science images : from raw data to physical measurements  (Chloe Brillatz, CNRS/St Gobain Research Paris)
- Using Deep Learning to rank and tag millions of hotel images (Christopher Lennan, idealo.de &amp; Tanuj Jain, Idealo)
- Vaex: Out of Core Dataframes for Python (Maarten Breddels, Independant / Maarten Breddels)
- Beat a Google Ads Bidder using ML (Arnaud Fouchet, Dolead)
- Deep Learning with PyTorch for more Fun and Profit (Part 2.5) (Alexander Hendorf, KÖNIGSWEG)
- GeoAlchemy: using SQLAlchemy with Spatial databases (Éric Lemoine, Oslandia)
- Robosat: an Open Source and efficient Semantic Segmentation Toolbox for Aerial Imagery (Olivier Courtin, DataPink)

### Theme: Tools

- Interactive widgets in the Jupyter Notebook (Martin Renou, QuantStack)
- Jupytext: Edit Jupyter notebooks represented as Python scripts (Marc Wouts, Capital Fund Management)
- Vim Your Python, Python Your Vim (Miroslav Šedivý, UBIMET GmbH)

### Theme: Web & Cloud

- A better way to use modern Javascript/Node.js with Django (Romain Dorgueil, Makersquad)
- Anyblok WMS Base  (Georges Racinet, Anybox SAS)
- Big forms with JSON schemas and transcrypt (Philippe ENTZMANN, Aon France)
- Crossing the native code frontier (Serge sans Paille, Namek)
- DSL in Pyrser (Lionel Auroux, LSE EPITA)
- GraphQL in Python and Django (Patrick Arminio, Verve)
- Inside Rapid.Space: Open Hardware and Free Software = Ultra Low Cost High Performance Cloud (Jean-Paul Smets, Nexedi)
- Invitation to a New Kind of Database (Sheer El Showk, Lore Ai)
- Python tooling for continuous deployment (Arthur Lutz, Logilab)
- Serverless Python (Michael Bright, @mjbright Consulting)
- The SIMPLE Framework, simplifying complex container clusters (Mayank Sharma, CERN)
- Using type annotation in Python (Philippe Fremy, IDEMIA)
- Version control in 2018: present and future (Pierre-Yves David, Octobus.net)
- What is asyncio and when to use it, an example with WatchGhost (Pierre Alexandre vuillard, hashbang.coop)

### Theme: Education


NOTE: Les présentations du track 'Education' ont lieu **en français**.

- Girls Can Code! summer camps: an experience of teaching computer science to young girls. (Garance Gourdel, ENS Paris Saclay &amp; Paul Guenezan, EPITA / Association Prologin)
- How we used Python to introduce teenagers to the fun of programming (Anne-Marie Tousch, Criteo)
- Python @ Sorbonne Université (Frederic Peschanski, Sorbonne Université - LIP6)

### Theme: Tutorials

- Dataviz with matplotlib and seaborn (Francis Wolinski, Yotta Conseil)
- GeoSpatial Data Analysis using Python (Fereshteh ASGARI, Research Engineer)
- Machine learning using scikit-learn (Guillaume Lemaitre, INRIA)
- Understanding and diagnosing your machine-learning models (Gael Varoquaux, Inria)
- Parallel Data Analysis with Dask (Loïc Estève, Inria)
- Python Micro-services with Kubernetes (Michael Bright, @mjbright Consulting)

----

## Talk / Tutorials details

### Theme: Core Python


#### How to use AsyncIO to make the most of a CPU Bound and IO Bound software with Python 3.7 (Rémy Hubscher, ChefClub)

AsyncIO is a revolution. Let's see why and how the event loop works with Python.

What are a CPU Bound and IO Bound software and how to take advantage of the producer/consumer model brought by asyncio with Python 3.7.

#### Porting application from Python 2.x to 3.x (Philippe BOULANGER, INVIVOO)

We are living the last months of Python 2... Lots of companies are always using the version 2 of Python and have to migrate to Python 3 in the next months. A migration is a long journey, most of the time it's boring with lots of production risks/issues. Purpose of my conference is to give the keys to reach the objective in avoiding traps.

#### Unexpected Dataclasses (Pierre Alexandre SCHEMBRI, NETSACH)

Why do we need "mutable namedtuples with defaults" a.k.a. dataclasses, one of the latest additions to Python (3.7) ?

One's may wonder on the intended use and the expected benefits for developers using this library. 

In this talk, we will see a bit further about design principles vs raw features and how dataclasses are a great tool to promote best practices.


### Theme: Data Science


#### (Deep) Machine Learned Model Deployment with ONNX (Xavier Dupré, Microsoft)

Many machine learning frameworks are optimized to train models such as scikit-learn, pytorch, tensorflow, keras. However they do not offer a standard way to deploy the learned model into an environment where the performance is critical. ONNX is one open source answer to that particular issue as it provides a separate and efficient way to compute the predictions. Microsoft is an active contributor to the ONNX ecosystem initiated by Facebook and Microsoft last year. This talk introduces ONNX concepts and demonstrates an end to end scenario with DNN and traditional ML models instead.


#### A Short History of Array-based Computing in Python (Wolf Vollprecht, QuantStack)

Solid foundations for array-based computing have been the key to the success of Python as the language of Data Science. NumPy, the de facto standard, has been the unconstested foundation of the ecosystem since its initial release in 2006.
In this talk we will walk through a number of interesting packages in the Python Data Science / Array Computing ecosystem, analyze and benchmark them, and see how all the pieces fit together to make Data Science applications faster and more efficient.

With the recent rise of Machine Learning and subsequently even larger problem sizes, array computing has gotten a new push. More efficient algorithms for more specialized objectives have been implemented in various packages: Dask, TensorFlow and PyTorch implement graph-based abstractions to dispatch computations to an abstract engine, CuPy implements a CUDA backend to compute NumPy-style operations on the GPU, pysparse implements sparse array containers and numexpr defers evaluating expressions in order to fuse loops for faster performance. Labeled arrays are implemented in the xarray and Pandas packages. Moreover, there are multiple JIT engines to compile array computations to high-performance machine code, notably Numba and Pythran.

Most recently, Matt Rocklin has started work on a NumPy Enhancement Proposal, that adds an abstract interface to array-like objects. This array interface will make it possible to treat specialized arrays (that implement the NumPy protocol) interchangeably – a huge milestone for the community as this enables generic programming and facilitates easy tuning at later stages.

Travis Oliphant, who started NumPy, is now gathering a team around the xnd project (an offspring of the libdynd efforts). xnd is a low-level library for array computations in Python with bindings to the C language. Similar efforts are made for C++ in the xtensor and xtensor-python project. 

We will look at ways to leverage these implementations in lower-level languages to generate application-specific computation kernels and seamlessly bind them to the Python language.


#### Data Science for Industry 4.0 (Alessandro Giassi, Saint-Gobain Recherche Paris)

The 4th industrial revolution relies on new sensors, connectivity and data science, but also on preexistent industrial structures. 
The journey of a Data Scientist to bring value to an industrial project is then a peculiar mix of new algorithms and traditional process engineer knowhow.
The presentation shows some examples of Machine Learning applications for Industry 4.0, addressing both technical and organizational aspects.


#### Exploring image processing pipelines with scikit-image, joblib, ipywidgets and dash (Emmanuelle Gouillart, Joint Unit CNRS / Saint-Gobain)

For image processing tasks such as segmentation of objects of interest, finding a satisfactory processing method often involves testing different functions or combinations of several functions, or varying parameters of algorithms. In this talk, I will discuss several tools which can accelerate this process, both in terms of developer and CPU time. 
I will start by describing how the documentation of scikit-image can help discovering functions suited for different usecases, thanks to a graphical gallery of examples. Functions are also exposed by scikit-image in order to test several methods at once on the same image, for example for image thresholding. I will then explain how to explore interactively the effect of function parameters thanks to ipywidgets, or dash for more complex applications. Finally, I will explain how caching results with joblib.Memory can save time when varying parameters of the processing pipeline.

#### Geospatial data processing for image automatic analysis (Raphaël Delhome, Oslandia)

Since a few years, the machine learning techniques have been more and more popular for geospatial data analysis, to the point that one talks about "geospatial artificial intelligence". More specifically, deep learning algorithms appear as a major breakthrough in the Geographic Information System (GIS) scope. As a seminal example, neural networks are able to do semantic segmentation on aerial images, so as to recover buildings, roads, and so on.

Oslandia is an opensource company studying and exploiting geospatial data, with an extensive R&D activity about geospatial data science. This presentation will detail some of our Python routines in terms of geospatial data handling.

As a guiding principle, our Python data ETL processes will be described, from raw data to machine learning results. In this global scheme, we consider Luigi as a tool of first importance: it highlights our workflow dependency graph, and makes the process easier to analyze. Whether it be from OpenStreetMap (.pbf), from open data portals (.xml, .json, .geojson) or from georeferenced image datasets (.tiff, .geotiff), we get open data in a wide range of formats. This data is stored in databases, or as files, then exploited using libraries like GDAL, shapely, geopandas or Mapnik. As the main step of the pipeline, some new data is produced through machine learning techniques (e.g. convolutional neural networks for image semantic segmentation with Keras). In the case of geospatial data, a postprocessing step is often necessary in order to display outputs in web applications or GIS tools.

A concrete illustration of our results will be provided through a light Flask application designed for demonstration purpose. This application comes as a tangible data pipeline output by providing understandable visualizations.

#### Let the AI Do the Talk: Adventures with Natural Language Generation (Marco Bonzanini, Bonzanini Consulting Ltd)

Recent advances in Artificial Intelligence have shown how computers can compete with humans in a variety of mundane tasks, but what happens when creativity is required?

This talk introduces the concept of Natural Language Generation, the task of automatically generating text, for examples articles on a particular topic, poems that follow a particular style, or speech transcripts that express some attitude. Specifically, we'll discuss the case for Recurrent Neural Networks, a family of algorithms that can be trained on sequential data, and how they improve on traditional language models.

The talk is for beginners, we'll focus more on the intuitions behind the algorithms and their practical implications, and less on the mathematical details. Practical examples with Python will showcase Keras, a library to quickly prototype deep learning architectures.

Brief Agenda:
- NLG: what and why
- Traditional Language Modelling
- Core Concepts of Neural Networks 
- Recurrent Neural Networks for Natural Language (Processing|Generation)

#### Machine Learning with Scikit-Learn: quick clusterization of a very large malware dataset (Robert ERRA, EPITA)

To cluster a set of (numerical) objects is to group into meaningful categories these
objects. We want objects in the same group to be closer (or more similar) to each other
than to those in other groups. Such groups of similar objects are called clusters. When
data are labeled, this problem is called supervised clustering. It is a difficult problem but
easier that the unsupervised clustering problem we have when data are not labeled.

Malware are now developed at an industrial scale and human analysts need automatic
tools to help them. We propose here to present the results of our experiments on this difficult problem: how to cluster 
quickly and efficiently a very large set of malware (using only static information). This is necessary: 
-(i) to understand our dataset
-(ii) to be able classify some new malware.

We propose:
- to present some results on our dataset of quite two million malware
- to present some (new) results we have found with the Ember (large) dataset 
- to talk about problems and future works that could be interesting to do (well: problems still to be solved)
- and to describre the Automeans algorithm, inspired by the Louvain algorithm that computes communities in a large graph, 
an algorithm we have developed to cluster a large dataset of vectors. 

All our experiments have been done with code written in Python and we have mainly used
Scikit-learn so we hope you will be able to do the work again with your own feature
vectors.

#### Modern Pandas - Writing effective, readable data pipeline (Hervé MIGNOT, Equancy)

Pandas API has evolved over the last versions to support an elegant, efficient and readable way to write data transformations, sometimes called Modern Pandas. This talk introduces this writing style, covers in detail how to code important data transformations, highlights its key benefits, evaluate performances and gives a handful of useful tricks in using the Modern Pandas style.

#### Pyodide: scientific Python compiled in WebAssembly, and application (Roman Yurchak,  )

The Pyodide project aims to compile the scientific Python stack to WebAssembly, so that it can be run directly in the browser. It currently supports data science libraries such as NumPy, Pandas, matplotlib (and more planned in the future). In this talk we will outline the current  capabilities, existing challenges, and possible future development directions.


Pyodide is closely related to the Iodide project, which implements a notebook environment (including but not limited to Pyodide) that allows performing calculations in the client-only mode (without sending requests to a server).

In the second part of this talk, wider implications of notebooks that do not require a centralized server in business and educational use-case will be discussed. We will also present an open-source approach for packaging Iodide notebooks as part of the OfficeJS suite,  developed at Nexedi.   With this approach, notebooks can be stored in Dropbox, WebDAV, ERP5 or local  storage, allowing both online and offline use. 

#### Scikit-learn: news on making even better machine learning (Gael Varoquaux, Inria &amp; Tom Dupré de la Tour, Telecom Paristech)

We will give an update on scikit-learn development. We will start with a perspective on the growth of the community, and how it led to creating a foundation to back this community. Then we will summarize the highlights of the 0.20 release. Finally, we will zoom in on the specific case of opening scikit-learn to use multiple NearestNeighbors backends to accelerate many algorithms. This raises challenge API issues, but a solution is possible!


#### Segmentation of 3-D materials science images : from raw data to physical measurements  (Chloe Brillatz, CNRS/St Gobain Research Paris)

In image analysis, segmentation means data discrimination or pixel labeling, in other words we want the computer to be able to differentiate, for instance, between dark colour areas and light areas. Only once it is done we are able to compute quantitative measurements about objects of interest and draw information from them. Hence, it is a key step for producing reliable statistics.

At the Grenoble synchrotron we followed the evolution at high temperature of composite glass samples, using a leading edge 3-D imaging technique called nanotomography. Characterising the morphological properties of the different phases is important for industrial applications, but this requires first an accurate segmentation of the phases. Totalling 1 TB (1000GB) of process-able data, manual segmentation is not an option.

The open-source Python Scikit-Image package is a high-quality and peer-reviewed useful tool kit to support us with this task. Combined to filtering, scikit-image segmentation algorithms as global thresholding and local thresholding were tested against each other. From there we used surface meshing, voxels counting, object counting with labeling, mayavi 3D visualisation as well as the mayavi 4-D visualizer. Here we show the process that lead us from raw data to exploitable statistics.

#### Using Deep Learning to rank and tag millions of hotel images (Christopher Lennan, idealo.de &amp; Tanuj Jain, Idealo)

At idealo.de (a leading price comparison website in Europe), we have a dedicated service to provide hotel price comparisons (hotel.idealo.de). For each hotel, we receive dozens of images and face the challenge of composing image galleries that are attractive and at the same time help our users to make informed decisions. Given that we have millions of hotel offers, we end up with more than 100 million images for which we need both an attractiveness assessment and a tag (e.g. a “bathroom” or “bedroom” tag).

We addressed the need to automatically assess image quality by implementing an aesthetic and technical image quality classifier based on Google’s research paper “NIMA: Neural Image Assessment”. NIMA consists of two Convolutional Neural Networks (CNN) that aim to predict the aesthetic and technical quality of images, respectively. Additionally, another CNN was trained to assign hotel area tags, like bathroom, bedroom, pool, etc. to each image. The models were trained via transfer learning, where ImageNet pre-trained CNNs were fine-tuned for each classification task. In this talk, we will present the insights that we’ve gained throughout the process and discuss the challenges we faced while putting such a system in production.

#### Vaex: Out of Core Dataframes for Python (Maarten Breddels, Independant / Maarten Breddels)

With the enormous growth and availability of datasets, many data scientists have difficulties processing and analyzing such voluminous data since it does not fit into RAM of a standard laptop or desktop computer.  

To this end, we created Vaex, a Python library that enables the exploratory analysis and visualization of datasets that are too large to fit in memory, largely independent of the amount of RAM available even on a laptop. Vaex combines efficient file reading, memory mapping, and simple and efficient algorithms with a DataFrame API like Pandas, which makes for a nearly non-existent learning curve.

Using an expression system which understands most numpy functions, all computations can be evaluated lazily and in chunks, effectively side-stepping any potential memory issues. Computations can also be executed remotely or distributed on a cluster. Memory copies are avoided even for subsets, making tasks such as data cleansing, selections, and feature engineering possible even for datasets that are larger than available RAM. Vaex also employs fast and reliable algorithms for computing statistics on N-dimensional grids, which is particularly useful for extracting key information from large datasets. The binned statistics form the basis of the visualization options, generating 1D (histograms), 2D (density maps), 3D (volume rendering) plots out of ~1 billion rows per second. Coupling this blazing fast plot generation together with the familiar DataFrame API allows for interactive visualization and exploration of any tabular dataset, regardless of its size.

In this talk, we will explain some of the technical details that lead to the performance that Vaex has. We will also demonstrate live in a Jupyter notebook many tasks that are typical to data science problems, such as data cleansing, exploration, feature engineering, and its machine learning capabilities. 

#### Beat a Google Ads Bidder using ML (Arnaud Fouchet, Dolead)

Real world problem: optimise volume with a CPA constraint (a Google Ads campaign) - using standard python ML libraries
- notions about paid marketing campaigns;
- translate business problem to ML;
- start with Gradient Boosted Decision Trees (a Kaggle classic);
- neural networks;
- transfer learning on neural networks;
- consensus;
- consensus optimisation;
- results

#### Deep Learning with PyTorch for more Fun and Profit (Part 2.5) (Alexander Hendorf, KÖNIGSWEG)

There are all these great articles and blog posts about Deep Learning describing all that awesome stuff. - Is it all that easy? Let's check! We'll look into: style transfer (making a picture look like painting), speech generation (like Siri or Alexa) and text generation (writing a story). In this talk I'll describe the whole journey: A fun ride from the idea to the very end including all the struggles, failures and successes.

#### GeoAlchemy: using SQLAlchemy with Spatial databases (Éric Lemoine, Oslandia)

GeoAlchemy provides "spatial" extensions to SQLAlchemy, the famous Python SQL toolkit and Object Relational Mapper.  GeoAlchemy makes it easy to use types, functions and operators of spatial databases, while leveraging the great flexibility and power of SQLAlchemy.  GeoAlchemy currently supports PostGIS and SpatiaLite, two major opensource spatial database systems. 

In this talk I will first explain what spatial databases are, and how they can be used for storing
and analyzing georeferenced data.  Then, I will provide an introduction to SQLAlchemy, attempting to demonstrate that it's much more than an ORM – ORMs being a bit controversial these days!  Finally I will show how to use GeoAlchemy to interact with spatial databases in Python.

Whether you're a developer or not, come to this talk to discover the world of spatial data and
spatial databases, and how to efficiently manipulate that data in Python.


#### Robosat: an Open Source and efficient Semantic Segmentation Toolbox for Aerial Imagery (Olivier Courtin, DataPink)

Aerial Imagery Semantic Segmentation is definitely not a new topic, 
but it's not an obvious one, as since decades it still an open subject.

Deep Learning techniques came as a game changer, as it allows to efficiently extract patterns from several kind of dataset far more easily than before.

RoboSat in this context, provide a toolbox, with several tools who could be chained together, to build a whole aerial semantic segmentation process.

This presentations will focus on:
 - Deep Learning Semantic Segmentation, and aerial imagery specificities
 - Ilustrated SemSeg use cases with OpenData
 - Ways to improve SemSeg efficiency (Dedicaded Losses, GAN post treatment...) 
 - Ways to improve SemSeg performances (SemSeg light models, Fine Tuning...)
 - Current RoboSat implementation
 - OpenDataSets available

### Theme: Tools


#### Interactive widgets in the Jupyter Notebook (Martin Renou, QuantStack)

Jupyter's interactive widgets are an important part of the Jupyter Project ecosystem, they bring rich interaction between user and data. From interactive 2-D plots to volume rendering, data visualization has never been so easy and dynamic.
During this talk, I will explain how Jupyter widgets work, and give an overview of some widgets libraries: ipywidgets, bqplot, ipyleaflet, ipyvolume.

#### Jupytext: Edit Jupyter notebooks represented as Python scripts (Marc Wouts, Capital Fund Management)

You've always wanted to
- edit Jupyter notebooks as e.g. plain Python scripts in your favorite editor?
 - do version control of Jupyter notebooks with clear and meaningful diffs?
 - collaborate on Jupyter notebooks using standard (text oriented) merge tools?

Jupytext is a plugin for Jupyter Notebook that allows to represent notebooks as simple text files: Julia, Python, R scripts, Markdown and R Markdown documents. Edit these text representation, share them using Git, merge contributions, and reload the updated notebook in Jupyter. Come to the talk and learn how to use Jupytext to efficiently edit, version control, and collaborate on Jupyter notebooks.

#### Vim Your Python, Python Your Vim (Miroslav Šedivý, UBIMET GmbH)

Master your fundamental tools — keyboard and text editor — and use your muscle memory to concentrate on your task, no matter in which language and what type of text you’re working on.

What do you use to write source code, docs, configs, books or e-mails? Single brain, single pair of hands, single physical keyboard, but a different keyboard layout for each language and a different text editor for each purpose?

I'll show you how I am happily typing in several European languages (French included) on a single standard US keyboard layout and why you should get rid of AZERTY. I'll show you how I use a single editor on all my machines to produce all sorts of text, and why you too should master one real text editor, whether it is Emacs or Vim. And I'll show you how to use your Python skills to hack all texts far beyond imagination.

### Theme: Web & Cloud


#### A better way to use modern Javascript/Node.js with Django (Romain Dorgueil, Makersquad)

A practical presentation on how to keep up with the pace of Node.js web innovation, while building on the rock-solid foundation of python-based web software.

Transpilation from various languages (like ES6, JSX, SCSS, ...), use of vue.js or react (with amazing associated development tools), hot module replacement, maintenance of node.js dependencies amongst various projects ...

All those can be hard and time consuming to integrate with django, but it should not, and we'll demonstrate simple techniques that makes it so damn simple.

#### Anyblok WMS Base  (Georges Racinet, Anybox SAS)

In this talk, we'll present Anyblok / WMS, a new core library to develop stock and logistics management applications. It is written in Python 3, leveraging PostgreSQL, SQLAlchemy and AnyBlok.

    https://pypi.org/project/anyblok-wms-base/
    https://blog.racinet.fr/tag/logistique.html
    https://anyblok-wms-base.readthedocs.io/
    https://github.com/AnyBlok/anyblok_wms_base

Anyblok WMS is meant to provide a robust foundation for end application developers and maintainers. As a stock and logistics intermediate framework, the functional scope of its potential applications encompasses anything that involves tracking and handling physical objects: backend support for ecommerce as well as traditional shops, or fleet management.
 
In Anyblok Wms, try and be as flexible and generic as possible, relying on the modularity that is the trademark of Anyblok, and good development practices, especially a certain kind of minimalism.

The development of the first set of components has been launched in early 2018, and we hope the first professional application relying on it (a multi channel b2c system with assemblies) will enter production before 2019.

Among the goals of the presentation : bootstrap exchanging with the broader development community, gather feedback and use cases, and in the long run, meet potential contributors. 


#### Big forms with JSON schemas and transcrypt (Philippe ENTZMANN, Aon France)

When you have 400 fields in your form, you also get a
lot of business rules to code. The expresiveness of Python is hard
to beat. We manage to have our business rules set able to run both
on the servers and on the web broswers. The classic CPython interpreter
is used on the server side.
A python-javascript transpiler is used on the client side : Transcrypt.
Then we have a common context-free code base to code our business rules.

#### Crossing the native code frontier (Serge sans Paille, Namek)

 Python shines as a glue language, wrapping up native libraries. In many subtle ways, and even when it is costless to cross, the interpreted <> native frontier has an impact on performance and/or potential optimisation. The Pythran compiler proposes a naive yet efficient approach to the problem, targeted at scientific kernels: move the frontier! Make the computation-intensive part of your code native while still writing it in **plain** Python. The talks presents the core idea of the Pythran compiler and compares its philosophy to the (utterly valid) paths taken by Cython's, PyPy's or Numba's. 


The talks presents the core idea of the Pythran compiler and compares its philosophy to the (uterly valid) paths taken by Cython's, PyPy's or Numba's.

#### DSL in Pyrser (Lionel Auroux, LSE EPITA)

This is a presentation of a toolbox for writing parsers (using the PEG algorithm and semantics), to handle AST, to write typing to help you creating DSL (domain specific language). This could be seen as a python alternative of Stratego.

https://pythonhosted.org/pyrser/

What advantages of PEG other LR? What is pyrser doing that others tools don't do?


#### GraphQL in Python and Django (Patrick Arminio, Verve)

GraphQL has grown a lot overtime, but it seems to still be a new “thing” in the Python and Django World. This talk will be an introduction to GraphQL, explaining why it has been created and how you can use it in Python and Django.

Agenda:

- Short speaker introduction
- Small digression on how the “old” web used to be and how it has now evolved into the modern web
- Really quick explanation of REST (just to make sure everyone is familiar with it)
- What are some limitations of REST? What can we do about it?
- Introduction to GraphQL, what it is, how’s using it and when has it been created?
- GraphQL: query language syntax
- GraphQL: types and introspection
- GraphQL: operation, how to read data, update data and more
- How to use Graphql with Python and Django
- Let’s make a simple API
- How to create queries
- How to create mutations
- Things to consider (security caching and performance)
- Closing thoughts

#### Inside Rapid.Space: Open Hardware and Free Software = Ultra Low Cost High Performance Cloud (Jean-Paul Smets, Nexedi)

This talk explains how it is possible for Rapid.Space to provide Big Data clusters for 3 to 10 times cheaper than any public cloud on the market thanks to exclusive use of Open Hardware and Free Software. This talk also explains how everyone could actually copy and do the same as Rapid.Space which source code, operation manual and business plan are entirely public. 

From server to router, from provisioning to billing, from CDN to routing, from virtualisation to firmware, Rapid.Space is entirely based on open hardware and Free Software, most of which is written in python.

The core of Rapid.Space is based on SlapOS (slapos.nexedi.com), an operation and orchestration system written in python that turns a GNU/Linux distribution into a general purpose Edge Computing / Cloud Computing system. SlapOS, which was created about 10 years ago, actually pioneered the concept of Edge Computing which became popular in early 2018 for 5G networks. SlapOS relies on nano-containers, much smaller than LXC containers, and supports massive deployment of services on a distributed, bare-metal architecture that spans from the data-centre to edge nodes of a mobile radio network. It supports accounting, billing, disaster recovery, devops, PaaS, etc.

The most surprising part of SlapOS is that it is actually a very small software compared to other, less general, cloud solutions written in python. Its tutorial of about 400 pages can be completed in less than 2 days. A good python developer can become the operator of Cloud or Edge infrastructure. Simplicity of SlapOS comes from reuse of mature python software: buildout, supervisord and ERP5. Rather than reinventing what already exists and works, SlapOS relies on exiting community projects. This pays off: we found in our benchmarks that SlapOS is 2 to 7 times more stable than OpenStack, and about 200% faster.

The hardware of Rapid.Space is based on recycled Open Compute Project servers that were previously used by some very large Web operator. Servers are refurbished with new SSDs. Linuxboot open source firmware is installed to replace previous proprietary AMI BIOS. Servers are then hosted in the same kind of data centre as other famous public clouds use. 

One of the challenges we faced was to provide good disk I/O performance with virtualisation, We solved this challenge by tweaking qemu and by allocating an entire attached disk to each VM. This way, we lose less performance than in other virtualised public clouds. Yet, we believe that bare metal containers are a must for any database application, something that SlapOS already supports. We provide detailed benchmarks on this topic.

The business model of Rapid.Space shows that the cost of a single big VM (256 GB RAM, 4 TB SSD, 20 core) is about 170 EUR per month (public price is 195 EUR). This is 3 to 10 times less than many offers on the market, especially those from famous public cloud providers. All companies that are currently migrating their in premise infrastructure to public clouds could actually slash costs by 10 by creating their own clone of Rapid.Space on premise and using Open Hardware.

This is actually much easier than one could think. A large big data operator in France already made this move, with our help. Hopefully, more and more companies will do the same after realising that there is a simple and stable Free Software solution to operate a Cloud, from provisioning to billing, from CDN to routing, from virtualisation to firmware.

References:

https://www.nexedi.com/NXD-Blog.High.Performance.VM.DB 
https://www.nexedi.com/press/NXD-Press.Release.Rapid.Space.Beta.Phase 
https://www.nexedi.com/NXD-Blog.Low.Cost.Cloud.Business.Model 

#### Invitation to a New Kind of Database (Sheer El Showk, Lore Ai)

The goal of this talk is to help launch an open-source project to develop a new kind of database in Python.

Most databases struggle with issues of consistency, scalability or durability and often trade one for the other because they lack an internal notion of "time".  In an elegant talk (https://youtu.be/Cym4TZwTCNU), Rich Hickey, revisited several ideas at the core of database design and arrived at a design that revolves fundamentally around immutability and versioning of data (aka time).  Integrating ideas from functional programming (immutable versioned data structures such as persistent trees) he was able to build a database (Datomic) that is at once:

- ACID
- Horizontally scalable
- Natively versioned (access an _indexed_ version of the data at any time-slice)
- Highly performant with most processing done in-process on the client

Unfortunately this database is not open source.

Our goal in this talk will be to explore how much of this we can (easily?) reproduce in an open source project (implemented in Python/Cython).  The talk will be very exploratory: we will outline challenges, possible solutions and available tools that might be useful but the goal is very much to get audience interaction and participation.

We hope that by the end we will have some feedback and collaborators!


#### Python tooling for continuous deployment (Arthur Lutz, Logilab)

How  we migrated the build and deploy processes to a continuous 
delivery  model, and the implications of such a change in terms of 
technology but  also team changes and the project management with the 
client. This talk will focus on the Python tooling that enabled to 
conduct such a change, but also on the human changes it requires.

* changes in infrastructure, in particular, the use of python software : 
  docker-compose and saltstack
* tools for collecting errors as soon as possible : sentry (django 
  based) and raven (its python library on the client-side)
* tools for continuous integration and review : jenkins with the python 
tool "jenkins-job-builder", and the python based version control 
"mercurial", the python plugins for interacting with "phabricator"
* tools for metrics and supervision: graphite-api (python rewrite of 
graphite which ships without django), and saltstack for collecting 
custom business-oriented metrics from python script
* integrating the projects with cloud infrastructure, using python-nova, 
python-openstack and salt-cloud (openstack and AWS)
* change management in the team of developers and the project management 
with the final users and project managers

#### Serverless Python (Michael Bright, @mjbright Consulting)

The Serverless Computing paradigm is taking the industry by storm.  In this talk we look at what is Serverless computing, what are the various cloud provider offerings and Open Source tools and frameworks available.

The talk will be supplemented with demos on AWS Lambda using the Chalice Python module and OpenFaaS demonstrating use of Python-based machine-learning examples and creation of a new Python function from the OpenFaaS provided Python3 template.

#### The SIMPLE Framework, simplifying complex container clusters (Mayank Sharma, CERN)

The Worldwide LHC Computing Grid a.k.a. the grid unites resources from over 169 sites spread across the world and the number is expected to grow in the coming years. These sites process and store data coming from the world's largest accelerator i.e The Large Hadron Collider housed at the border of France and Switzerland. However, setting up and configuring new sites to support WLCG workloads is still no straightforward task and often requires significant assistance from WLCG experts.  Given the rise of modern technologies for infrastructure provisioning management, we have developed a new open source framework which can be used to set up clusters of containerized site services easily, thereby simplifying the lives of site admins and WLCG experts alike. This new framework, known as SIMPLE Grid framework, however, is modular enough to be used beyond the WLCG in places where setting up of container clusters is required. In this talk, we describe this modular and extensible core system that abstracts low-level details through a YAML based site-wide configuration file which is used to configure all distributed components through a single command. To accommodate the diverse scenarios, the framework enables the users to cherry pick their background technologies and methodologies for orchestration (Puppet, Ansible, ...), clustering (Docker Swarm, Kubernetes, ...) and networking (dedicated networks, custom overlay networks or a combination of both). The talk will also focus on 2 python command line utilities for the framework,  a custom YAML compiler and configuration validation engine. 

#### Using type annotation in Python (Philippe Fremy, IDEMIA)

Since the release of Python 3.5 in 2015, an ecosystem 
has been growing around type annotation for Python. Major
companies such as Facebook or Dropbox are contributing tools
to help developers to "type" their Python code: they can
now benefit from static type analysis, an advantage no longer
reserved to statically typed languages.

This talk presents the benefits of type annotation
and then explore practically how to use the different tools
available today to detect errors and improve code quality.



#### Version control in 2018: present and future (Pierre-Yves David, Octobus.net)

The version control ecosystem has evolved a lot in the last decade, with the arrival of decentralized version control systems and platforms like Github. But, even with its tremendous success, Git is not the ultimate solution covering all the use-cases. Lots of people and companies prefer the previous generation of tools (like SVN), or proprietary tools (like Perforce™) or other tools of the same generation (like Mercurial).

In this Talk, we will study the constraint that shaped the current generation of tools. Then we will explore the new challenges that all current version control tool will have to face. We will show how alternatives to Git can foster innovation and explain why Mercurial seems a project more fitted for facing these challenge.

#### What is asyncio and when to use it, an example with WatchGhost (Pierre Alexandre vuillard, hashbang.coop)

Asyncio has been released recently (2014). It enables asynchronous programming in Python, which necessitates a new way of thinking for developers used to synchronous programming. In this talk, we will try to explain how asynchronous programming works, how to use it with Python, and a few usecases it can solve.

I will use WatchGhost (https://watchghost.readthedocs.io/en/latest/) as an illustration of asyncio use. WatchGhost is a simple and light monitoring tool written in Python using Tornado and asyncio libraries. It relies heavily on network communications and light configuration files to check network services. I will present how WatchGhost benefits from asynchronous programming capabilities given by Python.

### Theme: Education


NOTE: Les présentations du track 'Education' ont lieu **en français**.


#### Girls Can Code! summer camps: an experience of teaching computer science to young girls. (Garance Gourdel, ENS Paris Saclay &amp; Paul Guenezan, EPITA / Association Prologin)

For the fifth year in a row, the non-profit organization Prologin organized the “Girls can code!” summer camps to teach middle and high school girls basic computer science skills. The summer camp is meant to be a playful experience for the girls to enjoy discovering a field that is often hard to enter for them. It revolves around the learning of Python, chosen for its simplicity combined with the very large number of applications it can serve. After five years of experience, our pedagogical content has evolved a lot and we are thrilled to share our different approaches and how they turned out.

Overall we start the week by an introduction to Unix and the Linux environment they work on during the summer camp. Then we move on to a general introduction to Python, presenting the basic concepts and applying them immediately via small exercise. Later on, they start using more advanced structures such as lists which are going to be really useful during the projects. After that, at the middle of the week we present them other fields such as Network and Web development, on which they can spend  less or more time, just depending on their interest in computer science. We finish the week by several days where the girls are free to work on a project of their choice. This year they could work on micro controllers micro:bit, create a video game using the Pygame library, or work on Lego Mindstorm which can be programmed by instruction blocks. 

But this is just the format we chose for 2018, and we are still considering changing some parts of the format, such as removing the Unix introduction which isn’t very beginner friendly. Over the years, we also experimented other formats such as more theoretical summer camps oriented on solving algorithm problems, or an introduction to notions that are considered not very accessible such as IA for recommendation.

#### How we used Python to introduce teenagers to the fun of programming (Anne-Marie Tousch, Criteo)

Teenagers are known for being digital natives, but there is a gap between using new technologies and understanding how it has been built. Moreover, the computer science world is not yet sufficiently attractive amongst young women. The sadly low number of women working in Information Technology motivated the "Women in Engineering group" at Criteo to create the "Journée Aujourd'hui Je Code !" initiative. Our primary goals were to introduce teenagers to computer science, to learn coding basics in a fun environment, to meet engineers and to discover different potential careers in technology.

In this talk, we will detail first the guiding principles we found to make the workshops interesting for the teenagers. Fun was our top priority, but it was not everything: we had to deal with several questions. What could they learn in such a short time? How could we let them unlock their creativity? How could we best share our passion for programming with them? We wanted them to feel the same emotions that we have when we code.

In a second part, we will detail how we developed two workshops, guided by these principles, using Python as the programming language. We will show demos of the two Python programs and how we used them for teaching.

Finally, we will share feedback from students and teachers.

#### Python @ Sorbonne Université (Frederic Peschanski, Sorbonne Université - LIP6)

Since 2015 Python (3.x) is the support language for the entry-level Computer Science course for Science and Engineering students at Sorbonne Université. The course involves more than 900 students each year (and probably much more in the near future), with 6+ parallel sessions, 40+ study groups and dedicated lab-works.  In this talk I will explain how such a large-scale course is organized,  behind the scene. I will also explain the role of the Python language in this course, demonstrating our dedicated and minimalistic IDE: MrPython.

### Theme: Tutorials


#### Dataviz with matplotlib and seaborn (Francis Wolinski, Yotta Conseil)

The aim of the workshop is to put into action the matplotlib and seaborn Python libraries. It is intended for beginners/intermediate and will be based on a notebook comprising a dataset so as to perform dataviz. Basic to advanced functionalities of matplotlib and seaborn will be experienced experimented during the session.

#### GeoSpatial Data Analysis using Python (Fereshteh ASGARI, Research Engineer)

If you have a set of geo-spatial data and you want to do some analysis and visualisation using Python (and even apply Machine learning algorithms on them) this tutorial is what you need. In this tutorial I will present the basics about geospatial data and how they are defined and presented, how to analysis, visualize and perform basic transformations on Geospatial data. All the techniques will be applied on a real data set. 

#### Machine learning using scikit-learn (Guillaume Lemaitre, INRIA)

This tutorial aims at introducing the new features developed in the last release of scikit-learn and how they should be used in a intermediate to complex data science workflow.

More specifically, we will introduce and present the following tools: pipeline, grid-search, column transformer, cross-validation utilities.

#### Understanding and diagnosing your machine-learning models (Gael Varoquaux, Inria)

Often achieving a good prediction is only half of the job. Questions immediately arise: How to improve this prediction? What drives the prediction? Can we operate changes to the system based on the predictions? All these questions require understanding how good is the model prediction, and how do the model predict.

This tutorial assumes basic knowledge of scikit-learn. It will focus on statistics, tests, and interpretation rather than improving the prediction. The notes for the tutorial can be found on http://gael-varoquaux.info/interpreting_ml_tuto/




#### Parallel Data Analysis with Dask (Loïc Estève, Inria)

Dask is a flexible tool for parallelizing Python code on a single machine or
across a cluster. It builds upon familiar tools in the SciPy ecosystem (e.g.
NumPy and Pandas) while allowing them to scale across multiple cores or
machines.

We can think of dask at a high and a low level:
- High level collections: Dask provides high-level Array, Bag, and DataFrame
  collections that mimic NumPy, lists, and Pandas but can operate in parallel
  on datasets that don't fit into main memory. Dask's high-level collections
  are alternatives to NumPy and Pandas for large datasets.
- Low Level schedulers: Dask provides dynamic task schedulers that execute task
  graphs in parallel. These execution engines power the high-level collections
  mentioned above but can also power custom, user-defined workloads. These
  schedulers are low-latency (around 200 us) and work hard to run computations
  in a small memory footprint. Dask's schedulers are an alternative to direct
  use of threading or multiprocessing libraries in complex cases or other task
  scheduling systems like Luigi or IPython parallel.

Different users operate at different levels but it is useful to understand
both. This tutorial will cover both the high-level use of dask.array and
dask.dataframe and low-level use of dask graphs and schedulers.

#### Python Micro-services with Kubernetes (Michael Bright, @mjbright Consulting)

This tutorial will show attendees how to deploy Python-based micro-services to a Kubernetes cluster, with visualizations of what happens on the Kubernetes cluster using the KubeView tool (https://github.com/mjbright/kubeview) as many standard operations - deployment, upgrade, rollback, cordoning are performed.

Attendees can watch, follow along or repeat the tutorial at home using the online materials to be provided on github.

Attendees will perform some operations using kubectl command-line tool, and also the Kubernetes Python client.
