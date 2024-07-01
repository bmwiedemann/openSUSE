#
# spec file for package xfce4-kbdleds-plugin
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


Name:           xfce4-kbdleds-plugin
Version:        0.3.0
Release:        0
Summary:        Keyboard LEDs plugin for the Xfce panel
License:        GPL-2.0-only
URL:            https://github.com/oco2000/xfce4-kbdleds-plugin
Source:         https://github.com/oco2000/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)

%description
This plugin allows to display the keyboard LED state in the Xfce panel

%lang_package

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/*.la

%find_lang %{name} %{name}.lang %{?no_lang_C}

%files
%license COPYING
%doc README.md
%{_libdir}/xfce4/panel/plugins/libkbdleds.so
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/xfce4/panel/plugins/kbdleds.desktop

%files lang -f %{name}.lang

%changelog
