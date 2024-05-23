#
# spec file for package libcap-ng-python
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


%define sover  0
Name:           libcap-ng-python
Version:        0.8.5
Release:        0
Summary:        An alternate Linux/POSIX capabilities library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://people.redhat.com/sgrubb/libcap-ng
Source0:        https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  kernel-headers >= 2.6.11
BuildRequires:  libcap-ng-devel = %{version}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  swig

%description
libcap-ng is a library providing an alternate mechanism to libcap to
inspect and set Linux process and file capabilities (modeled upon a
withdrawn POSIX.1e draft).

%package -n python3-capng
Summary:        Python bindings for libcap-ng library
Group:          Development/Libraries/Python
Requires:       libcap-ng%{sover} = %{version}

%description -n python3-capng
The libcap-ng-python package contains the bindings so that libcap-ng
and can be used by Python applications.

%prep
%setup -q -n libcap-ng-%{version}

%build
%configure \
    --disable-static \
    --with-python3
make %{?_smp_mflags} PYTHON="python3"

%install
%make_install -C bindings/python3 PYTHON="python3"
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{python3_sitearch}

%files -n python3-capng
%pycache_only %{python3_sitearch}/__pycache__/capng*.pyc
%{python3_sitearch}/_capng.so
%{python3_sitearch}/capng.py

%changelog
