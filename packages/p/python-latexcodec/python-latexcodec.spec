#
# spec file for package python-latexcodec
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
%define modname latexcodec
Name:           python-latexcodec
Version:        2.0.1
Release:        0
Summary:        A lexer and codec to work with LaTeX code in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mcmtroffaes/latexcodec
Source:         https://github.com/mcmtroffaes/latexcodec/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/mcmtroffaes/latexcodec/commit/88eca3e4e279ffa313662a75052598ec5610ff92
Patch0:         python-latexcodec-no-python2.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A lexer and codec to work with LaTeX code in Python.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
