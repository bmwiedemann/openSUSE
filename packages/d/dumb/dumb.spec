#
# spec file for package dumb
#
# Copyright (c) 2021 SUSE LLC
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


%define sover   2
Name:           dumb
Version:        2.0.3
Release:        0
Summary:        Dynamic Universal Music Bibliotheque
License:        Zlib
Group:          Productivity/Multimedia/Other
URL:            https://github.com/kode54/dumb
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        license-clarification.eml
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(argtable2)
BuildRequires:  pkgconfig(sdl2)

%description
DUMB is a module audio renderer library.
It reads module files and outputs audio that can be dumped
to the actual audio playback library.

%package -n lib%{name}%{sover}
Summary:        Tracker module player library
Group:          System/Libraries

%description -n lib%{name}%{sover}
DUMB is a module audio renderer library.
It reads module files and outputs audio that can be dumped
to the actual audio playback library.

This package contains the shared libraries for dumb.

%package devel
Summary:        Development libraries and headers for libdumb
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Suggests:       %{name}-devel-doc

%description devel
The development files that must be installed in order to compile
applications which use libdumb.

%package devel-doc
Summary:        Doc Package for Dumb
Group:          Documentation/Other
Suggests:       %{name} = %{version}

%description devel-doc
DUMB is a module audio renderer library.
It reads module files and outputs audio that can be dumped
to the actual audio playback library.

This package contains the docs for dumb.

%prep
%setup -q

%build
%cmake -DBUILD_ALLEGRO4=OFF
%cmake_build

%install
%cmake_install

%post -n libdumb%{sover} -p /sbin/ldconfig
%postun -n libdumb%{sover} -p /sbin/ldconfig

%files
%{_bindir}/%{name}out
%{_bindir}/%{name}play

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/dumb.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/dumb.pc

%files devel-doc
%doc README.md UPDATING_YOUR_PROJECTS.md DUMBFILE_SYSTEM.md CHANGELOG.md
%doc examples

%changelog
