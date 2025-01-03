#
# spec file for package python-bibtexparser
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-bibtexparser
Version:        1.4.3
Release:        0
Summary:        Bibtex parser for python
License:        BSD-3-Clause OR LGPL-3.0-only
URL:            https://github.com/sciunto-org/python-bibtexparser
Source:         https://github.com/sciunto-org/python-bibtexparser/archive/v%{version}.tar.gz#/python-bibtexparser-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyparsing >= 2.0.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyparsing >= 2.0.3}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python library to parse bibtex files.

%prep
%autosetup -p1 -n python-bibtexparser-%{version}
sed -i -e '/^#!\//, 1d' bibtexparser/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.utf8
%pytest

%files %{python_files}
%doc README.rst CHANGELOG
%license COPYING
%{python_sitelib}/bibtexparser
%{python_sitelib}/bibtexparser-%{version}.dist-info

%changelog
