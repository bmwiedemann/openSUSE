#
# spec file for package ristretto
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


%bcond_with git
Name:           ristretto
Version:        0.12.4
Release:        0lib
Summary:        Image viewer for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://docs.xfce.org/apps/ristretto/start
Source0:        https://archive.xfce.org/src/apps/ristretto/0.12/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE ristretto-add-mime-types.patch gber@opensuse.org -- Adds support for additional image MIME types supported by openSUSE
Patch0:         ristretto-add-mime-types.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libexif) >= 0.6.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.16.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.1
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
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
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

%suse_update_desktop_file -i org.xfce.ristretto GTK Graphics Viewer

%fdupes %{buildroot}%{_datadir}

%find_lang %{name} %{?no_lang_C}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/ristretto
%{_datadir}/applications/org.xfce.ristretto.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.ristretto.*
%{_datadir}/metainfo/org.xfce.ristretto.appdata.xml

%files lang -f %{name}.lang

%changelog
