from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='VirusInfo',
    version='0.4.1',
    description='Library for obtaining the number of people infected with COVID-19',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='gx1285',
    author_email="runay2342@gmail.com",
    url="https://github.com/gx1285/VirusInfo",
    install_requires="requests",
    python_requires='>=3.8.0',
    license='MIT',
    classifiers=[
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages()
)
