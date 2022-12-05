#
# spec file for package scummvm-tools
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


Name:           scummvm-tools
Version:        2.6.0
Release:        0
Summary:        ScummVM-related tools
License:        GPL-3.0-or-later
URL:            https://www.scummvm.org
Source0:        https://downloads.scummvm.org/frs/scummvm-tools/%{version}/scummvm-tools-%{version}.tar.xz
Source1:        %{name}.desktop
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM fix-new-wxwidgets.patch -- https://bugs.scummvm.org/ticket/9554
Patch0:         fix-new-wxwidgets.patch
BuildRequires:  ImageMagick
BuildRequires:  boost-devel >= 1.32.0
BuildRequires:  c++_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  icns-utils
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  pkgconfig(flac) >= 1.1.3
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng) >= 1.2.8
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(zlib)

%description
This is a collection of various tools that may be useful to use in
conjunction with ScummVM.
Please note that although a tool may support a feature, certain ScummVM
versions may not. ScummVM 0.6.x does not support FLAC audio, for example.

Many games package together all their game data in a few big archive files.
The following tools can be used to extract these archives, and in some cases
are needed to make certain game versions usable with ScummVM.

The following tools can also be used to analyze the game scripts
(controlling the behavior of certain scenes and actors in a game).
These tools are most useful to developers.

%prep
%autosetup -p1
# build the endianness test without optimization otherwise gcc is too smart
# and optimize everything away, making the test fail
sed -i '/tmp_endianness_check.cpp/ s/$CXXFLAGS/$CXXFLAGS -fno-lto -O0/' configure
# extract icon
icns2png -x -s 512x512 gui/media/scummvmtools.icns

%build
./configure --prefix=%{_prefix} \
            --enable-verbose-build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install
# Install icons and .desktop file
for res in 16 32 48 64 128 256 512; do
   mkdir -pv "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps"
   convert -strip -resize $resx$res scummvmtools_512x512x32.png "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps/%{name}.png"
done
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%fdupes %{buildroot}%{_datadir}

%files
%defattr(0644,root,root,0755)
%license COPYING
%doc README TODO
%attr(0755,root,root) %{_bindir}/scummvm-tools
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
