from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'K&H VCF Parser'
LONG_DESCRIPTION = 'VCF Parser for VCF versions 4.0 and 4.1 at GenePoweRx'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cvmvcf",
        version=VERSION,
        author="Vamsi Mohan Challa",
        author_email="vmchalla@khdreamlife.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: GenePoweRx Employees",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Ubuntu :: Linux",
        ]
)