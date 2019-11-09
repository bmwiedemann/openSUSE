#
# spec file for package ibus-chewing
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


Name:           ibus-chewing
Version:        1.6.1
Release:        0
Summary:        The Chewing engine for IBus input platform
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/definite/ibus-chewing
Source0:        https://github.com/definite/ibus-chewing/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  cmake-fedora-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gob2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(chewing)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(x11)

%description
The Chewing engine for IBus platform. It provides Chinese input method from
libchewing.
新酷音輸入法

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DLIBEXEC_DIR=%{_libdir}/ibus

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc/ibus-chewing

%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc USER-GUIDE AUTHORS INSTALL ChangeLog README.md RELEASE-NOTES.txt
%license COPYING
%{_libdir}/ibus
%{_datadir}/%{name}
%{_datadir}/ibus
%{_datadir}/applications/ibus-setup-chewing.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.IBus.Chewing.gschema.xml

%changelog
