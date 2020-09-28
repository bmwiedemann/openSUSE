#
# spec file for package mediastreamer2
#
# Copyright (c) 2020 SUSE LLC
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


%define sobase  libmediastreamer
%define sover   11
Name:           mediastreamer2
Version:        4.4.2
Release:        0
Summary:        Audio/Video real-time streaming
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/technical-corner/mediastreamer2/overview
Source:         https://github.com/BelledonneCommunications/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch0:         mediastreamer2-fix-pkgconfig.patch
BuildRequires:  bcmatroska2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libgsm-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsrtp-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  spandsp-devel
BuildRequires:  sqlite3-devel
BuildRequires:  vim
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0
BuildRequires:  pkgconfig(libbcg729)
BuildRequires:  pkgconfig(libbzrtp) >= 1.0.6
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(ortp) >= 1.0.2
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
%if 0%{?suse_version} >= 1500
BuildRequires:  libjpeg-devel
%endif
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libswscale) >= 0.7.0

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package -n %{sobase}%{sover}
Summary:        Audio/video real-time streaming library, base part
Group:          System/Libraries

%description -n %{sobase}%{sover}
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package doc
Summary:        Documentation for the mediastreamer2 library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the ortp library.

This package contains documentation files

%package devel
Summary:        Headers and libraries for the mediastreamer2 library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{sobase}%{sover} = %{version}
Requires:       bcmatroska2-devel

%description devel
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the ortp library.

This package contains header files and development libraries needed to
develop programs using the mediastreamer2 library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
export CFLAGS="%(echo %{optflags}) -fcommon -Wno-implicit-function-declaration"
export CXXFLAGS="$CFLAGS"
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="-flto=auto -Wl,--as-needed -Wl,-z,now" \
    -DENABLE_STATIC=NO
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -T %{buildroot}%{_datadir}/doc/%{name}-4.4.0/ \
  %{buildroot}%{_docdir}/%{name}/

%post -n %{sobase}%{sover} -p /sbin/ldconfig

%postun -n %{sobase}%{sover} -p /sbin/ldconfig

%files
%license LICENSE.txt 
%{_bindir}/mediastream
%{_bindir}/mkvstream

%files -n %{sobase}%{sover}
%{_libdir}/%{sobase}.so.%{sover}*

%files doc
%doc README.md
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/*
%dir %{_datadir}/images/
%{_datadir}/images/nowebcamCIF.jpg

%files devel
%{_includedir}/mediastreamer2/
%{_bindir}/mediastreamer2_tester
%{_libdir}/libmediastreamer.so
%{_datadir}/mediastreamer2_tester/
%{_datadir}/Mediastreamer2/
%{_libdir}/pkgconfig/mediastreamer.pc

%changelog
