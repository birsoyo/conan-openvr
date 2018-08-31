# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools

class OpenvrConan(ConanFile):
    name = 'openvr'
    version = '1.0.16'
    description = 'OpenVR is an API and runtime that allows access to VR hardware from multiple vendors without requiring that applications have specific knowledge of the hardware they are targeting.'
    url = 'https://github.com/birsoyo/conan-openvr'
    homepage = 'https://github.com/ValveSoftware/openvr'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = 'BSD-3-Clause'

    # Packages the license for the conanfile.py
    exports = ['LICENSE.md']

    settings = 'os_build', 'arch_build'
    no_copy_source = True

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = 'https://github.com/ValveSoftware/openvr'
        tools.get(f'{source_url}/archive/v{self.version}.tar.gz')
        extracted_dir = f'{self.name}-{self.version}'
        #Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy(pattern='LICENSE', dst='licenses', src=self.source_subfolder)
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can just remove the lines below
        include_folder = os.path.join(self.source_subfolder, 'headers')
        self.copy(pattern='*', dst='include', src=include_folder)

        os_build = {
            'Windows': 'win',
            'Macos': 'osx',
            'Linux': 'linux'
        }[str(self.settings.os_build)]

        arch_build = {
            'x86': '32',
            'x86_64': '64'
        }[str(self.settings.arch_build)]

        libpath = f'{self.source_subfolder}/lib/{os_build}{arch_build}'
        self.copy(pattern='*.lib', dst='lib', src=libpath, keep_path=False)
        self.copy(pattern='*.so', dst='lib', src=libpath, keep_path=False)

        binpath = f'{self.source_subfolder}/bin/{os_build}{arch_build}'
        self.copy(pattern='*', dst='bin', src=binpath, keep_path=True)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
