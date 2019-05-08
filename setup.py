import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-captcha3",
    version="1.0",
    author="Abdallah Nassif",
    author_email="a.nassif@sit-mena.com",
    description="Django form field google captcha extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sitmena/sitech-django-models",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'': ['templates/*.html']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
