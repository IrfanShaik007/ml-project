from setuptools import find_packages,setup
from typing import List
hypen='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements
    






setup(
    name='MLProject',
    version='0.0.1',
    author='SHAIK_IRFAN',
    author_email='Irfanshareef05@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)