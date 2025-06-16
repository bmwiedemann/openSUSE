#
# spec file for package python-CCColUtils
#
# Copyright (c) 2025 SUSE LLC
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


%define oldpython python
Name:           python-CCColUtils
Version:        1.5
Release:        0
Summary:        Kerberos5 Credential Cache Collection utilities
License:        GPL-2.0-or-later
URL:            https://pagure.io/cccolutils
Source:         https://files.pythonhosted.org/packages/source/C/CCColUtils/CCColUtils-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(krb5)
%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150200
BuildRequires:  %{oldpython}-krbV
Suggests:       %{oldpython}-krbV
%endif
%python_subpackages

%description
Kerberos5 Credential Cache Collection utilities.

%prep
%setup -q -n CCColUtils-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license COPYING
%{python_sitearch}/cccolutils.cpython-*-linux-gnu.so
%{python_sitearch}/[Cc][Cc][Cc]ol[Uu]tils-%{version}.dist-info

%changelog
