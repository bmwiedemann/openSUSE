#
# spec file for package python-pytest-dependency
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pytest-dependency
Version:        0.5.1
Release:        0
Summary:        Manage dependencies of tests
License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
Source:         https://files.pythonhosted.org/packages/source/p/pytest-dependency/pytest-dependency-%{version}.tar.gz
Patch0:         https://github.com/RKrahl/pytest-dependency/commit/0930889a.patch#/pytest6.2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.6.0
BuildArch:      noarch
%python_subpackages

%description
This pytest plugin manages dependencies of tests.  It allows to mark
some tests as dependent from other tests.  These tests will then be
skipped if any of the dependencies did fail or has been skipped.

%prep
%setup -q -n pytest-dependency-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
