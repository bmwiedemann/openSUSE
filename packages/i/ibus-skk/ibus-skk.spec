#
# spec file for package ibus-skk
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


Name:           ibus-skk
Version:        1.4.3
Release:        0
Summary:        Japanese SKK input method for ibus
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
Url:            https://github.com/ueno/ibus-skk
Source0:        https://github.com/ueno/ibus-skk/releases/download/ibus-skk-%{version}/ibus-skk-%{version}.tar.xz
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(vapigen) >= 0.16
Requires:       ibus

%description
A Japanese Simple Kana Kanji Input Method Engine for ibus.


%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file ibus-setup-skk Utility DesktopUtility System
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING
%{_datadir}/ibus-skk
%{_datadir}/applications/ibus-setup-skk.desktop
%{_libexecdir}/ibus-*-skk
%{_datadir}/ibus/component/skk.xml

%changelog
