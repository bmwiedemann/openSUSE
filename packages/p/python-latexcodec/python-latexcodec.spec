#
# spec file for package python-latexcodec
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


%define modname latexcodec
Name:           python-latexcodec
Version:        3.0.0
Release:        0
Summary:        A lexer and codec to work with LaTeX code in Python
License:        MIT
URL:            https://github.com/mcmtroffaes/latexcodec
Source:         https://github.com/mcmtroffaes/latexcodec/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A lexer and codec to work with LaTeX code in Python.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/latexcodec
%{python_sitelib}/latexcodec-%{version}.dist-info

%changelog
