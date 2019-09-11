#
# spec file for package python-latexcodec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-latexcodec
Version:        1.0.5
Release:        0
Summary:        A lexer and codec to work with LaTeX code in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mcmtroffaes/latexcodec
Source:         https://github.com/mcmtroffaes/latexcodec/archive/1.0.5.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.4.1
BuildArch:      noarch
%python_subpackages

%description
A lexer and codec to work with LaTeX code in Python.

%prep
%setup -q -n latexcodec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_exec %{_bindir}/nosetests -v}

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst LICENSE.rst README.rst
%{python_sitelib}/*

%changelog
