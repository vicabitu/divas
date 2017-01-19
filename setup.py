from distutils.core import setup
import py2exe

setup(name="main",
 version="1.0",
 description="Demo2",
 author="VoidSoftware",
 author_email="mi_correo@",
 url="url del proyecto",
 license="GPL",
 scripts=["main.py"],
 console=["main.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)