#
# spec file for package python-case
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
Name:           python-case
Version:        1.5.3
Release:        0
Summary:        Python unittest Utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/celery/case
Source:         https://files.pythonhosted.org/packages/source/c/case/case-%{version}.tar.gz
Patch:          remove_unittest2.patch
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mock >= 2.0
Requires:       python-nose >= 1.3.7
Requires:       python-setuptools
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python unittest Utilities

%prep
%setup -q -n case-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc Changelog README.rst
%{python_sitelib}/*

%changelog
