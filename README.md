# cvmvcf
## _cvmvcf is my spinoff of pyvcf_

Pyvcf is currently not being maintained actively. This package helps those who want to parse vcf and are looking for similar functinality as pyvcf.

## How to work with cvmvcf

- Read Pyvcf documentation for working with cvmvcf
-  [Pyvcf Documentation](https://pyvcf.readthedocs.io/en/latest/INTRO.html) - HTML

## Installation

To install cvmvcf you need [Python 3](https://www.python.org/downloads/) v3.9+ to run.

Install the library.
You can install it in your local by downloading this libray, unzip it and then pip install the local extracted directory.
## Example: 
say you have downloaded the zip file and extracted into a folder call cvm in 
```sh 
C:\Users\sam\cvm
```
You can pip install using the following command:
```sh
pip3 install C:\Users\sam\cvm\cvmvcf
```

If you want to make any changes and reinstall the library

```sh
pip3 uninstall cvmvcf
cd C:\Users\sam\cvm\cvmvcf
pip3 install wheel
pip3 install setuptools
pip3 install twine
python3 setup.py bdist_wheel
pip3 install C:\Users\sam\cvm\cvmvcf
```

## Thats it... Enjoy parsing vcf as before

## License

MIT

**Free Software, Hell Yeah!**
