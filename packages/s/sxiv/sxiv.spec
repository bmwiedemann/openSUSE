#
# spec file for package sxiv
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


Name:           sxiv
Version:        25
Release:        0
Summary:        Simple X Image Viewer
License:        GPL-2.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/muennich/sxiv
Source:         https://github.com/muennich/sxiv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         sxiv.desktop.patch
Patch1:         sxiv.makefile.patch
Patch2:         sxiv.icon-makefile.patch
BuildRequires:  giflib-devel
BuildRequires:  imlib2-devel
BuildRequires:  libexif-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
Requires:       imlib2-loaders
Requires(post): desktop-file-utils
Requires(post): hicolor-icon-theme
Requires(postun): desktop-file-utils
Requires(postun): hicolor-icon-theme

%description
sxiv is an image viewer which only has the most basic features
for image viewing. It has vi key bindings and works with
tiling window managers.

Features:
- Basic image operations, e.g. zooming, panning, rotating
- Thumbnail mode: grid of selectable previews of all images
- Ability to cache thumbnails for fast re-loading
- Basic support for multi-frame images
- Loads all frames from GIF files and plays GIF animations
- Displays image information in status bar

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} V=1

%install
%make_install PREFIX=%{_prefix}
cd icon
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/sxiv
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/sxiv.1%{?ext_man}
%{_datadir}/sxiv/
%{_datadir}/sxiv/exec/
%{_datadir}/sxiv/exec/image-info
%{_datadir}/sxiv/exec/key-handler

%changelog
