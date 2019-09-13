#
# spec file for package gtk2-engine-murrine
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _name   murrine
Name:           gtk2-engine-murrine
Version:        0.98.2
Release:        0
Summary:        Murrine GTK Theme Engine
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/GUI/XFCE
URL:            http://ftp.gnome.org/pub/GNOME/sources/murrine/
Source:         http://download.gnome.org/sources/murrine/0.98/%{_name}-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  gtk2-devel >= 2.12.0
BuildRequires:  intltool
BuildRequires:  pkgconfig
# Only needed because we don't (and won't) support building xz tarballs by default... See bnc#697467
BuildRequires:  xz

%description
Murrine is a GTK+ 2 theme engine, that uses the Cairo vector drawing
library to render widgets. It features a modern glassy look, is elegant
and clean on the eyes, and is extremely customizable.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --enable-animation
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gtk-2.0/*/engines/*
%dir %{_datadir}/gtk-engines
%{_datadir}/gtk-engines/murrine.xml

%changelog
