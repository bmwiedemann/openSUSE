#
# spec file for package caja-dropbox
#
# Copyright (c) 2024 SUSE LLC
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


%define _version 1.28

Name:           caja-dropbox
Version:        1.28.0
Release:        0
Summary:        Dropbox client integrated into Caja
License:        GPL-3.0-or-later
URL:            https://mate-desktop.org/
Group:          Productivity/File utilities
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE caja-dropbox_no-dropbox-bin.patch sor.alexei@meowr.ru -- Strip dropbox binary installation.
Patch0:         caja-dropbox_no-dropbox-bin.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
Recommends:     %{name}-lang

%description
Dropbox is a proprietary service that lets one bring photos,
documents, and videos anywhere and share them easily.

This package integrates Dropbox seamlessly into Caja.

%package -n caja-extension-dropbox
Summary:        Dropbox client integrated into Caja
Requires:       caja >= %{_version}
Requires:       dropbox
# caja-dropbox was last used in openSUSE Leap 42.1.
Provides:       caja-dropbox = %{version}
Obsoletes:      caja-dropbox < %{version}

%description -n caja-extension-dropbox
Dropbox is a proprietary service that lets one bring photos,
documents, and videos anywhere and share them easily.

This package integrates Dropbox seamlessly into Caja.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static
%make_build

%install
%make_install

%find_lang %{name}

%files -n caja-extension-dropbox
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.*

%files lang -f %{name}.lang

%changelog
