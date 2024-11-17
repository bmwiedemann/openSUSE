#
# spec file for package python-bson
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-bson
Version:        0.5.10
Release:        0
Summary:        BSON codec for Python
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/py-bson/bson
Source:         https://github.com/py-bson/bson/archive/%{version}.tar.gz#/bson-%{version}.tar.gz
# PATCH-FIX-UPSTREAM drop-python2-support.patch gh#py-bson/bson#118
Patch0:         drop-python2-support.patch
# PATCH-FIX-OPENSUSE Use assertEqual to support Python 3.12
Patch1:         support-python312.patch
Patch2:         fix2038.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-dateutil >= 2.4.0}
# /SECTION
%python_subpackages

%description
BSON codec for Python.

%prep
%autosetup -p1 -n bson-%{version}
sed -i '1 {/^#!/d}' bson/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE_APACHE
%{python_sitelib}/bson
%{python_sitelib}/bson-%{version}.dist-info

%changelog
