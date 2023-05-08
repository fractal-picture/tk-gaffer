#!/bin/env python
# -*- coding: utf-8 -*-

name = 'tk_gaffer'

description = """Implementation of a shotgun engine for Gaffer. It supports the classic bootstrap 
startup methodology and integrates with Gaffer adding a new Shotgun Menu in the main Gaffer tool-bar."""

authors = ['https://www.linkedin.com/in/diegogh/']
help = 'https://github.com/diegogh/tk-gaffer'

plugin_for = ["tk_core"]

requires = ['~tk_core']


build_command = r"J:\tools\bin\rezutils\fdeploy_rez.bat {install}"
# build_command = r"python J:\tools\pipecrew\mgangaiwar\workspace\FractalPicture\packages\fdeploy\python\fdeploy\rez_deploy.py {install}"
# build_command = "rez env git GitPython rez fdeploy -- rez_deploy.bat {install}"
build_requires = ["python", "GitPython", "git", "rez"]


@early()
def _version():
    import fp_rezutils
    return fp_rezutils.get_next_tag_version("minor")

version = _version()


def commands():
    env.PYTHONPATH.append("{root}/python")

    # required for `tk_gaffer` to bootstrap itself
    env.SGTK_GAFFER_MODULE_PATH = "{root}/python"
    env.SGTK_GAFFER_ENGINE_STARTUP = "{root}/startup/init.py"
    env.SGTK_ENGINE = "tk_gaffer"

    env.GAFFER_STARTUP_PATHS.append("{root}/python")
    env.GAFFER_STARTUP_PATHS.append("{root}/startup")



uuid = 'tk_gaffer'
