#
# spec file for package python-transitions
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-transitions
Version:        0.8.1
Release:        0
Summary:        A lightweight, object-oriented Python state machine implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytransitions/transitions
Source:         https://files.pythonhosted.org/packages/source/t/transitions/transitions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Suggests:       python-pygraphviz
Suggests:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pygraphviz}
BuildRequires:  %{python_module pytest < 5}
BuildRequires:  %{python_module six}
# png support for graphviz
BuildRequires:  graphviz-gnome
# /SECTION
%python_subpackages

%description
The transitions package makes it convenient and relatively easy to define and
implement FSMs (finite state machines) in python.

%prep
%setup -q -n transitions-%{version}
find . -type f -exec chmod -x {} \;
sed -i 's/\r$//' LICENSE Changelog.md README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -v tests/test_codestyle.py
%pytest

%files %{python_files}
%license LICENSE
%doc Changelog.md README.md
%{python_sitelib}/*

%changelog
