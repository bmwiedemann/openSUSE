#
# spec file for package clipgrab
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2008-2013 detlef@links2linux.de
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


Name:           clipgrab
Version:        3.9.14
Release:        0
Summary:        Video downloader
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://clipgrab.org
Source0:        https://download.clipgrab.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM clipgrab-qt6.patch - enable building with qt6 taken from void linux https://github.com/void-linux/void-packages/blob/master/srcpkgs/clipgrab/patches/qt6.patch
Patch0:         clipgrab-qt6.patch
BuildRequires:  ImageMagick-extra
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  qt6-webenginewidgets-devel
BuildRequires:  qt6-widgets-devel
Requires:       ffmpeg

%description
A program which downloads and converts online videos from YouTube, Vimeo,
DailyMotion, MyVideo and many other platforms.

%prep
%autosetup -p1

chmod 0644 COPYING

%build
# none too clean, but it beats depending on icns-utils which has problems on non-x86 archs
dd if=%{name}.icns of=icon512.jp2 bs=1 skip=71836 count=79384
for s in 16 32 128 256 512; do
    convert -strip -resize ${s}x${s} icon512.jp2 ${s}.png
done

%qmake6 %{name}.pro
%make_build

%install
install -D -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m0755 %{name} %{buildroot}/%{_bindir}/%{name}
for s in 16 32 128 256 512; do
    install -D -m0644 "${s}.png" "%{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png"
done

%files
%license COPYING
%{_bindir}/clipgrab
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
