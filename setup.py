import setuptools

VERSION = "1.0.0"
PACKAGE_NAME = "S3GeoJSONProvider"
AUTHOR = "Valerio Luzzi, Marco Renzi, EHJ, JSL"
EMAIL = "valerio.luzzi@gecosistema.com, marco.renzi@gecosistema.com"
GITHUB = "https://github.com/icisk/pygeoapi-provider-s3-geojson.git"
DESCRIPTION = "An implementation of a GeoJSON provider for Pygeoapi with compatibility for S3 buckets."

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url=GITHUB,
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        's3fs',
        'pygeoapi'
    ]
)
