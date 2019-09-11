#
# spec file for package alure
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 openSUSE_user1
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


Name:           alure
Version:        1.2
Release:        0
Summary:        Audio Library Tools REloaded
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
# ALURE code is LGPL-2.0+; note -devel subpackage has its own license tag
Url:            http://kcat.strangesoft.net/alure.html
Source0:        http://kcat.strangesoft.net/%{name}-releases/%{name}-%{version}.tar.bz2
# patch for build with gcc47
Patch0:         alure-gcc47.patch
BuildRequires:  cmake
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  libdumb-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
# Devel doc includes some files under GPLv2+ from NaturalDocs
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libalure1
Summary:        Utility library around OpenAL
License:        LGPL-2.0-or-later
Group:          System/Libraries

%description -n libalure1
ALURE is a utility library to help manage common tasks with OpenAL
applications.

%prep
%setup -q
%patch0

%build
%cmake -DBUILD_STATIC=OFF -DMPG123=OFF -DMODPLUG=ON
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
find %{buildroot} -name '*.la' -type f -delete
# remove installed html doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}/html

# fix encoding
sed -i 's/\r$//' docs/html/javascript/main.js docs/html/styles/1.css

%post   -n libalure1 -p /sbin/ldconfig
%postun -n libalure1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/alure*

%files -n libalure1
%defattr(-,root,root)
%{_libdir}/libalure.so.*

%files devel
%defattr(-,root,root,-)
%doc docs/html examples
%{_includedir}/AL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
