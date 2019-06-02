#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostProgram_OptionsConan(base.BoostBaseConan):
    name = "boost_program_options"
    version = "1.70.0"

    @property
    def boost_build_defines(self):
        return ["BOOST_PROGRAM_OPTIONS_DYN_LINK=1"]
