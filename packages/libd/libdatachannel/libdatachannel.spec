#
# spec file for package libdatachannel
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


#%%define soversion() %%(echo "%%{1}" | awk -F. '{print $1"."$2}')
%define son 24
%define soversion 0_%{son}
%define libname %{name}%{soversion}
Name:           libdatachannel
Version:        0.24.1
Release:        0
Summary:        WebRTC network library featuring Data Channels, Media Transport, and WebSockets
License:        MPL-2.0
URL:            https://libdatachannel.org/
Group:          Development/Libraries/C and C++
Source0:        https://github.com/paullouisageneau/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(plog)
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
# Not yet needed and not packaged in openSUSE yet
#BuildRequires:  cmake(LibJuice)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(nice)
BuildRequires:  pkgconfig(nlohmann_json) >= 3
%if 0%{?suse_version} < 1600
BuildRequires:  usrsctp-devel
%else
BuildRequires:  pkgconfig(usrsctp)
%endif

%description
libdatachannel is a standalone implementation of WebRTC Data Channels,
WebRTC Media Transport, and WebSockets in C++17 with C bindings for POSIX platforms
(including GNU/Linux, Android, FreeBSD, Apple macOS and iOS) and Microsoft Windows.

%package -n	%{libname}
Summary:        C++ library for %{name}
Group:          System/Libraries

%description -n	%{libname}
libdatachannel is a standalone implementation of WebRTC Data Channels,
WebRTC Media Transport, and WebSockets in C++17 with C bindings for POSIX platforms
(including GNU/Linux, Android, FreeBSD, Apple macOS and iOS) and Microsoft Windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%cmake -DPREFER_SYSTEM_LIB=ON -DUSE_GNUTLS=ON -DUSE_NICE=ON
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/%{name}.so.*.%{son}*

%files devel
%doc README.md DOC.md
%{_includedir}/rtc/
%{_libdir}/cmake/LibDataChannel/
%{_libdir}/%{name}.so

%changelog
