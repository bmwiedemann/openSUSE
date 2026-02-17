#
# spec file for package dvdauthor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           dvdauthor
Version:        0.7.2
Release:        0
Summary:        Low-level DVD Authoring Tools
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://dvdauthor.sourceforge.net/
Source0:        https://github.com/ldo/dvdauthor/archive/%{version}.tar.gz#/dvdauthor-%{version}.tar.gz
#PATCH-FIX-UPSTREAM dvdauthor-0.7.0_glibc-2.20.patch avvissu@yandex.ru -- Fix build with glibc-2.20
Patch0:         dvdauthor-0.7.0_glibc-2.20.patch
Patch1:         dvdauthor-0.7.2-imagemagick7.patch

# Patches from upstream's git:
Patch3:         0001-change-to-interim-version-number.patch
Patch4:         0002-fix-to-build-with-GraphicsMagick.patch
Patch5:         0003-Looks-like-I-need-both-MAGICK_CPPFLAGS-and-MAGICK_CF.patch
Patch6:         0004-try-using-simpler-way-of-building-with-ImageEMagick.patch
Patch7:         0005-merge-MAGICK_CPPFLAGS-into-MAGICK_CFLAGS.patch
Patch8:         0006-use-different-module-names-ImageMagick-vs-GraphicsMa.patch
Patch9:         0007-No-longer-automatically-build-with-ImageMagick-or-Gr.patch
Patch10:        0008-fix-incorrect-use-of-AC_ARG_WITH.patch
Patch11:        0009-Use-pkg-config-to-find-FreeType-thanks-to-Lars-Wendl.patch
Patch12:        0010-fix-some-build-warnings.patch
Patch13:        0011-Use-PKG_CHECK_MODULES-to-detect-the-libxml2-library.patch
Patch14:        0012-Fix-another-build-warning.patch
Patch15:        gettext-fix.patch

Patch20:        dvdauthor-bootstrap-workaround-for-autoconf-2.73.patch

BuildRequires:  ImageMagick-devel
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
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
Provides:       dvdauthor07 = %{version}
Obsoletes:      dvdauthor07 <= %{version}
ExcludeArch:    i586

%description
dvdauthor is a program that will generate a DVD-Video movie from a
valid MPEG-2 stream. To start you need MPEG-2 files that contain
the necessary DVD-Video VOB packets. These can be generated with
FFmpeg, or by by passing `-f 8` to `mplex`.

%prep
%autosetup -p1

%build
./bootstrap
# export MAGICK_CFLAGS=`ImageMagick-config --cppflags`
# export CFLAGS="%{optflags} $MAGICK_CFLAGS"
export LDFLAGS="$LDFLAGS -Wl,-z -Wl,noexecstack"
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc README TODO AUTHORS ChangeLog
%license COPYING
%{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/dvdauthor
%{_datadir}/dvdauthor/*

%changelog
