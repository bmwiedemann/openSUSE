#
# spec file for package python-vine
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
Name:           python-vine
Version:        1.3.0
Release:        0
Summary:        Python Promises
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/celery/vine/
Source:         https://pypi.io/packages/source/v/vine/vine-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module case}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Promises implementation for python.

%prep
%setup -q -n vine-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %python_files
%defattr(-,root,root,-)
%doc Changelog LICENSE README.rst
%{python_sitelib}/*

%changelog
