#
# spec file for package python-pocketsphinx-python
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
Name:           python-pocketsphinx-python
Version:        0.1.3
Release:        0
Summary:        Python interface to CMU Sphinxbase and Pocketsphinx libraries
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/bambocher/pocketsphinx-python
Source:         https://files.pythonhosted.org/packages/source/p/pocketsphinx/pocketsphinx-%{version}.tar.bz2
Patch0:         fix-encoding.diff
# PATCH-FIX-UPSTREAM https://github.com/bambocher/pocketsphinx-python/pull/45
Patch1:         reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libpulse-devel
BuildRequires:  python-rpm-macros
BuildRequires:  swig
Provides:       pocketsphinx = %{version}
Obsoletes:      pocketsphinx < %{version}
%python_subpackages

%description
This package provides a python interface to CMU Sphinxbase and Pocketsphinx libraries created with SWIG and Setuptools.
Pocketsphinx is a part of the CMU Sphinx Open Source Toolkit For Speech Recognition.

%prep
%setup -q -n pocketsphinx-%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
