#
# spec file for package pmemkv-python
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


Name:           pmemkv-python
Version:        1.0
Release:        0
Summary:        Machine administration
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pmem/pmemkv-python
Source:         https://github.com/pmem/pmemkv-python/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pmemkv-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       pmemkv-python-%{version}-%{release}
ExclusiveArch:  x86_64 aarch64 ppc64le
%{?systemd_ordering}
# This software does not compile with gcc 7 or earliear.
# When SLES moves to gcc 8 or later as default compiler
# this patch can be removed
%if %{defined sle_version}
Patch0:         gcc_9.patch
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Python bindings for pmemkv. Currently functionally equal to pmemkv in version 1.0. Some of the new functionalities (from pmemkv 1.1) are not yet available.

%prep
%setup -q
%if %{defined sle_version}
%patch -P 0 -p1
%endif

%build
%py3_build

%install
%py3_install

%files
%{python3_sitearch}/pmemkv-*
%dir %{python3_sitearch}/pmemkv
%{python3_sitearch}/pmemkv/*
%{python3_sitearch}/_pmemkv.cpython-*

%changelog
