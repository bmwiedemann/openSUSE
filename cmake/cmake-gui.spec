#
# spec file for package cmake-gui
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shortversion 3.14
# exclude for SLE 12 and Leap 42.x
%if 0%{?suse_version} == 1315
%define system_libuv OFF
%else
%define system_libuv ON
BuildRequires:  libuv-devel >= 1.10
%endif
Name:           cmake-gui
Version:        3.14.5
Release:        0
Summary:        CMake graphical user interface
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://www.cmake.org/
Source0:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}.tar.gz
Source5:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt
Source6:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt.asc
Source7:        cmake.keyring
# PATCH-FIX-UPSTREAM form.patch -- set the correct include path for the ncurses includes
Patch4:         form.patch
# PATCH-FIX-UPSTREAM system-libs.patch -- allow choosing between bundled and system jsoncpp & form libs
Patch5:         system-libs.patch
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel >= 3.0.2
BuildRequires:  libexpat-devel
BuildRequires:  openssl-devel
# this is commented as it would create dependancy cycle between jsoncpp and cmake
#if 0%{?suse_version} > 1320
#BuildRequires:  pkgconfig(jsoncpp)
#endif
BuildRequires:  pkgconfig
BuildRequires:  python-sphinx
BuildRequires:  rhash-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
Requires:       cmake
Recommends:     cmake-man

%description
This is a Graphical User Interface for CMake, a cross-platform,
open-source build system.

%package -n cmake-man
Summary:        Cross-platform, open-source make system - manual pages
Group:          Development/Tools/Building

%description -n cmake-man
Manual pages for cmake, Cross-platform, open-source make system

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep cmake-%{version}.tar.gz %{SOURCE5} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%setup -q -n cmake-%{version}
%patch4 -p1
%patch5 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# This is not autotools configure
./configure \
    --prefix=%{_prefix} \
    --datadir=/share/cmake \
    --docdir=/share/doc/packages/cmake \
    --mandir=/share/man \
    --sphinx-man \
    --system-libs \
    --no-system-jsoncpp \
    --parallel=0%{jobs} \
    --verbose \
    --qt-gui \
    -- \
    -DCMAKE_USE_SYSTEM_LIBRARY_LIBUV=%{system_libuv}
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/cmake
%suse_update_desktop_file  -r %{name} CMake Development IDE Tools Qt

# delete files that belong to the 'cmake' package
rm -rf %{buildroot}%{_bindir}/{cpack,cmake,ctest}
rm -rf %{buildroot}%{_datadir}/cmake
rm -rf %{buildroot}%{_datadir}/aclocal/cmake.m4
rm -rf %{buildroot}%{_docdir}/cmake

%files
%license Copyright.txt
%{_bindir}/cmake-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/cmakecache.xml
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/*
%{_datadir}/icons/hicolor/128x128/apps/CMakeSetup.png
%{_datadir}/icons/hicolor/32x32/apps/CMakeSetup.png

%files -n cmake-man
%license Copyright.txt
%{_mandir}/man7/*
%{_mandir}/man1/*

%changelog
