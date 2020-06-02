#
# spec file for package python-deprecation
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
%bcond_without python2
Name:           python-deprecation
Version:        2.1.0
Release:        0
Summary:        A library to handle automated deprecations
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/briancurtin/deprecation
Source:         https://files.pythonhosted.org/packages/source/d/deprecation/deprecation-%{version}.tar.gz
# https://github.com/briancurtin/deprecation/pull/50
Patch0:         python-deprecation-no-unittest2.patch
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-unittest2
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The `deprecation` library provides a `deprecated` decorator and a
`fail_if_not_removed` decorator for your tests. Together, the two
enable the automation of several things:

%prep
%setup -q -n deprecation-%{version}
%patch0 -p1

%build

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
