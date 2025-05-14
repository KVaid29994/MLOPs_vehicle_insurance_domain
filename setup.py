## setup.py is that label and packing list combined.
## It tells Python (and tools like pip) how to install your project as a package.
## find_packages()	Automatically finds all sub-packages (with __init__.py)


from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",  # Initial version of the package
    author="Kashish Vaid",
    author_email="kashish,vaid29994@gmail.com",
    packages=find_packages()
)

# setup: Main function to define metadata and configuration for your package.
# find_packages(): Automatically detects and includes all Python packages (i.e. folders with __init__.py) under your project directory.
#🧾 Why Do We Need This?
        ### package your code .  Use in cloud / Docker