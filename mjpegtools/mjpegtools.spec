#
# spec file for package mjpegtools
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


%define lib_version %(echo %{version} | cut -d. -f1-2)
Name:           mjpegtools
Version:        2.0.0
Release:        0
Summary:        MJPEG Video Capture and Processing Tools
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://mjpeg.sourceforge.net/
Source:         http://sourceforge.net/projects/mjpeg/files/mjpegtools/%{version}/mjpegtools-%{version}.tar.gz
Source99:       baselibs.conf
Patch0:         mjpegtools-cpuinfo.patch
Patch1:         mjpegtools-vector_alignment.patch
Patch2:         mjpegtools-getopt.patch
Patch3:         mjpegtools-writeable_strings.patch
Patch4:         mjpegtools-no_arch_tuning.patch
Patch5:         mjpegtools-config_h.patch
Patch6:         mjpegtools-v4l-2.6.38.patch
Patch7:         mjpegtools-gcc47.patch
Patch8:         mjpegtools-2.0.0-fix-bashisms.patch
Patch9:         mjpegtools-more-pie.patch
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(libdv)
BuildRequires:  pkgconfig(libpng) >= 1.4
BuildRequires:  pkgconfig(libquicktime)
BuildRequires:  pkgconfig(libv4l1)
BuildRequires:  pkgconfig(sdl)
Requires(post): info
Requires(preun): info
Obsoletes:      mjpegtools-orig-addon

%description
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n libmjpegutils-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n libmjpegutils-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n liblavfile-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n liblavfile-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n liblavjpeg-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n liblavjpeg-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n liblavplay-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n liblavplay-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n liblavrec-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n liblavrec-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n libmplex2-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n libmplex2-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n libmpeg2encpp-2_0-0
Summary:        MJPEG Video Capture and Processing Tools
Group:          System/Libraries

%description -n libmpeg2encpp-2_0-0
The mjpegtools allow for capture, playback, processing, and simple
editing of MJPEG AV data. The hardware I/O applications are intended
for use with Zoran MJPEG framegrabber-based hardware (see the
zoran-driver package), but the processing tools can be used with MJPEG
data from other sources as well.

%package -n libmjpegutils-devel
Summary:        MJPEG Video Capture and Processing Tools
Group:          Development/Libraries/C and C++
Requires:       liblavfile-2_0-0 = %{version}
Requires:       liblavjpeg-2_0-0 = %{version}
Requires:       liblavplay-2_0-0 = %{version}
Requires:       liblavrec-2_0-0 = %{version}
Requires:       libmjpegutils-2_0-0 = %{version}
Requires:       libmpeg2encpp-2_0-0 = %{version}
Requires:       libmplex2-2_0-0 = %{version}
Provides:       mjpegtools-devel = %{version}
Obsoletes:      mjpegtools-devel < %{version}

%description -n libmjpegutils-devel
This package contains all files needed to develop code that uses the
mjpegtools libraries.

%prep
%autosetup -N
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4
%patch5
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
sed -i~ '/currently broken/d' mpeg2enc/mpeg2enc.cc
diff -u mpeg2enc/mpeg2enc.cc* || :
autoreconf -vfi
EXTRAOPTS=""
%ifarch ppc ppc64
EXTRAOPTS="--disable-simd-accel"
%endif
export CFLAGS="%{optflags} $(pkg-config --cflags SDL_gfx)"
%configure \
	--disable-static \
	--disable-arch_tuning \
	--without-gtk \
	$EXTRAOPTS \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
%install_info --info-dir=%{_infodir} %{_infodir}/mjpeg-howto.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/mjpeg-howto.info%{ext_info}

%post -n libmjpegutils-2_0-0 -p /sbin/ldconfig
%postun -n libmjpegutils-2_0-0 -p /sbin/ldconfig

%post -n liblavfile-2_0-0 -p /sbin/ldconfig
%postun -n liblavfile-2_0-0 -p /sbin/ldconfig

%post -n liblavjpeg-2_0-0 -p /sbin/ldconfig
%postun -n liblavjpeg-2_0-0 -p /sbin/ldconfig

%post -n liblavplay-2_0-0 -p /sbin/ldconfig
%postun -n liblavplay-2_0-0 -p /sbin/ldconfig

%post -n liblavrec-2_0-0 -p /sbin/ldconfig
%postun -n liblavrec-2_0-0 -p /sbin/ldconfig

%post -n libmplex2-2_0-0 -p /sbin/ldconfig
%postun -n libmplex2-2_0-0 -p /sbin/ldconfig

%post -n libmpeg2encpp-2_0-0 -p /sbin/ldconfig
%postun -n libmpeg2encpp-2_0-0 -p /sbin/ldconfig

%files
%attr(0755,root,root) %{_bindir}/*
%doc AUTHORS BUGS CHANGES HINTS NEWS PLANS README* TODO
%{_mandir}/man?/*.?%{ext_man}
%{_infodir}/mjpeg-howto.info%{ext_info}

%files -n libmjpegutils-2_0-0
%license COPYING
%{_libdir}/libmjpegutils-%{lib_version}.so.*

%files -n liblavfile-2_0-0
%{_libdir}/liblavfile-%{lib_version}.so.*

%files -n liblavjpeg-2_0-0
%{_libdir}/liblavjpeg-%{lib_version}.so.*

%files -n liblavplay-2_0-0
%{_libdir}/liblavplay-%{lib_version}.so.*

%files -n liblavrec-2_0-0
%{_libdir}/liblavrec-%{lib_version}.so.*

%files -n libmplex2-2_0-0
%{_libdir}/libmplex2-%{lib_version}.so.*

%files -n libmpeg2encpp-2_0-0
%{_libdir}/libmpeg2encpp-%{lib_version}.so.*

%files -n libmjpegutils-devel
%{_includedir}/mjpegtools/
%{_libdir}/liblavfile.so
%{_libdir}/liblavjpeg.so
%{_libdir}/liblavplay.so
%{_libdir}/liblavrec.so
%{_libdir}/libmjpegutils.so
%{_libdir}/libmpeg2encpp.so
%{_libdir}/libmplex2.so
%{_libdir}/pkgconfig/mjpegtools.pc

%changelog
