#
# spec file for package omniORBpy
#
# Copyright (c) 2022 SUSE LLC
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


Name:           omniORBpy
Summary:        Python bindings for the omniORB CORBA implementation
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Version:        4.3.0
Release:        0
URL:            http://omniorb.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/omniorb/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  omniORB-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.

%package devel
Group:          Development/Libraries/C and C++
Summary:        Header files for omniORBpy
Requires:       %{name} = %{version}

%description devel
omniORBpy-devel contains the omniORBpy development files.

%prep
%setup -q
find . -iname \*\.py -exec sed -ie '1 s@env python@python3@' '{}' \;

%build
%configure --disable-static \
           --with-omniNames-logdir=%{_var}/log/omninames

%make_build

%install
%make_install
# Avoid conflict with empty module marker from omniORB package
rm %{buildroot}%{python3_sitelib}/omniidl_be/{__init__.py,__pycache__/__init__.*}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc README* ReleaseNotes*
%doc doc/omniORBpy*
%{python3_sitearch}/
%{python3_sitelib}/

%files devel
%{_includedir}/*

%changelog
