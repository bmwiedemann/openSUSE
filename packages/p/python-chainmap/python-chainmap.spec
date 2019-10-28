#
# spec file for package python-chainmap
#
# Copyright (c) 2017-2019, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-chainmap
Version:        1.0.3
Release:        0
License:        Python-2.0
Summary:        Backport/clone of ChainMap for py26, py32, and pypy3
Url:            https://bitbucket.org/jeunice/chainmap
Group:          Development/Languages/Python
Source:         chainmap-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
This module is a polyfill implementing 'ChainMap' for
reasonably-recent versions of Python that do not have
'collections.ChainMap' --namely, Python 2.6, Python 3.2,
and PyPy3 releases based on Python 3.2. (It will also
work as expected on Python 2.7, PyPy, and Python 3.3 and higher,
but it is not needed there since those verions' 'collection'
modules contains a 'ChainMap' implementation.)

%prep
%setup -q -n chainmap-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.yml README.rst
%{python_sitelib}/*

%changelog
