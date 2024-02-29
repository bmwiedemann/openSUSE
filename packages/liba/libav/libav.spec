#
# spec file for package libav
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

Name:           libav
Version:        12.3
Release:        0
Summary:        Library working with various multimedia formats
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            https://libav.org/
Source:         http://%{name}.org/releases/%{name}-%{version}.tar.xz
Patch0:         use-ffmpeg-libs.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  ffmpeg-private-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libav is a C library that works with various multimedia formats.

%package tools
Summary:        Tools for multimedia access
Group:          Productivity/Multimedia/Video/Editors and Convertors

%description tools
Various tools providing access to multimedia metadata and similar things.

This build of libav-tools is modified to use the ffmpeg libraries

%prep
%autosetup -p1

# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" -i cmdutils.c
sed -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -i cmdutils.c
rm -Rf libavcodec libavdevice libavfilter libavformat libavresample libavutil libswscale

%build
export CFLAGS='%{optflags}'
export IFLAGS='-I/usr/include/ffmpeg -iquote /usr/include/ffmpeg/private -iquote /usr/include/ffmpeg/libavutil -iquote /usr/include/ffmpeg/libavformat -iquote /usr/include/ffmpeg/libavcodec'
./configure \
	--prefix=%{_prefix} --libdir=%{_libdir} --shlibdir=%{_libdir} \
	--extra-cflags='%{optflags}' --optflags='%{optflags}' \
	--incdir="%{_includedir}/libav" \
        --enable-pic  --disable-yasm

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install install-man

%files tools
%defattr(-,root,root)
%doc Changelog COPYING.GPLv2 CREDITS LICENSE README.md
%{_bindir}/*
%{_datadir}/avconv
%{_mandir}/man1/*

%changelog
