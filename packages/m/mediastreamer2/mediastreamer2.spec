#
# spec file for package mediastreamer2
#
# Copyright (c) 2023 SUSE LLC
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
%define docuver 5.2.0

Name:           mediastreamer2
Version:        5.2.6
Release:        0
Summary:        Audio/Video real-time streaming
License:        AGPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/technical-corner/mediastreamer2
Source:         https://gitlab.linphone.org/BC/public/mediastreamer2/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         mediastreamer2-fix-pkgconfig.patch
Patch1:         fix-srtp2-linphone.patch
Patch2:         fix-build-ffmpeg5.patch
BuildRequires:  bcmatroska2-devel >= 0.23
BuildRequires:  broadvoice16-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  graphviz
%if 0%{?suse_version}
BuildRequires:  libgsm-devel
%else
BuildRequires:  gsm-devel
%endif
BuildRequires:  libjpeg-turbo >= 2.0.0
%if 0%{?fedora}
BuildRequires:  turbojpeg-devel
%endif
BuildRequires:  libpcap-devel
BuildRequires:  libsrtp2-linphone-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  spandsp-devel
%if 0%{?suse_version}
BuildRequires:  sqlite3-devel
%else
BuildRequires:  libsqlite3x-devel
%endif
BuildRequires:  vim
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bctoolbox) >= 5.2.0
BuildRequires:  pkgconfig(libbcg729)
BuildRequires:  pkgconfig(libbzrtp) >= 5.2.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(ortp) >= 5.2.0
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
%if 0%{?suse_version} >= 1500
BuildRequires:  libjpeg-devel >= 8.2.0
%endif
BuildRequires:  chrpath
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libswscale) >= 0.7.0

%description
Mediastreamer2 is a library to make audio and video real-time
streaming and processing. It is written in pure C and based upon the
oRTP library.

%package -n %{sobase}%{sover}
Summary:        Audio/video real-time streaming library, base part
Group:          System/Libraries

%description -n %{sobase}%{sover}
Mediastreamer2 is a library to make audio and video real-time
streaming and processing. It is written in pure C and based upon the
oRTP library.

%package doc
Summary:        Documentation for the mediastreamer2 library
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
Mediastreamer2 is a library to make audio and video real-time
streaming and processing. It is written in pure C and based upon the
oRTP library.

This package contains documentation files

%package devel
Summary:        Headers and libraries for the mediastreamer2 library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{sobase}%{sover} = %{version}
Requires:       bcmatroska2-devel

%description devel
Mediastreamer2 is a library to make audio and video real-time
streaming and processing. It is written in pure C and based upon the
oRTP library.

This package contains header files and development libraries needed to
develop programs using the mediastreamer2 library.

%prep
%autosetup -N
%patch0 -p1
%patch1 -p1
if pkg-config --atleast-version 59.37.100 libavcodec; then
%patch2 -p1
fi

%build
export CFLAGS="%(echo %{optflags}) -fcommon -Wno-implicit-function-declaration"
export CXXFLAGS="$CFLAGS"
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="-flto=auto -Wl,--as-needed -Wl,-z,now" \
    -DENABLE_STATIC=NO \
%if 0%{?fedora}
   -DCMAKE_INSTALL_LIBDIR=lib64 \
%endif
    -DENABLE_STRICT=NO
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -T %{buildroot}%{_datadir}/doc/%{name}-%{docuver}/ \
  %{buildroot}%{_docdir}/%{name}/

chrpath -d %{buildroot}%{_bindir}/mediastream %{buildroot}%{_bindir}/mkvstream %{buildroot}%{_bindir}/mediastreamer2_tester
chrpath -d %{buildroot}%{_libdir}/%{sobase}.so.%{sover}* %{buildroot}%{_libdir}/libmediastreamer.so

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
%dir %{_includedir}/OpenGL
%dir %{_includedir}/OpenGL/EGL
%dir %{_includedir}/OpenGL/GLES2
%dir %{_includedir}/OpenGL/GLES3
%dir %{_includedir}/OpenGL/KHR
%{_includedir}/mediastreamer2/
%{_includedir}/OpenGL/EGL/egl.h
%{_includedir}/OpenGL/EGL/eglext.h
%{_includedir}/OpenGL/EGL/eglplatform.h
%{_includedir}/OpenGL/GLES2/gl2.h
%{_includedir}/OpenGL/GLES2/gl2ext.h
%{_includedir}/OpenGL/GLES2/gl2platform.h
%{_includedir}/OpenGL/GLES3/gl3.h
%{_includedir}/OpenGL/GLES3/gl31.h
%{_includedir}/OpenGL/GLES3/gl32.h
%{_includedir}/OpenGL/GLES3/gl3platform.h
%{_includedir}/OpenGL/KHR/khrplatform.h
%{_includedir}/OpenGL/LICENSE
%{_includedir}/OpenGL/README.md
%{_includedir}/OpenGL/angle_windowsstore.h
%{_bindir}/mediastreamer2_tester
%{_libdir}/libmediastreamer.so
%{_datadir}/mediastreamer2_tester/
%{_datadir}/Mediastreamer2/
%{_libdir}/pkgconfig/mediastreamer.pc

%changelog
