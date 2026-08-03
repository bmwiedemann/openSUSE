# spec file for package libzpc-legacy
#
# Copyright (c) 2026 SUSE LLC
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

Name:           libzpc-legacy
Version:        1.5.0
Release:        0
Summary:        IBM Z Protected-key Crypto library (Legacy 1.x branch)
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/libzpc
Source:         https://github.com/opencryptoki/libzpc/archive/refs/tags/v%{version}.tar.gz#/libzpc-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjson-c-devel
BuildRequires:  texlive-bibtex-bin
ExclusiveArch:  s390x

%description
This is the legacy 1.x branch of the IBM Z Protected-key Crypto library,
retained for compatibility with applications built against the 1.x API.

%package -n libzpc1
Summary:        IBM Z Protected-key Crypto library
Group:          System/Libraries

%description -n libzpc1
This package contains the shared library to work with the
IBM protected-key cryptography hardware.

%package devel
Summary:        Header files for the IBM Z Protected-key Crypto library
Group:          Productivity/Security
Requires:       libzpc1 = %{version}-%{release}
Provides:       libzpc-devel = %{version}-%{release}
Obsoletes:      libzpc-devel < %{version}-%{release}

%description devel
This package provides the header files and symbolic link to the
shared library for the libzpc RPM.

%prep
%autosetup -p1 -n libzpc-%{version}

%build
%cmake -DBUILD_DOC=ON
%make_build

%install
cd build
%make_install

%post -n libzpc1 -p /sbin/ldconfig

%postun -n libzpc1 -p /sbin/ldconfig

%files -n libzpc1
%doc README.md
%license LICENSE
%{_libdir}/libzpc.so.1
%{_libdir}/libzpc.so.%{version}

%files devel
%dir %{_includedir}/zpc
%{_includedir}/zpc/*.h
%{_libdir}/libzpc.so
%{_libdir}/pkgconfig/libzpc.pc

%changelog
