#
# spec file for package python-python-pseudorandom
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-pseudorandom
Version:        0.2.2
Release:        0
License:        GPL-3.0-or-later
Summary:        A Python library for generating pseudorandom condition
Url:            https://github.com/smathot/python-pseudorandom
Group:          Development/Languages/Python
Source:         https://github.com/smathot/python-pseudorandom/archive/release/%{version}.tar.gz#/python-pseudorandom-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module python-datamatrix}
# /SECTION
BuildRequires:  fdupes
Requires:       python-python-datamatrix
Recommends:     python-fastnumbers
Recommends:     python-numpy
BuildArch:      noarch

%python_subpackages

%description
A package for pseudorandomization of DataMatrix objects. That is, it allows
you to apply certain constraints to the randomization.

%prep
%setup -q -n python-pseudorandom-release-%{version}
touch _unittest/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test --test-suite=_unittest

%files %{python_files}
%license copyright COPYING
%doc readme.md examples/
%{python_sitelib}/*

%changelog
