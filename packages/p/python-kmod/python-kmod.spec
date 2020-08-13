#
# spec file for package python-kmod
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-kmod
Version:        0.9.1
Release:        0
Summary:        Python module to work with kernel modules
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/agrover/python-kmod
Source:         https://files.pythonhosted.org/packages/source/k/kmod/kmod-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-build.patch
Patch0:         fix-build.patch
Patch1:         fix-build-kmod-17.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  kmod
BuildRequires:  libkmod-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for kmod/libkmod

kmod is a set of tools to handle common tasks with Linux kernel modules like
insert, remove, list, check properties, resolve dependencies and aliases.

These tools are designed on top of libkmod, a library that is shipped with
kmod. It can be found at:

http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary

python-kmod is a Python wrapper module for libkmod, exposing common module
operations: listing installed modules, modprobe, and rmmod.

%prep
%setup -q -n kmod-%{version}
%if 0%{?suse_version} > 1320
%patch0 -p1
%else
%patch1 -p1
%endif

%build
%python_build

%install
%python_install

%files %{python_files}
%dir %{python_sitearch}/kmod/
%{python_sitearch}/kmod/*
%{python_sitearch}/kmod*.egg-info
%license COPYING.LESSER README

%changelog
