#
# spec file for package dvdauthor
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dvdauthor
Version:        0.7.2
Release:        0
Summary:        Low-level DVD Authoring Tools
License:        GPL-2.0+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://dvdauthor.sourceforge.net/
Source0:        https://github.com/ldo/dvdauthor/archive/%{version}.tar.gz#/dvdauthor-%{version}.tar.gz
#PATCH-FIX-UPSTREAM dvdauthor-0.7.0_glibc-2.20.patch avvissu@yandex.ru -- Fix build with glibc-2.20
Patch0:         dvdauthor-0.7.0_glibc-2.20.patch
#
#Patch1:         dvdauthor-imagemagick7.patch
BuildRequires:  bison
BuildRequires:  docbook-utils
BuildRequires:  flex
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  openjade
BuildRequires:  pkgconfig
BuildRequires:  texlive-booktabs
BuildRequires:  texlive-currfile
BuildRequires:  texlive-dviasm-bin
BuildRequires:  texlive-footmisc
BuildRequires:  texlive-koma-script
BuildRequires:  texlive-luatexbase
BuildRequires:  GraphicsMagick-devel
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
Provides:       dvdauthor07 = %{version}
Obsoletes:      dvdauthor07 <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dvdauthor is a program that will generate a DVD-Video movie from a
valid MPEG-2 stream. To start you need MPEG-2 files that contain
the necessary DVD-Video VOB packets. These can be generated with
FFmpeg, or by by passing `-f 8` to `mplex`.

%prep
%setup -q
%patch0
#%%patch1

%build
%if 1 == 0
%define gcc_version 7
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif
./bootstrap
export MAGICK_CFLAGS=`GraphicsMagick-config --cppflags`
export CFLAGS="%{optflags} $MAGICK_CFLAGS"
export LDFLAGS="$LDFLAGS -Wl,-z -Wl,noexecstack"
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README TODO AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/dvdauthor
%{_datadir}/dvdauthor/*

%changelog
