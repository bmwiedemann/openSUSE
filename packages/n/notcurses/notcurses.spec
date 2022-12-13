#
# spec file for package notcurses
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2022, Martin Hauke <mardnh@gmx.de>
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


%global sover   3
%ifarch %{ix86} %{arm}
%bcond_with  pandoc
%else
%bcond_without  pandoc
%endif
Name:           notcurses
Version:        3.0.9
Release:        0
Summary:        Character graphics and TUI library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://nick-black.com/dankwiki/index.php/Notcurses
#Git-Clone:     https://github.com/dankamongmen/notcurses.git
Source:         https://github.com/dankamongmen/notcurses/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# default openSUSE ffmpeg can't play the codec used in the xray demo
Patch:          notcurses-3.0.8-skip-xray.diff
BuildRequires:  QR-Code-generator-devel
BuildRequires:  cmake
BuildRequires:  doctest-devel >= 2.3.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libavcodec) >= 57.0
BuildRequires:  pkgconfig(libavformat) >= 57.0
BuildRequires:  pkgconfig(libavutil) >= 56.0
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(libswscale) >= 5.0
BuildRequires:  pkgconfig(readline) >= 8.0
BuildRequires:  pkgconfig(tinfo) >= 6.1
BuildRequires:  pkgconfig(zlib)
%if %{with pandoc}
BuildRequires:  python3-pypandoc
%endif
BuildRequires:  qrcodegen-devel

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

%package -n libnotcurses-ffi%{sover}
Summary:        Character graphics and TUI library (FFI version)
Group:          System/Libraries

%description -n libnotcurses-ffi%{sover}
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains shared library part of libnotcurses (FFI
version).

%package -n libnotcurses-core%{sover}
Summary:        Character graphics and TUI library
Group:          System/Libraries

%description -n libnotcurses-core%{sover}
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains shared library part of libnotcurses-core.

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

%package -n notcurses-core-devel
Summary:        Development files for notcursescore
Group:          Development/Libraries/C and C++
Requires:       libnotcurses-core%{sover} = %{version}

%description -n notcurses-core-devel
notcurses facilitates the creation of modern TUI programs, making
full use of Unicode and 24-bit TrueColor. Its API is similar
to that of NCURSES, but extends that with z-buffering, rendering
of images and video using ffmpeg, alpha blending, widgets, palette
fades, resize awareness, and multithreading support.

This subpackage contains libraries and header files for developing
applications that want to make use of libnotcurses-core.

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
%autosetup -p1
#sed -e '/^#!\//, 1d' -i python/src/notcurses/notcurses.py

%build
%cmake -DUSE_DOCTEST=OFF -DUSE_STATIC=OFF \
     -DDFSG_BUILD=ON \
     -DUSE_QRCODEGEN=ON \
%if %{with pandoc}
     -DUSE_PANDOC=ON
%else
     -DUSE_PANDOC=OFF
%endif
%make_build
cd ../python
export CFLAGS="%{optflags} -I../include -L../build"
%python3_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/notcurses/
cd python
%python3_install
%fdupes %{buildroot}/%{python3_sitearch}

%post   -n libnotcurses%{sover} -p /sbin/ldconfig
%postun -n libnotcurses%{sover} -p /sbin/ldconfig
%post   -n libnotcurses-core%{sover} -p /sbin/ldconfig
%postun -n libnotcurses-core%{sover} -p /sbin/ldconfig
%post   -n libnotcurses++%{sover} -p /sbin/ldconfig
%postun -n libnotcurses++%{sover} -p /sbin/ldconfig

%check
cd build
# FIXME: fails in build env
%make_build test || :

%files -n libnotcurses%{sover}
%license COPYRIGHT
%{_libdir}/libnotcurses.so.%{sover}*

%files -n libnotcurses-core%{sover}
%{_libdir}/libnotcurses-core.so.%{sover}*

%files -n libnotcurses++%{sover}
%{_libdir}/libnotcurses++.so.%{sover}*

%files -n libnotcurses-ffi%{sover}
%{_libdir}/libnotcurses-ffi.so.%{sover}*

%files demos
%doc NEWS.md README.md USAGE.md
%{_bindir}/ncls
%{_bindir}/ncneofetch
%{_bindir}/notcurses-demo
%{_bindir}/notcurses-info
%{_bindir}/notcurses-input
%{_bindir}/nctetris
%{_bindir}/ncplayer
%{_bindir}/tfman
%if %{with pandoc}
%{_mandir}/man1/notcurses-demo.1%{?ext_man}
%{_mandir}/man1/notcurses-info.1%{?ext_man}
%{_mandir}/man1/notcurses-input.1%{?ext_man}
%{_mandir}/man1/nctetris.1%{?ext_man}
%{_mandir}/man1/ncplayer.1%{?ext_man}
%{_mandir}/man1/ncls.1%{?ext_man}
%{_mandir}/man1/ncneofetch.1%{?ext_man}
%{_mandir}/man1/tfman.1.gz
%endif
%{_datadir}/notcurses/

%files -n notcurses-core-devel
%{_libdir}/libnotcurses-core.so
%{_libdir}/pkgconfig/notcurses-core.pc
%dir %{_libdir}/cmake/NotcursesCore
%{_libdir}/cmake/NotcursesCore/NotcursesCoreConfig.cmake
%{_libdir}/cmake/NotcursesCore/NotcursesCoreConfigVersion.cmake

%files -n notcurses-devel
%{_includedir}/notcurses
%{_libdir}/libnotcurses.so
%{_libdir}/libnotcurses-ffi.so
%{_libdir}/pkgconfig/notcurses.pc
%{_libdir}/pkgconfig/notcurses-ffi.pc
%dir %{_libdir}/cmake/Notcurses
%{_libdir}/cmake/Notcurses/NotcursesConfig.cmake
%{_libdir}/cmake/Notcurses/NotcursesConfigVersion.cmake
%if %{with pandoc}
%{_mandir}/man3/*.3%{?ext_man}
%endif

%files -n notcurses++-devel
%{_includedir}/ncpp
%{_libdir}/libnotcurses++.so
%{_libdir}/pkgconfig/notcurses++.pc
%dir %{_libdir}/cmake/Notcurses++
%{_libdir}/cmake/Notcurses++/Notcurses++Config.cmake
%{_libdir}/cmake/Notcurses++/Notcurses++ConfigVersion.cmake

%files -n python3-notcurses
%{python3_sitearch}/*

%changelog
