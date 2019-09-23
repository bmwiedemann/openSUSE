#
# spec file for package python-shortuuid
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-shortuuid
Version:        0.5.0
Release:        0
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stochastic-technologies/shortuuid/
Source:         https://files.pythonhosted.org/packages/source/s/shortuuid/shortuuid-%{version}.tar.gz
# https://github.com/skorokithakis/shortuuid/issues/38
Patch0:         shortuuid-no-pep8.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library that generates short, pretty, unambiguous unique IDs
by using an extensive, case-sensitive alphabet and omitting
similar-looking letters and numbers.

%prep
%setup -q -n shortuuid-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
