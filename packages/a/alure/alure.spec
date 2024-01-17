#
# spec file for package alure
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


%define sover 1

Name:           alure
Version:        1.2
Release:        0
Summary:        Audio Library Tools REloaded
# ALURE code is LGPL-2.0+; note -devel subpackage has its own license tag
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://kcat.tomasu.net/alure.html
Source0:        https://kcat.tomasu.net/alure-releases/%{name}-%{version}.tar.bz2
Patch0:         fix-cmake_minimum_required.patch
Patch1:         fix-missing-include.patch
Patch2:         fix-lib-suffix.patch
Patch3:         fix-link-flac.patch
Patch4:         fix-FLUIDSYNTH_CFLAGS.patch
Patch5:         fix-dumb2.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dumb)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)

%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package -n lib%{name}%{sover}
Summary:        Utility library around OpenAL
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n lib%{name}%{sover}
ALURE is a utility library to help manage common tasks with OpenAL
applications.

%package devel
Summary:        Development files for %{name}
# Devel doc includes some files under GPLv2+ from NaturalDocs
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
	-DBUILD_STATIC=OFF	\
	-DDYNLOAD=OFF		\
	-DMPG123=ON		\
	-DMODPLUG=ON
%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print

# remove installed html doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}/html
# fix encoding
sed -i 's/\r$//' docs/html/javascript/main.js docs/html/styles/1.css

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/alure{cdplay,play,stream}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%doc docs/html examples
%{_includedir}/AL
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
