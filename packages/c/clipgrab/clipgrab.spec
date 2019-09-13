#
# spec file for package clipgrab
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.8.2
Release:        0
Summary:        Video downloader
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://clipgrab.org
Source0:        https://download.clipgrab.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  ImageMagick-extra
BuildRequires:  hicolor-icon-theme >= 0.15
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.9
BuildRequires:  pkgconfig(Qt5Xml) >= 5.9
Requires:       ffmpeg

%description
A program which downloads and converts online videos from YouTube, Vimeo,
DailyMotion, MyVideo and many other platforms.

%prep
%setup -q
chmod 0644 COPYING

%build
# none too clean, but it beats depending on icns-utils which has problems on non-x86 archs
dd if=%{name}.icns of=icon512.jp2 bs=1 skip=71836 count=79384
for s in 16 32 128 256 512; do
    convert -strip -resize ${s}x${s} icon512.jp2 ${s}.png
done

%qmake5 %{name}.pro
make %{?_smp_mflags}

%install
install -D -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m0755 %{name} %{buildroot}/%{_bindir}/%{name}
for s in 16 32 128 256 512; do
    install -D -m0644 "${s}.png" "%{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png"
done
%suse_update_desktop_file -r %{name} Video Editor

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%{_bindir}/clipgrab
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
