#
# spec file for package ldmtool
#
# Copyright (c) 2020 SUSE LLC
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


%define srcname libldm
%define sover  1_0-0

Name:           ldmtool
Version:        0.2.4
Release:        0
Summary:        A tool to manage Windows dynamic disks
License:        GPL-3.0-only
Group:          System/Base

URL:            https://github.com/mdbooth/libldm 
# Disable until the create a tarball with the 2.4.0 release
#Source0:        %{url}/downloads/%{srcname}-%{version}.tar.gz
Source0:        %{srcname}-%{version}.tar.gz
Patch0:         Remove-deprecated-g_type_class_add_private.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  device-mapper-devel >= 1.0
BuildRequires:  glib2-devel >= 2.38.0
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel >= 0.14.0
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel

Requires:       %{srcname}-%{sover} = %{version}-%{release}

%description
Command-line tool for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted.

%package    -n  %{srcname}-%{sover}
Summary:        Library to manage Windows dynamic disks
License:        LGPL-3.0-only
Group:          System/Libraries

%description -n %{srcname}-%{sover}
Library for managing Microsoft Windows dynamic disks, which use Microsoft's
LDM metadata. It can inspect them, and also create and remove device-mapper
block devices which can be mounted.


%package        -n %{srcname}-%{sover}-devel
Summary:        Development files for %{name}
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       %{srcname}-%{sover} = %{version}-%{release}

%description    -n %{srcname}-%{sover}-devel
Contains libraries and header files for developing applications using
%{srcname}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
gtkdocize
autoreconf -fiv
%configure --disable-static --enable-gtk-doc
%make_build

%install
%make_install
find "%buildroot" -type f -name '*.la' -delete

%post -n %{srcname}-%{sover} -p /sbin/ldconfig

%postun -n %{srcname}-%{sover} -p /sbin/ldconfig

%files
%license COPYING.gpl
%{_bindir}/ldmtool
%{_mandir}/man1/ldmtool.1.gz

%files -n %{srcname}-%{sover}
%license COPYING.lgpl
%{_libdir}/*.so.*

%files -n %{srcname}-%{sover}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ldm-1.0.pc
%{_datadir}/gtk-doc

%changelog
