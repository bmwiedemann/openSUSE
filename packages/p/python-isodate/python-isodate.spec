#
# spec file for package python-isodate
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


# Tests don't work and cause a dependency loop with python-SPARQLWrapper
%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-isodate
Version:        0.6.0
Release:        0
Url:            http://cheeseshop.python.org/pypi/isodate
Summary:        An ISO 8601 Date/Time/Duration Parser and Formatter
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/isodate/isodate-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module implements ISO 8601 date, time and duration parsing.
The implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an allowed
option.

%prep
%setup -q -n isodate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%python_exec setup.py -q test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.txt README.rst TODO.txt
%{python_sitelib}/*

%changelog
