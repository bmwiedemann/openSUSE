#
# spec file for package python-bson
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
Name:           python-bson
Version:        0.5.8
Release:        0
Summary:        BSON codec for Python
License:        BSD-3-Clause AND Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/py-bson/bson
Source:         https://github.com/py-bson/bson/archive/%{version}.tar.gz#/bson-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.4.0
Requires:       python-six >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-dateutil >= 2.4.0}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
%python_subpackages

%description
BSON codec for Python.

%prep
%setup -q -n bson-%{version}
sed -i '1 {/^#!/d}' bson/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE_APACHE
%{python_sitelib}/*

%changelog
