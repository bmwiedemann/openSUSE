#
# spec file for package python-bibtexparser
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
%bcond_without  python2
Name:           python-bibtexparser
Version:        1.1.0
Release:        0
Summary:        Bibtex parser for python
License:        LGPL-3.0-only OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sciunto-org/python-bibtexparser
Source:         https://github.com/sciunto-org/python-bibtexparser/archive/v%{version}.tar.gz#/python-bibtexparser-%{version}.tar.gz
# https://github.com/sciunto-org/python-bibtexparser/pull/259
Patch0:         python-bibtexparser-remove-unittest2.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future >= 0.16.0
Requires:       python-pyparsing >= 2.0.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future >= 0.16.0}
BuildRequires:  %{python_module pyparsing >= 2.0.3}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-unittest2
%endif
# /SECTION
%python_subpackages

%description
Python library to parse bibtex files..

%prep
%setup -q -n python-bibtexparser-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' bibtexparser/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.utf8
%pytest

%files %{python_files}
%doc README.rst CHANGELOG
%license COPYING
%{python_sitelib}/bibtexparser-%{version}-py*.egg-info
%{python_sitelib}/bibtexparser/

%changelog
