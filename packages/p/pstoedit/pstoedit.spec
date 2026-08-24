#
# spec file for package pstoedit
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


Name:           pstoedit
Version:        4.3
Release:        0
Summary:        PostScript and PDF Converter
License:        GPL-2.0-or-later
URL:            https://www.pstoedit.com/
Source0:        https://github.com/woglu/pstoedit/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.1
# PATCH-FIX-UPSTREAM fix-wrong-pkg-config-file-contents.patch -- based on commit 4911078
Patch0:         fix-wrong-pkg-config-file-contents.patch
# PATCH-FIX-UPSTREAM fix-wrong-L-flag-for-linking-the-GUI.patch -- based on commit a7c5e80
Patch1:         fix-wrong-L-flag-for-linking-the-GUI.patch
# PATCH-FIX-UPSTREAM fix-Qt-linker-flags.patch -- based on commit 65f4bbf
Patch2:         fix-Qt-linker-flags.patch
# PATCH-FIX-OPENSUSE fix-pkgconfig-ImageMagick.patch munix9@googlemail.com -- fix pkgconfig ImageMagick module name
Patch3:         fix-pkgconfig-ImageMagick.patch
# PATCH-FIX-OPENSUSE fix-reproducible-build.patch munix9@googlemail.com -- allow for reproducible builds
Patch4:         fix-reproducible-build.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-devel
BuildRequires:  libEMF-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  plotutils-devel
# docs: there are currently issues with reproducible builds (eg. section order)
#BuildRequires:  texlive-babel
#BuildRequires:  texlive-babel-english
#BuildRequires:  texlive-fancyhdr
#BuildRequires:  texlive-latex
#BuildRequires:  texlive-scheme-basic
#BuildRequires:  texlive-scripts
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libzip)
Requires:       ghostscript

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers.

%package gui
Summary:        Qt GUI of %{name}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt6-base-devel
Requires:       %{name} = %{version}

%description gui
PstoeditQtGui provides an alternative to the command driven operation.
The GUI provides access to almost all options and features that are
supported by pstoedit. In addition it supports the conversion of multiple
files in one job and also provides some shortcuts to some of Ghostscript's
high leve output devices.

%package devel
Summary:        PostScript and PDF converter (development files)
Requires:       %{name} = %{version}
Requires:       plotutils-devel
Requires:       pkgconfig(Magick++)
Requires:       pkgconfig(libzip)

%description devel
PostScript and PDF converter development headers and library files.

%prep
%autosetup -p1

mkdir -p m4
dos2unix doc/*.htm examples/figtext.ps

# create dummy docs so the make below will run correctly
touch doc/pstoedit.{1,htm,pdf}

%build
autoreconf -if --warnings=all
%configure \
	--disable-docs \
	--disable-static \
	--with-emf \
	--with-gui \
	--with-libplot \
	--with-magick \
	--with-pptx
%make_build

%install
%make_install
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 %{SOURCE1}

chrpath -d %{buildroot}%{_bindir}/pstoedit
chrpath -d %{buildroot}%{_bindir}/PstoeditQtGui

find %{buildroot} -type f -name "*.la" -delete -print

# doc cleanup
rm -f examples/Makefile*
rm -rf %{buildroot}%{_datadir}/doc

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/PstoeditQtGui.desktop

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md doc/changelog.htm examples
%{_bindir}/pstoedit
%{_datadir}/pstoedit
%{_libdir}/libpstoedit.so.*
%dir %{_libdir}/pstoedit
%{_libdir}/pstoedit/libp2edrvlplot.so
%{_libdir}/pstoedit/libp2edrvmagick++.so
%{_libdir}/pstoedit/libp2edrvpptx.so
%{_libdir}/pstoedit/libp2edrvstd.so
%{_libdir}/pstoedit/libp2edrvwmf.so
%{_mandir}/man1/pstoedit.1%{?ext_man}

%files gui
%{_bindir}/PstoeditQtGui
%{_datadir}/applications/PstoeditQtGui.desktop
%{_datadir}/icons/hicolor/256x256/apps/pstoedit.png

%files devel
%{_includedir}/pstoedit
%{_libdir}/libpstoedit.so
%{_libdir}/pkgconfig/pstoedit.pc

%changelog
