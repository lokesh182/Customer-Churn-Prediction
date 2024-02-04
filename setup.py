import setuptools# Required for packaging and distribution of the package
 
with open("README.md","r",encoding="utf-8") as f: # Read the README.md file
    long_description = f.read() # Store the contents of the file in the variable long_description
    
__version__ = "0.0.0" # Version of the package

REPO_NAME = "Customer-Churn-Prediction" # Name of the repository
AUTHOR_USER_NAME = "lokesh182" #  
SRC_REPO = "CustomerChurnPrediction"# Name of the repository
AUTHOR_EMAIL = "lokesh18.ml@gmail.com" # Email of the author

setuptools.setup(
    name = SRC_REPO, # Name of the repository
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small package for Customer Churn Prediction",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", # URL of the repository
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",# URL of the bug tracker
    },
    package_dir = {"":"src"}, # Directory where the package is located
    packages = setuptools.find_packages(where = "src") # Find the packages in the directory
)