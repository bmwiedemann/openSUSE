#
# spec file for package python-pydenticon
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# tests on big endian systems fail due to https://github.com/azaghal/pydenticon/issues/10 , disabled until fixed"
# can not use "ifarch" when BuildArch is set to noarch
%if %_arch == s390x || %_arch == s390x || %_arch == ppc || %_arch == ppc64
%bcond_with test
%else
%bcond_without test
%endif
%define         modname pydenticon
Name:           python-%{modname}
Version:        0.3.1
Release:        0
Summary:        Library for generating identicons
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/azaghal/%{modname}
Source:         https://pypi.io/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       python-Pillow

%python_subpackages

%description
Pydenticon is a small utility library that can be used for deterministically
generating identicons based on the hash of provided data.

The implementation is a port of the Sigil identicon implementation from:

* https://github.com/cupcake/sigil/

Pydenticon provides a couple of extensions of its own when compared to the
original Sigil implementation, like:

* Ability to supply custom digest algorithms (allowing for larger identicons if
  digest provides enough entropy).
* Ability to specify a rectangle for identicon size..

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{modname}

%check
%if %{with test}
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
