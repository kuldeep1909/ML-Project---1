# this is responsible to create a ml project as a package and we can deploy this in pypi
## Building our appllication as a package



from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines into a list
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kuldeep',
    author_email='malviyakuldeep38@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
