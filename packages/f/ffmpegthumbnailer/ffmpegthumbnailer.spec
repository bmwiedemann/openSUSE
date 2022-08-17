#
# spec file for package ffmpegthumbnailer
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Mariusz Fik <fisiu@opensuse.org>
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define soname  4
Name:           ffmpegthumbnailer
Version:        2.2.2
Release:        0
Summary:        Video thumbnailer that can be used by file managers
License:        GPL-2.0-or-later
URL:            https://github.com/dirkvdb/ffmpegthumbnailer
Source:         https://github.com/dirkvdb/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
#PATCH-FIX-UPSTREAM ffmpegthumbnailer-cmake-updates.patch dirk.vdb@gmail.com -- Update CMakeLists.txt for new cmake version.
Patch0:         ffmpegthumbnailer-cmake-updates.patch
# PATCH-FIX-UPSTREAM badshah400@gmail.com -- Removes use of functionality deprecated in ffmpeg4 and dropped from ffmpeg5, patch taken from upstream commit
Patch1:         https://github.com/dirkvdb/ffmpegthumbnailer/commit/372cd422e57a9a3531eb9a30559d665caecff1ba.patch
# PATCH-FIX-UPSTREAM badshah400@gmail.com -- Constify AVCodec, patch taken from upstream commit
Patch2:         https://github.com/dirkvdb/ffmpegthumbnailer/commit/efb5b618f1c1471c1a7900aed3a59d851ea9a210.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

%description
This video thumbnailer can be used to create thumbnails for
video files. The thumbnailer uses ffmpeg to decode frames from the
video files, so supported video formats depend on the configuration
flags of ffmpeg.

The project also includes a C/C++ library that can be used by
developers to generate thumbnails in their projects.

%package -n lib%{name}%{soname}
Summary:        Video thumbnail generator

%description -n lib%{name}%{soname}
Video thumbnailer that can be used by file managers.

This video thumbnailer can be used to create thumbnails for video
files. The thumbnailer uses ffmpeg to decode frames from files.

%package -n lib%{name}-devel
Summary:        Development files for ffmpegthumbnailer
Requires:       libffmpegthumbnailer%{soname} = %{version}

%description -n lib%{name}-devel
Video thumbnailer that can be used by file managers.

This video thumbnailer can be used to create thumbnails for video
files. The thumbnailer uses ffmpeg to decode frames from files.

%prep
%autosetup -p1
chmod 644 AUTHORS README

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_GIO=ON \
  -DENABLE_THUMBNAILER=ON
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_mandir}/man1/*.1%{?ext_man}
%{_bindir}/%{name}
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer

%files -n lib%{name}%{soname}
%{_libdir}/lib%{name}.so.%{soname}
%{_libdir}/lib%{name}.so.%{soname}.*

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so
%dir %{_includedir}/lib%{name}
%{_includedir}/lib%{name}/*.h
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
