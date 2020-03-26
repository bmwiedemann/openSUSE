#
# spec file for package python-fasteners
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
Name:           python-fasteners
Version:        0.14.1
Release:        0
Summary:        A python package that provides useful locks
License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
Source:         https://files.pythonhosted.org/packages/source/f/fasteners/fasteners-%{version}.tar.gz
BuildRequires:  %{python_module monotonic >= 0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-monotonic >= 0.1
Requires:       python-six
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-futures
%endif
%python_subpackages

%description
A python package that provides useful locks
It includes the following.
 * Locking decorator
 * Reader-writer locks
 * Inter-process locks
 * Generic helpers

%prep
%setup -q -n fasteners-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/*

%changelog
