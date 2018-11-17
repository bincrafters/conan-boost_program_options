#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostProgram_OptionsConan(base.BoostBaseConan):
    name = "boost_program_options"
    url = "https://github.com/bincrafters/conan-boost_program_options"
    lib_short_names = ["program_options"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_only_deps = [
        "bind",
        "tokenizer"
    ]
    b2_defines = [
        "BOOST_PROGRAM_OPTIONS_DYN_LINK=1"
    ]
    source_only_deps = [
        "tokenizer",
    ]
    b2_requires = [
        "boost_any",
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_function",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]


