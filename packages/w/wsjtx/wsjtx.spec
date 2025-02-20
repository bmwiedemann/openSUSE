#
# spec file for package wsjtx
#
# Copyright (c) 2017 Walter Fey DL8FCL
# Copyright (c) 2024 Wojciech Kazubski <wk@ire.pw.edu.pl>
#
# This file is under MIT license

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#FIXME upstream fixing needed so lto can be re-enabled.
%define _lto_cflags %{nil}
Name:           wsjtx
Version:        2.7.0
Release:        0
Summary:        Weak signal hamradio software
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://wsjt.sourceforge.io/wsjtx.html
Source:         %{name}-%{version}.tar.xz
Source2:        wsjtx.rpmlintrc
Patch0:         reproducible.patch
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.7.2
BuildRequires:  dos2unix
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hamlib
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  pkgconfig(hamlib) >= 4.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_regex-devel
%endif

%description
WSJT-X implements communication protocols or "modes" called FST4, FST4W, FT4,
FT8, JT4, JT9, JT65, Q65, MSK144, and WSPR, as well as one called Echo for
detecting and measuring your own radio signals reflected from the Moon.
These modes were designed for making reliable, confirmed QSOs under extreme
weak-signal conditions.

%prep
%autosetup -p1

dos2unix AUTHORS
dos2unix BUGS
dos2unix NEWS
dos2unix README
dos2unix THANKS
dos2unix example_log_configurations/*

%build
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
%cmake \
    -DWSJT_GENERATE_DOCS=OFF
%cmake_build

%install
%cmake_install
rm %{buildroot}/%{_docdir}/%{name}/COPYING

%check
%ctest

%files
%license COPYING
%doc AUTHORS BUGS NEWS README THANKS
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}_icon.png
%{_datadir}/%{name}
%{_docdir}/%{name}/example_log_configurations
%{_mandir}/man1/*.1%{?ext_man}

%changelog
