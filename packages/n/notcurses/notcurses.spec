#
# spec file for package notcurses
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%global sover   1
Name:           notcurses
Version:        1.6.19
Release:        0
Summary:        Character graphics and TUI library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://nick-black.com/dankwiki/index.php/Notcurses
#Git-Clone:     https://github.com/dankamongmen/notcurses.git
Source:         https://github.com/dankamongmen/notcurses/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  QR-Code-generator-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libunistring-devel
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-pypandoc
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libavcodec) >= 57.0
BuildRequires:  pkgconfig(libavutil) >= 56.0
BuildRequires:  pkgconfig(libavformat) >= 57.0
BuildRequires:  pkgconfig(libswscale) >= 5.0
BuildRequires:  pkgconfig(tinfo) >= 6.1

%description
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

%package -n libnotcurses%{sover}
Summary:        Character graphics and TUI library
Group:          System/Libraries

%description -n libnotcurses%{sover}
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains shared library part of libnotcurses.

%package -n libnotcurses++%{sover}
Summary:        Character graphics and TUI library
Group:          System/Libraries

%description -n libnotcurses++%{sover}
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains shared library part of libnotcurses++.

%package -n notcurses-devel
Summary:        Development files for notcurses
Group:          Development/Libraries/C and C++
Requires:       libnotcurses%{sover} = %{version}

%description -n notcurses-devel
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains libraries and header files for developing
applications that want to make use of libnotcurses.

%package -n notcurses++-devel
Summary:        Development files for notcurses++
Group:          Development/Libraries/C and C++
Requires:       libnotcurses++%{sover} = %{version}

%description -n notcurses++-devel
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains libraries and header files for developing
applications that want to make use of libnotcurses.

%package demos
Summary:        Character graphics and TUI library demos
Group:          Development/Libraries/C and C++

%description demos
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains the demo binaries for the notcurses
library.

%package -n python3-notcurses
Summary:        Python3 bindings for the notcurses library
Group:          Development/Languages/Python

%description -n python3-notcurses
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains the python3 bindings for the notcurses
library.

%prep
%setup -q
sed -e '/^#!\//, 1d' -i python/src/notcurses/notcurses.py

%build
%cmake -DUSE_DOCTEST=OFF -DUSE_STATIC=OFF
%make_build
cd ../python
export CFLAGS="%optflags -I../include -L../build"
%python3_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/notcurses/
cd python
%python3_install
%fdupes %{buildroot}/%{python3_sitearch}


%post   -n libnotcurses%{sover} -p /sbin/ldconfig
%postun -n libnotcurses%{sover} -p /sbin/ldconfig
%post   -n libnotcurses++%{sover} -p /sbin/ldconfig
%postun -n libnotcurses++%{sover} -p /sbin/ldconfig

%files -n libnotcurses%{sover}
%license LICENSE
%doc NEWS.md OTHERS.md README.md TERMS.md USAGE.md
%{_libdir}/libnotcurses.so.%{sover}*

%files -n libnotcurses++%{sover}
%{_libdir}/libnotcurses++.so.%{sover}*

%files demos
%{_bindir}/ncneofetch
%{_bindir}/notcurses-demo
%{_bindir}/notcurses-input
%{_bindir}/notcurses-ncreel
%{_bindir}/notcurses-tetris
%{_bindir}/notcurses-view
%{_mandir}/man1/notcurses-demo.1%{?ext_man}
%{_mandir}/man1/notcurses-input.1%{?ext_man}
%{_mandir}/man1/notcurses-ncreel.1%{?ext_man}
%{_mandir}/man1/notcurses-tester.1%{?ext_man}
%{_mandir}/man1/notcurses-tetris.1%{?ext_man}
%{_mandir}/man1/notcurses-view.1%{?ext_man}
%{_mandir}/man1/ncneofetch.1%{?ext_man}
%{_datadir}/notcurses/

%files -n notcurses-devel
%{_includedir}/notcurses
%{_libdir}/libnotcurses.so
%{_libdir}/pkgconfig/notcurses.pc
%dir %{_libdir}/cmake/notcurses
%{_libdir}/cmake/notcurses/notcursesConfig.cmake
%{_libdir}/cmake/notcurses/notcursesConfigVersion.cmake
%{_mandir}/man3/*.3%{?ext_man}

%files -n notcurses++-devel
%{_includedir}/ncpp
%{_libdir}/libnotcurses++.so
%{_libdir}/pkgconfig/notcurses++.pc

%files -n python3-notcurses
%{_bindir}/notcurses-pydemo
%{_mandir}/man1/notcurses-pydemo.1%{?ext_man}
%{python3_sitearch}/*

%changelog
