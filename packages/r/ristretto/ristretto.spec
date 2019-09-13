#
# spec file for package ristretto
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


Name:           ristretto
Version:        0.10.0
Release:        0
Summary:        Image viewer for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://docs.xfce.org/apps/ristretto/start
Source0:        https://archive.xfce.org/src/apps/ristretto/0.10/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE ristretto-add-mime-types.patch gber@opensuse.org -- Adds support for additional image MIME types supported by openSUSE
Patch0:         ristretto-add-mime-types.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(exo-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0)
Recommends:     %{name}-lang = %{version}

%description
The Ristretto Image Viewer is an application that can be used to
view, and scroll through images.

It can be used to run a slideshow of images, open images with other
applications like an image editor or configure an image as the
desktop wallpaper.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%suse_update_desktop_file -i ristretto GTK Graphics Viewer

%fdupes %{buildroot}%{_datadir}

%find_lang %{name} %{?no_lang_C}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/ristretto
%{_datadir}/applications/ristretto.desktop
%{_datadir}/icons/hicolor/*/apps/ristretto.*
%{_datadir}/metainfo/ristretto.appdata.xml

%files lang -f %{name}.lang

%changelog
