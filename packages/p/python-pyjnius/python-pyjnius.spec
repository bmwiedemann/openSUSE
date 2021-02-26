#
# spec file for package python-pyjnius
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
%define pythons python38
Name:           python-pyjnius
Version:        1.3.0
Release:        0
Summary:        Access Java classes from Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kivy/pyjnius
Source:         https://github.com/kivy/pyjnius/archive/%{version}.tar.gz#/pyjnius-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  python-rpm-macros
Requires:       python-Cython
Requires:       python-six >= 1.7.0
# SECTION test requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.7.0}
BuildRequires:  javapackages-local
# /SECTION
%python_subpackages

%description
Access Java classes from Python.

%prep
%setup -q -n pyjnius-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

ant jar test-compile
ls build/pyjnius.jar

%install
%python_install
%{python_expand rm -f %{buildroot}%{$python_sitearch}/setup_sdist.py %{buildroot}%{$python_sitearch}/__pycache__/setup_sdist.*
%fdupes %{buildroot}%{$python_sitearch}
}

%check

mv jnius /tmp/jnius
%{python_expand export CLASSPATH=${PWD}/build/pyjnius.jar:${PWD}/build/test-classes:%{buildroot}%{$python_sitearch}/jnius/src:%{buildroot}%{$python_sitearch}/jnius/:
export PYTHONPATH=${PWD}:%{buildroot}%{$python_sitearch}
$python -m pytest
}
mv /tmp/jnius .

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitearch}/*

%changelog
