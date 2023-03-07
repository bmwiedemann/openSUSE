#
# spec file for package python-pyjnius
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pyjnius
Version:        1.4.2
Release:        0
Summary:        Access Java classes from Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kivy/pyjnius
Source:         https://github.com/kivy/pyjnius/archive/%{version}.tar.gz#/pyjnius-%{version}.tar.gz
# https://github.com/kivy/pyjnius/commit/ee4e9c224c4a3dda1f15a6f161cd0dfb268eb0e3
Patch0:         python-pyjnius-no-python2.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  python-rpm-macros
Requires:       python-Cython
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  javapackages-local
# /SECTION
%python_subpackages

%description
Access Java classes from Python.

%prep
%setup -q -n pyjnius-%{version}
%patch0 -p1
sed -i 's:python:python3:' tests/test_jvm_options.py

%build
export CFLAGS="%{optflags}"
%python_build
ant jar test-compile
mv build/test-classes tests

%install
%python_install
%{python_expand rm -f %{buildroot}%{$python_sitearch}/setup_sdist.py %{buildroot}%{$python_sitearch}/__pycache__/setup_sdist.*
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mv jnius jnius.hide
%{python_expand export CLASSPATH="${PWD}/tests/test-classes:${PWD}/jnius.hide/src"
export PYTHONPATH=${PWD}:%{buildroot}%{$python_sitearch}
# https://github.com/kivy/pyjnius/issues/617
$python -m pytest -k 'not test_jvm_options'
}

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitearch}/*

%changelog
