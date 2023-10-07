from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.00',
    description='Package for sorting files in a specific folder',
    url='https://github.com/Awaveform/HW7.git',
    author='Antonii Illarionov',
    author_email='antonii.illarionov@gmail.com',
    license='unlicensed',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sort_files_by_path']}
)
