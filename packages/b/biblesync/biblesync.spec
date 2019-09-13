#
# spec file for package biblesync
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%define _soversion 2.0
%define _shlibname libbiblesync2_0

Name:           biblesync
Version:        2.0.1
Release:        0
Summary:        A library for sharing Bible navigation
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Url:            https://github.com/karlkleinpaste/biblesync
Source0:        https://github.com/karlkleinpaste/biblesync/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config

%description
BibleSync is a multicast protocol to support Bible software shared
co-navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

%package -n %{_shlibname}
Summary:        A library for sharing Bible navigation 
Group:          System/Libraries

%description -n %{_shlibname}
BibleSync is a multicast protocol to support Bible software shared
co- navigation. It uses LAN multicast in either a personal/small team
mutual navigation motif or in a classroom environment where there are
Speakers plus the Audience. It provides a complete yet minimal public
interface to support mode setting, setup for packet reception,
transmit on local navigation, and handling of incoming packets.

This library is not specific to any particular Bible software
framework, completely agnostic as to structure of layers above
BibleSync.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{_shlibname} = %{version}-%{release}
Requires:       libuuid-devel

%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake -DLIBDIR=%{_libdir} .. -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" -DBIBLESYNC_SOVERSION=%{_soversion}
make %{?_smp_mflags}

%install
%cmake_install DESTDIR=%{buildroot}

%post -n %{_shlibname} -p /sbin/ldconfig

%postun -n %{_shlibname} -p /sbin/ldconfig

%files -n %{_shlibname}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libbiblesync.so.%{_soversion}

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.md WIRESHARK
%{_includedir}/biblesync
%{_libdir}/pkgconfig/biblesync.pc
%{_libdir}/libbiblesync.so
%{_mandir}/man7/biblesync.7*

%changelog
