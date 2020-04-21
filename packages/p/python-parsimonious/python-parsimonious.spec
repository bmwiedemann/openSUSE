#
# spec file for package python-parsimonious
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
Name:           python-parsimonious
Version:        0.8.1
Release:        0
Summary:        Pure-Python PEG parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/erikrose/parsimonious
Source:         https://files.pythonhosted.org/packages/source/p/parsimonious/parsimonious-%{version}.tar.gz
# PATCH-FIX-UPSTREAM replace-nose.patch gh#erikrose/parsimonious#160 mcepl@suse.com
# replace use of nose with the standard library
Patch0:         replace-nose.patch

BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
BuildArch:      noarch
%python_subpackages

%description
Parsimonious is an arbitrary-lookahead parser written in pure
Python. It's based on parsing expression grammars (PEGs), which
means you feed it a simplified sort of EBNF notation.

%prep
%setup -q -n parsimonious-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
