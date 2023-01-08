#
# spec file for package python-terminado
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


Name:           python-terminado
Version:        0.17.1
Release:        0
Summary:        Terminals served to termjs using Tornado websockets
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/terminado
Source:         https://files.pythonhosted.org/packages/source/t/terminado/terminado-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 0.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ptyprocess}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ptyprocess
Requires:       python-tornado >= 4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

It evolved out of pyxterm, which was part of GraphTerm (as lineterm.py), and
ultimately derived from the public-domain Ajaxterm code (also on Github as part
of QWeb).

%prep
%setup -q -n terminado-%{version}
sed -i '/addopts/ s/--durations 10 --color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/jupyter/terminado/issues/21
donttest="test_max_terminals"
# somehow the reading from the spawned process does fail inside OBS
donttest+=" or test_basic"
# ?
donttest+=" or test_unique_processes"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/terminado
%{python_sitelib}/terminado-%{version}*-info

%changelog
