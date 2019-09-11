#
# spec file for package raw-thumbnailer
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


Name:           raw-thumbnailer
Version:        3.0.0
Release:        0
Summary:        RAW images thumbnailer for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Url:            http://libopenraw.freedesktop.org
Source0:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Summary(ru):	Генератор миниатюр RAW изображений для GNOME
# PATCH-FEATURE-UPSTREAM raw-thumbnailer-3.0.0-add-Panasonic.patch svalx@svalx.net -- Add support for image/x-panasonic-raw and image/x-panasonic-raw2.
Patch0:         raw-thumbnailer-3.0.0-add-Panasonic.patch
# PATCH-FIX-OPENSUSE raw-thumbnailer-3.0.0-mime-data-remove.patch svalx@svalx.net -- remove mime type definitions - it is duplicate of definition in shared-mime-info package.
Patch1:         raw-thumbnailer-3.0.0-mime-data-remove.patch
BuildRequires:  intltool
BuildRequires:  libopenraw-devel
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
Requires:       shared-mime-info >= 0.90
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A lightweight and fast thumbnailer used by Nautilus for digital camera RAW files.

%description -l ru
Быстрое и не требовательное приложение, используемое Nautilus для создание миниатюр RAW файлов, полученных с цифровых камер.

%prep
%setup -q
if pkg-config --exists libopenraw-gnome-0.1; then
  sed -i "s/libopenraw-gnome-1.0/libopenraw-gnome-0.1/g" configure*
fi
%patch0
%patch1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%doc NEWS ChangeLog
%{_bindir}/raw-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/raw.thumbnailer

%changelog
