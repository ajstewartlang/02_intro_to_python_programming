Installing Python with Conda 
============================

In this first workshop we will cover how to install Python (plus Jupyter notebooks) via the package manager Conda.

<center>

<iframe width="560" height="315" src="https://youtube.com/embed/HjF98JryayQ" frameborder="0" allowfullscreen></iframe>

</center>

&nbsp;

You can view and download the slides in a variety of formats by clicking on the image below.

<center>

[![link_to_slides](images/conda_slides.png)](https://docs.google.com/presentation/d/18H_H-qQLbtFSF-jjUIQqHGEN7WxBpOuIfxcHF7f7cnA/edit?usp=sharing)
    
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

Rather than just use the default environment, it’s better practice from a reproducibility point of view to create a separate environment for each type of project. That way, you can have different packages - and different versions of each package - in different environments. Updating a package in one environment won’t affect the package in other environments - all this is managed via `conda`.

Below I use the conda create command to create a new virtual environment that I’m calling `data_science`. If I want just a few specific packages, I’d add the package names after `data_science` (I can also add the package versions too here if I want, e.g., `numpy=1.19.2` and `pandas=1.1.3`). I could even specify the version of Python I want my adding `Python=3.7.1`.

    $ conda create --name data_science conda numpy=1.19.2 pandas=1.1.3
    
Typing conda list will list the packages and version numbers in the currently active environment. Note, here we’re now in the data_science environment.

    $ conda activate data_science
    $ conda list
    # packages in environment at /home/andrew/anaconda3/envs/data_science:
    #
    # Name                    Version                   Build  Channel
    _libgcc_mutex             0.1                        main  
     alabaster                 0.7.12                     py_0  
    anaconda                  2020.11                  py38_0  
    anaconda-client           1.7.2                    py38_0  
    anaconda-project          0.8.4                      py_0  
    argh                      0.26.2                   py38_0  
    argon2-cffi               20.1.0           py38h7b6447c_1  
    asn1crypto                1.4.0                      py_0   
    ...

If we need to export all the information about our environment (perhaps to share with others or to build a Docker image), we can do that using the following to produce output in YAML format:

    $ conda env export
    name: data_science
    channels:
      - defaults
    dependencies:
      - _libgcc_mutex=0.1=main
      - alabaster=0.7.12=py_0
      - anaconda=2020.11=py38_0
      - anaconda-client=1.7.2=py38_0
      - anaconda-project=0.8.4=py_0
      - argh=0.26.2=py38_0
      - argon2-cffi=20.1.0=py38h7b6447c_1
      - asn1crypto=1.4.0=py_0
    ...

## Creating a new Python shell and Jupyter Kernel

Make sure you are not in the default environment (type conda deactivate if (base) is displayed in front of your prompt). In the following, I activate my new environment, install the ipykernel package (if it’s not already present) and create the kernel for use in Jupyter.
 
    (base)$ conda activate data_science
    (data_science)$ conda install ipykernel
    (data_science)$ python -m ipykernel install --user --name data_science --display-name "Python (data_science)"

We’re now ready to fire up a Jupyter Notebook. To do that, type: 

    (data_science)$ jupyter notebook

In the video, you'll be able to see what happens when the Jupyter Notebook opens in our browser. Follow the steps in the video and save your Python script as a `.py` file.

## Running the .py script from the CLI

We can run Python scripts from the command line - just make sure you’re running it in the right conda environment - we can tell that we’re in the `data_science` environment by the fact that `(data_science)` is presented at the start of the prompt. From the folder where you’ve saved the `hello_world.py` script, you can type python `hello_world.py` like below.

    (data_science)$ python hello_world.py
    hello world!
    Our two variables added together equals 3

Obviously this is a trivial example, but it’s useful to remember that you can run Python scripts like this rather than having to manually run things in Jupyter Notebooks or another interactive environment.


    

