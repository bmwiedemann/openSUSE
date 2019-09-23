#
# spec file for package clanlib
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


%define clan_ver 2.3

Name:           clanlib
Version:        2.3.6
Release:        0
Summary:        A Portable Interface for Writing Games
License:        Zlib
Group:          System/Libraries
Url:            http://www.clanlib.org/
Source:         ClanLib-%{version}.tgz
# PATCH-FIX-UPSTREAM -- fix compilation with new Mesa, coolo@suse.de
Patch0:         ClanLib-2.3.6-fix-opengl.patch
# PATCH-FIX-UPSTREAM -- Use cpuid only on x86, schwab@suse.de
Patch1:         clanlib-cpuid.patch
# Use std=gnu++11 option for ppc64le
Patch2:         stdgnu++11.patch
Patch3:         clanlib-alsa.patch
BuildRequires:  alsa-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxslt
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ClanLib delivers a platform-independent interface for writing games.

%package        devel
Summary:        A portable interface for writing games
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
#wants compiler intrinsics in installed headers
Requires:       c++_compiler
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)

%description     devel
ClanLib delivers a platform independent interface to write games with.

%prep
%autosetup -p1 -n ClanLib-%{version}

%build
%configure --with-pic --disable-static --disable-docs
make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING CREDITS README
%{_libdir}/libclan*.so.*

%files devel
%defattr(-, root, root)
%doc CODING_STYLE PATCHES
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libclan*.so

%changelog
