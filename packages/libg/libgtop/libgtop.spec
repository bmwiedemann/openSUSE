#
# spec file for package libgtop
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


%define sover 11
Name:           libgtop
Version:        2.41.3+4
Release:        0
Summary:        System status information library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://developer.gnome.org/libgtop/stable/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  util-linux-systemd
BuildRequires:  pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.26.0
BuildRequires:  pkgconfig(xau)
PreReq:         permissions

%description
A library that fetches information about the running system, such as
CPU and memory usage and active processes.

On Linux systems, this information is taken directly from the /proc
file system. On other systems, a server is used to read information
from /dev/kmem.

%package -n libgtop-2_0-%{sover}
Summary:        System status information library
Group:          System/Libraries
# Needed to make lang package installable
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
#

%description -n libgtop-2_0-%{sover}
A library that fetches information about the running system, such as
CPU and memory usage and active processes.

On Linux systems, this information is taken directly from the /proc
file system. On other systems, a server is used to read information
from /dev/kmem.

%package -n typelib-1_0-GTop-2_0
Summary:        Introspection bindings for libgtop
Group:          System/Libraries

%description -n typelib-1_0-GTop-2_0
A library that fetches information about the running system, such as
CPU and memory usage and active processes.

On Linux systems, this information is taken directly from the /proc
file system. On other systems, a server is used to read information
from /dev/kmem.

This package provides the GObject Introspection bindings for libgtop.

%package devel
Summary:        Development files for libgtop
Group:          Development/Libraries/GNOME
Requires:       libgtop-2_0-%{sover} = %{version}
Requires:       typelib-1_0-GTop-2_0 = %{version}
# FIXME: use proper Requires(pre/post/preun/...)
#
PreReq:         %{install_info_prereq}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        Documentation for the libgtop library
Group:          Development/Libraries/GNOME
Requires:       libgtop-2_0-%{sover} = %{version}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         /sbin/install-info
BuildArch:      noarch

%description doc
A library that fetches information about the running system, such as
CPU and memory usage and active processes.

On Linux systems, this information is taken directly from the /proc
file system. On other systems, a server is used to read information
from /dev/kmem.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure\
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%ldconfig_scriptlets -n libgtop-2_0-%{sover}

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}2.info.gz

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}2.info.gz

%post
%set_permissions /usr/libexec/libgtop_server2

%verifyscript
%verify_permissions -e /usr/libexec/libgtop_server2

%files lang -f %{name}.lang

%files
%{_libexecdir}/libgtop_server2
%{_libexecdir}/libgtop_daemon2

%files -n libgtop-2_0-%{sover}
%license COPYING
%doc AUTHORS NEWS README copyright.txt
%{_libdir}/*.so.*

%files -n typelib-1_0-GTop-2_0
%{_libdir}/girepository-1.0/GTop-2.0.typelib

%files devel
%{_includedir}/libgtop-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GTop-2.0.gir

%files doc
%{_infodir}/*.info*

%changelog
