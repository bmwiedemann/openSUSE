#
# spec file for package python-unittest-mixins
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
Name:           python-unittest-mixins
Version:        1.6
Release:        0
License:        Apache-2.0
Summary:        Helpful mixins for unittest classes
Url:            https://github.com/nedbat/unittest-mixins
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/u/unittest-mixins/unittest-mixins-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module six >= 1.4.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six >= 1.4.0
BuildArch:      noarch

%python_subpackages

%description
Helpful mixins for unittest classes.

%prep
%setup -q -n unittest-mixins-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
