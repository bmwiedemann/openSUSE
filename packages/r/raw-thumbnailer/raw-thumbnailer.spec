#
# spec file for package raw-thumbnailer
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           raw-thumbnailer
Version:        48.0.0+git5.e8f0079
Release:        0
Summary:        RAW images thumbnailer for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://libopenraw.freedesktop.org
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Summary(ru):    Генератор миниатюр RAW изображений для GNOME
BuildRequires:  cargo
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libopenraw-gnome-0.3)
Requires:       shared-mime-info >= 0.90

%description
A lightweight and fast thumbnailer used by Nautilus for digital camera RAW files.

%description -l ru
Быстрое и не требовательное приложение, используемое Nautilus для создание миниатюр RAW файлов, полученных с цифровых камер.

%prep
%autosetup -p1 -a1

%build
%meson -Dprofile=release
%meson_build

%install
%meson_install

%check
%meson_test

%files
%defattr(-,root,root)
%license COPYING
%doc NEWS ChangeLog
%{_bindir}/raw-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/raw.thumbnailer
%{_datadir}/mime/packages/raw-thumbnailer.xml

%changelog
