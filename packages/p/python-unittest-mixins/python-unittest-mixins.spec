#
# spec file for package python-unittest-mixins
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-unittest-mixins
Version:        1.6
Release:        0
Summary:        Helpful mixins for unittest classes
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nedbat/unittest-mixins
Source:         https://files.pythonhosted.org/packages/source/u/unittest-mixins/unittest-mixins-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/nedbat/unittest-mixins/pull/4 drop python<=3.7 support and use of six module
Patch0:         drop-old-pythons.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Helpful mixins for unittest classes.

%prep
%autosetup -p1 -n unittest-mixins-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/unittest_mixins
%{python_sitelib}/unittest_mixins-%{version}*-info

%changelog
