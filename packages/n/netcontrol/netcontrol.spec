#
# spec file for package netcontrol
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           netcontrol
Version:        0.3.1
Release:        0
Summary:        A network configuration library
License:        LGPL-2.1+
Group:          Productivity/Networking/System
#
# License note:
# libnetcontrol contains source code which is based on wicked.
# Wicked is licensed under the GPL-2.0+, but permission has been
# granted by the authors of wicked to use the code derived from
# wicked under the LGPL-2.1+ in libnetcontrol.
#
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1310
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnl3-devel
BuildRequires:  libtool
%else
%if 0%{?suse_version} >= 1210
BuildRequires:  libnl-1_1-devel
%else
BuildRequires:  libnl-devel
%endif
%endif
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1230
Requires:       sysconfig >= 0.80.0
%else
Requires:       sysconfig >= 0.71.0
%endif

%description
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.



Authors:
--------
    Olaf Kirch <okir@suse.de>
    Marius Tomaschewski <mt@suse.de>

%package -n     libnetcontrol0

Summary:        A network configuration library
Group:          Productivity/Networking/System

%description -n libnetcontrol0
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.

The libnetcontrol0 package provides the shared library.



Authors:
--------
    Olaf Kirch <okir@suse.de>
    Marius Tomaschewski <mt@suse.de>

%package -n     libnetcontrol-devel

Summary:        Development header and library files
Group:          Development/Libraries/C and C++
Requires:       libnetcontrol0 = %{version}

%description -n libnetcontrol-devel
A interim network configuration library, currently implementing the
libnetcf interface for libvirt.

The libnetcontrol-devel package contains libraries and header files
required for development.



Authors:
--------
    Olaf Kirch <okir@suse.de>
    Marius Tomaschewski <mt@suse.de>

%prep
%setup -q

%build
export CFLAGS="-W -Wall $RPM_OPT_FLAGS"
%configure \
%if 0%{?suse_version} >= 1230
	--enable-network-service \
%endif
	--enable-pthreads \
	--disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_libdir}/pkgconfig
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n libnetcontrol0
/sbin/ldconfig

%postun -n libnetcontrol0
/sbin/ldconfig

%files -n libnetcontrol0
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n libnetcontrol-devel
%defattr(-,root,root,-)
%doc README COPYING.LGPL COPYING.GPL ChangeLog.git
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/netcontrol.pc

%changelog
