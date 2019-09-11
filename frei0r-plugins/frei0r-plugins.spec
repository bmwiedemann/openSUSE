#
# spec file for package frei0r-plugins
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           frei0r-plugins
Version:        1.6.1
Release:        0
Summary:        Collection of video sources and filters plugins
# Upstream says 2.0+ but quite few of their plugins are GPL-3.0+
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://frei0r.dyne.org/
Source0:        http://files.dyne.org/frei0r/releases/frei0r-plugins-%{version}.tar.gz
# PATCH-FIX-UPSTREAM frei0r-plugins-1.4-missing_include.patch http://www.piksel.no/projects/frei0r/ticket/41 reddwarf@opensuse.org -- Add missing header
Patch0:         frei0r-plugins-1.4-missing_include.patch
# PATCH-FIX-UPSTREAM frei0r-plugins-openCV-3.0-compatibility.patch  tittiatcoke@gmail.com -- Make it compile with openCV3. This is a rebase of the two usptream commits by Dan Dennedy
Patch1:         frei0r-plugins-openCV-3.0-compatibility.patch
# PATCH-FIX-UPSTREAM frei0r-plugins-openCV-3.4.2-compatibility.patch -- Fix build with opencv > 3.4.1
Patch2:         frei0r-plugins-openCV-3.4.2-compatibility.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.0.0
BuildRequires:  pkgconfig(gavl) >= 0.2.3
BuildRequires:  pkgconfig(opencv)

%description
This package provides a collection of video sources and filters plugins,
using the Frei0r API.

%package opencv
Summary:        OpenCV video sources and filters plugins
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{name} = %{version}-%{release}

%description opencv
These plugins may cause slow exports due to multiprocessing issues
in kdenlive and shotcut. plugins facebl0r and facedetect.
See boo#1068792

%package devel
Summary:        Frei0r plugin API for video sources and filters
Group:          Development/Libraries/C and C++

%description devel
Frei0r is a minimalistic plugin API for video sources and filters. The
behaviour of the effects can be controlled from the host by simple
parameters. The intent is to solve the recurring reimplementation or
adaptation issue of standard effects.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/doc/frei0r-plugins/{AUTHORS.txt,ChangeLog.txt,README.txt,TODO.txt}

%files
%license COPYING.txt
%doc AUTHORS.txt ChangeLog.txt README.txt
%{_libdir}/frei0r-1/
%exclude %{_libdir}/frei0r-1/facebl0r.so
%exclude %{_libdir}/frei0r-1/facedetect.so

%files opencv
%license COPYING.txt
%dir %{_libdir}/frei0r-1
%{_libdir}/frei0r-1/facebl0r.so
%{_libdir}/frei0r-1/facedetect.so

%files devel
%{_libdir}/pkgconfig/frei0r.pc
%{_includedir}/frei0r.h

%changelog
