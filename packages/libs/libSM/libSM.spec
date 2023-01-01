#
# spec file for package libSM
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


%define lname	libSM6
Name:           libSM
Version:        1.2.4
Release:        0
Summary:        X Session Management library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libSM
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libSM/
Source:         https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ice) >= 1.0.5
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)

%description
The X Session Management Protocol provides a uniform mechanism for
users to save and restore their sessions. A session is a group of X
clients (programs), each of which has a particular state. The session
is controlled by a network service called the session manager, which
issues commands to its clients on behalf of the user. These commands
may cause clients to save their state or to terminate. It is expected
that the client will save its state in such a way that the client can
be restarted at a later time and resume its operation as if it had
never been terminated.

%package -n %{lname}
Summary:        X Session Management library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libSM = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libSM < 7.6_%{version}-%{release}

%description -n %{lname}
The X Session Management Protocol provides a uniform mechanism for
users to save and restore their sessions. A session is a group of X
clients (programs), each of which has a particular state. The session
is controlled by a network service called the session manager, which
issues commands to its clients on behalf of the user. These commands
may cause clients to save their state or to terminate. It is expected
that the client will save its state in such a way that the client can
be restarted at a later time and resume its operation as if it had
never been terminated.

%package devel
Summary:        Development files for the X Session Management library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libSM-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libSM-devel < 7.6_%{version}-%{release}

%description devel
The X Session Management Protocol provides a uniform mechanism for
users to save and restore their sessions. A session is a group of X
clients (programs), each of which has a particular state. The session
is controlled by a network service called the session manager, which
issues commands to its clients on behalf of the user. These commands
may cause clients to save their state or to terminate. It is expected
that the client will save its state in such a way that the client can
be restarted at a later time and resume its operation as if it had
never been terminated.

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
%configure --docdir=%{_docdir}/%{name} --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libSM.so.6*

%files devel
%license COPYING
%doc README.md
%{_includedir}/X11/*
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%{_docdir}/%{name}

%changelog
