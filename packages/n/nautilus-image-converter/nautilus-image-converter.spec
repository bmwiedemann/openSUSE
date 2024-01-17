#
# spec file for package nautilus-image-converter
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2007-2010 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define nautilus_extdir %(pkg-config --variable=extensiondir libnautilus-extension-4)

Name:           nautilus-image-converter
Summary:        Nautilus Image Converter
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Convertors
Version:        0.4.0
Release:        0
URL:            https://gitlab.gnome.org/coreyberla/nautilus-image-converter
Source:         %{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43.rc
Recommends:     ImageMagick

%description
The Nautilus-Image-Converter extension allows you to resize/rotate images
from Nautilus.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{nautilus_extdir}/libnautilus-image-converter.so
%dir %{_datadir}/nautilus-image-converter
%{_datadir}/nautilus-image-converter/nautilus-image-resize.ui
%{_datadir}/nautilus-image-converter/nautilus-image-rotate.ui

%files lang -f %{name}.lang

%changelog
