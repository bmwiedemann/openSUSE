#
# spec file for package ibus-chewing
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ibus-chewing
Version:        2.1.4
Release:        0
Summary:        The Chewing engine for IBus input platform
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/chewing/ibus-chewing/
Source0:        https://github.com/chewing/ibus-chewing/releases/download/v%{version}/%{name}-%{version}-Source.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 2.6.2
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(chewing)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(x11)

%description
The Chewing engine for IBus platform. It provides Chinese input method from
libchewing.
新酷音輸入法

%prep
%autosetup -p1 -n %{name}-%{version}-Source

%build
%cmake -DLIBEXEC_DIR=%{_ibus_libexecdir}

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc/packages/ibus-chewing

%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc USER-GUIDE AUTHORS INSTALL ChangeLog-1.x CHANGELOG.md README.md
%license COPYING
%{_libexecdir}/ibus-*
%{_datadir}/%{name}
%{_datadir}/ibus
%{_datadir}/applications/ibus-setup-chewing.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.IBus.Chewing.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.IBus.Chewing.Setup.svg

%changelog
