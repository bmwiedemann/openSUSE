#
# spec file for package mediastreamer2
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


%define _name   mediastreamer
%define sobase  libmediastreamer_base
%define sovoip  libmediastreamer_voip
%define sover   10
%bcond_without ffmpeg
Name:           mediastreamer2
Version:        2.16.1
Release:        0
Summary:        Audio/Video real-time streaming
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/technical-corner/mediastreamer2/overview
Source:         https://linphone.org/releases/sources/%{_name}/%{_name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE mediastreamer2-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install mediastreamer.pc.
Patch0:         mediastreamer2-fix-pkgconfig.patch
# PATCH-FIX-OPENSUSE mediastreamer2-fix-xv.patch sor.alexei@meowr.ru -- Fix Xv by linking with Xext.
Patch1:         mediastreamer2-fix-xv.patch
# PATCH-FIX-UPSTREAM mediastreamer2-2.16.1-fix-no-git.patch -- Fix building out-of-git (commit de3a24b).
Patch2:         mediastreamer2-2.16.1-fix-no-git.patch
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
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  spandsp-devel
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
Obsoletes:      %{name}-lang
%if 0%{?suse_version} >= 1500
BuildRequires:  libjpeg-devel
%endif
%if %{with ffmpeg}
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libswscale) >= 0.7.0
%endif

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

%package -n %{sovoip}%{sover}
Summary:        Audio/video real-time streaming library, voip part
Group:          System/Libraries

%description -n %{sovoip}%{sover}
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package devel
Summary:        Headers, libraries and docs for the mediastreamer2 library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{sobase}%{sover} = %{version}
Requires:       %{sovoip}%{sover} = %{version}
Requires:       bcmatroska2-devel

%description devel
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the ortp library.

This package contains header files and development libraries needed to
develop programs using the mediastreamer2 library.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
%if %{with ffmpeg}
  -DCMAKE_INCLUDE_PATH=%{_includedir}/ffmpeg \
%else
  -DENABLE_NON_FREE_CODECS=OFF \
  -DENABLE_VIDEO=OFF           \
%endif
  -DENABLE_ZRTP=ON             \
  -DENABLE_STRICT=OFF          \
  -DENABLE_STATIC=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -T %{buildroot}%{_datadir}/doc/%{name}-%{version}/ \
  %{buildroot}%{_docdir}/%{name}/

%post -n %{sobase}%{sover} -p /sbin/ldconfig

%postun -n %{sobase}%{sover} -p /sbin/ldconfig

%post -n %{sovoip}%{sover} -p /sbin/ldconfig

%postun -n %{sovoip}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_docdir}/%{name}/
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120000
%{_bindir}/mediastream
%{_bindir}/mkvstream
%dir %{_datadir}/images/
%{_datadir}/images/nowebcamCIF.jpg
%endif

%files -n %{sobase}%{sover}
%{_libdir}/%{sobase}.so.%{sover}*

%files -n %{sovoip}%{sover}
%{_libdir}/%{sovoip}.so.%{sover}*

%files devel
%{_includedir}/mediastreamer2/
%{_bindir}/mediastreamer2_tester
%{_libdir}/libmediastreamer_*.so
%{_datadir}/mediastreamer2_tester/
%{_datadir}/Mediastreamer2/
%{_libdir}/pkgconfig/%{_name}.pc

%changelog
