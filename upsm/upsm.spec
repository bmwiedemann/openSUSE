#
# spec file for package upsm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           upsm
Version:        2.2.0
Release:        0
Summary:        Qt-based ups monitor (front-end for upsc from Network UPS Tools)
License:        SUSE-Public-Domain
Group:          System/Monitoring
URL:            https://github.com/psemiletov/upsm
Source:         https://github.com/psemiletov/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  binutils-gold
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       nut

%description
upsm is Qt-based ups monitor (front-end for upsc from Network UPS Tools).
It sits at the tray and polls nut server using upsc, so you need to set
up NUT first.

%prep
%setup -q
convert -strip icons/upsm.png -resize 128x128 icons/upsm.png

%build
%cmake
%make_jobs

%install
%cmake_install
%suse_update_desktop_file -r  %{name} System Monitor

%if 0%{?suse_version} <= 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc ChangeLog README
%{_bindir}/upsm
%{_datadir}/applications/upsm.desktop
%{_datadir}/icons/hicolor/128x128/apps/upsm.png
%{_datadir}/icons/hicolor/scalable/apps/upsm.svg

%changelog
