Installing Python with Conda 
============================

In this first workshop we will cover how to install Python (plus Jupyter notebooks) via the package manager Conda.

<center>

<iframe width="560" height="315" src="https://youtube.com/embed/HjF98JryayQ" frameborder="0" allowfullscreen></iframe>

</center>

&nbsp;

You can view and download the slides in a variety of formats by clicking on the image below.

<center>

[![link_to_slides](images/conda_slides.png){:height="50%" width="50%"}](https://docs.google.com/presentation/d/18H_H-qQLbtFSF-jjUIQqHGEN7WxBpOuIfxcHF7f7cnA/edit?usp=sharing)
    
</center>

## Why Python?

The main goal of this session is to ensure you have a working Python installation using Conda that you can access via Jupyter Notebooks. Python is a general purpose programming language increasingly used for machine learning and scientific programming (as well as a bunch of other things such as the Instagram, Netflix, Spotify). Many data science/analysis roles require a mix of Python and R - it’s great if you know one of these languages, even better if you know both!

Python and R are both interpreted languages - and code can be used together (you can run a Python script from within an R session, and vice versa). You may find some things are easier/quicker to code in one language, and others in the other. So why not use both?

## Installing Conda and Python

Conda is a package and environment management system that will allow us to install Python (as well as other data science tools), assorted libraries and importantly allow us to manage which versions of the software we're using for different projects we might be working on. This managment of packages and environments is important and sometimes you'll find that different projects you are involved with require *different* versions of Python and/or Python libraries. By creating separate environments (with particular configurations of software versions), your data science life will become so much easier.

To install Conda (which comes with Python and common libraries), just follow the instructions here:

https://www.anaconda.com/products/individual

Once it's installed, check to make sure things are working ok by following the guide here:

https://docs.anaconda.com/anaconda/install/verify-install/

On Windows machines, you can access the command line interface (CLI) using the Anaconda Prompt in the Windows Start menu. On MacOS and Linux, access the CLI via the Terminal. The Terminal on a Mac can be found in the Utilities folder within your Applications folder. You might want to pin it to your Dock as you'll be using it a lot in this course.

To check your Conda installation has worked, open a Terminal window and at the prompt type:

    $ conda activate
    $ python --version
    Python 3.8.8

This will print the version of Python you are running - which in my case ia Python 3.8.8. In the terminal, you can start a Jupyter Notebook running in your default Conda environment by typing:

    $ jupyter notebook

This should automatically open via your web browser. If it doesn't open automatically, just copy and paste the link in the Terminal to your web browser manually. Of course, we just said that we may need to use different environments for different Python projects we are working on so now let's look at how we create those.

## Creating a new Python environment

kk
