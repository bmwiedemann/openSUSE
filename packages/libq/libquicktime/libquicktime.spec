#
# spec file for package libquicktime
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


%define sover 0
%bcond_with    faac
%bcond_with    faad
%bcond_with    x264
Name:           libquicktime
Version:        1.2.4+git20180804.fff99cd
Release:        0
Summary:        Library for Reading and Writing Quicktime Movie Files
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libquicktime.sf.net
Source0:        %{name}-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libdv-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  schroedinger-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libavcodec) < 59
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libswscale) < 6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xv)
%if 0%{?BUILD_ORIG}
%if %{with faac}
BuildRequires:  libfaac-devel
%endif
%if %{with faad}
BuildRequires:  libfaad2-devel
%endif
%if %{with x264}
BuildRequires:  libx264-devel
%endif
%endif

%description
A library for reading and writing Quicktime movie files, based on and
forked from quicktime4linux.

%package orig-addon
Summary:        Library for Reading and Writing Quicktime Movie Files
Group:          System/Libraries
Requires:       %{name}

%description orig-addon
A library for reading and writing Quicktime movie files, based on and
forked from quicktime4linux.

%package -n %{name}%{sover}
Summary:        Library for Reading and Writing Quicktime Movie Files
Group:          System/Libraries

%description -n %{name}%{sover}
A library for reading and writing Quicktime movie files, based on and
forked from quicktime4linux.

%package -n libquicktime-devel
Summary:        Library for reading/writing quicktime movie files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}%{sover} = %{version}
%if 0%{?BUILD_ORIG}
Requires:       %{name}-orig-addon = %{version}
%endif

%description -n libquicktime-devel
library for reading/writing quicktime movie files, based on and forked
from quicktime4linux

%package -n libquicktime-tools
Summary:        Libquicktime Tools
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{name} = %{version}
Requires:       %{name}%{sover} = %{version}
%if 0%{?BUILD_ORIG}
Requires:       %{name}-orig-addon = %{version}
%endif

%description -n libquicktime-tools
Tools for reading/writing quicktime movie files.

%lang_package

%prep
%setup -q

%build
echo 'HTML_TIMESTAMP=NO' >> doc/Doxyfile.in
./autogen.sh
%configure \
       --enable-gpl \
       --docdir="%{_docdir}/%{name}-devel" \
       --with-libdv \
       --with-cpuflags=none \
       --without-gtk
make %{?_smp_mflags}

%install
%make_install
ln -s lqt "%{buildroot}%{_includedir}/quicktime"
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libquicktime%{sover} -p /sbin/ldconfig
%postun -n libquicktime%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README TODO
%dir %{_libdir}/libquicktime
%{_libdir}/libquicktime/lqt_audiocodec.so
%{_libdir}/libquicktime/lqt_dv.so
%{_libdir}/libquicktime/lqt_lame.so
%{_libdir}/libquicktime/lqt_mjpeg.so
%{_libdir}/libquicktime/lqt_png.so
%{_libdir}/libquicktime/lqt_rtjpeg.so
%{_libdir}/libquicktime/lqt_schroedinger.so
%{_libdir}/libquicktime/lqt_videocodec.so
%{_libdir}/libquicktime/lqt_vorbis.so
%{_libdir}/libquicktime/lqt_ffmpeg.so

%if 0%{?BUILD_ORIG}
%files orig-addon
%if %{with faac}
%{_libdir}/libquicktime/lqt_faac.so
%endif
%if %{with faad}
%{_libdir}/libquicktime/lqt_faad2.so
%endif
%if %{with x264}
%{_libdir}/libquicktime/lqt_x264.so
%endif
%endif

%files -n libquicktime%{sover}
%license COPYING
%{_libdir}/libquicktime.so.%{sover}
%{_libdir}/libquicktime.so.%{sover}.*.*

%files -n libquicktime-devel
%doc %{_docdir}/%{name}-devel
%{_includedir}/lqt
%{_includedir}/quicktime
%{_libdir}/libquicktime.so
%{_libdir}/pkgconfig/libquicktime.pc

%files -n libquicktime-tools
%{_bindir}/lqt_transcode
%{_bindir}/lqtplay
%{_bindir}/lqtremux
%{_bindir}/qt2text
%{_bindir}/qtdechunk
%{_bindir}/qtdump
%{_bindir}/qtinfo
%{_bindir}/qtrechunk
%{_bindir}/qtstreamize
%{_bindir}/qtyuv4toyuv
%{_mandir}/man1/lqtplay.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
