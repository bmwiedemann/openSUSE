#
# spec file for package python-terminado
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Disable tests until random testing race condition fixed, see: https://github.com/jupyter/terminado/issues/21
%bcond_with     tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-terminado
Version:        0.8.2
Release:        0
Summary:        Terminals served to termjs using Tornado websockets
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/jupyter/terminado
Source:         https://files.pythonhosted.org/packages/source/t/terminado/terminado-%{version}.tar.gz
BuildRequires:  %{python_module ptyprocess}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-ptyprocess
Requires:       python-tornado >= 4
BuildArch:      noarch
%python_subpackages

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

It evolved out of pyxterm, which was part of GraphTerm (as lineterm.py), and
ultimately derived from the public-domain Ajaxterm code (also on Github as part
of QWeb).

%prep
%setup -q -n terminado-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_max_terminals'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
