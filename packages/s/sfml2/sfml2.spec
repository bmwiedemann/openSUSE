#
# spec file for package sfml2
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


%define so_ver -2_5
Name:           sfml2
Version:        2.5.1
Release:        0
Summary:        C++ multimedia library with access to input, sound and display
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.sfml-dev.org/
Source0:        https://github.com/SFML/SFML/archive/%{version}/SFML-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
Requires:       lib%{name}%{so_ver} = %{version}

%description
SFML is a multimedia API that provides access to graphics, input,
audio, etc. similar to SDL.

%package -n lib%{name}%{so_ver}
Summary:        Free multimedia C++ API
Group:          System/Libraries

%description -n lib%{name}%{so_ver}
SFML is a multimedia API that provides access to graphics, input,
audio, etc., and may be seen as an object-oriented alternative to
SDL. It can be used as a minimal windowing system to interface with
OpenGL, or as a multimedia library for building games and interactive
programs.

%package devel
Summary:        SFML development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       pkgconfig(gl)
# Conflict with the sfml 1 devel package(same include files)
Conflicts:      sfml-devel

%description devel
SFML is a C++ multimedia API that provides a low and high-level
access to graphics, input, audio, etc., and may be seen as an
object-oriented alternative to SDL. SFML can be used as a minimal
windowing system to interface with OpenGL, or as a multimedia library
for building games or interactive programs.

This subpackage provides the header files needed to build SFML
programs.

%package doc
Summary:        SFML developer documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
SFML is a multimedia API that provides access to graphics, input,
audio, etc. similar to SDL.

This subpackage contains the developer documentation.

%prep
%setup -q -n SFML-%{version}

%build
%cmake -DSFML_BUILD_DOC=TRUE \
       -DSFML_INSTALL_PKGCONFIG_FILES=TRUE \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
make VERBOSE=1 %{?_smp_mflags}

cd doc/html
%fdupes -s .

%install
%cmake_install

# Remove doc from wrong location
rm -r %{buildroot}%{_datadir}/SFML/doc
rm %{buildroot}%{_datadir}/SFML/*.md

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files -n lib%{name}%{so_ver}
%license license.md
%{_libdir}/libsfml-*.so.*

%files devel
%doc readme.md changelog.md
%{_includedir}/SFML
%{_libdir}/libsfml-*.so
%{_libdir}/pkgconfig/sfml-*.pc
%{_libdir}/cmake/SFML
%{_datadir}/SFML/

%files doc
%doc build/doc/html/* CONTRIBUTING.md

%changelog
