#
# spec file for package pantheon-mail
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


%define         appid io.elementary.mail
Name:           pantheon-mail
Version:        8.0.0
Release:        0
Summary:        A lightweight email reader for the Pantheon desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/mail
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libapparmor)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Provides:       elementary-mail = %{version}
Obsoletes:      elementary-mail < %{version}

%description
Mail is a email reader for Pantheon designed to let you read your email
quickly and effortlessly.

Its interface is based on conversations, so you can easily read an entire
discussion without having to click from message to message.

%package apparmor
Summary:        Apparmor profile for %{name}
BuildArch:      noarch
Supplements:    (%{name} and apparmor-abstractions)

%description apparmor
This package ships only the apparmor profile for %{name}

%lang_package

%prep
%autosetup -n mail-%{version}

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson \
  -Ddocumentation=false
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_libdir}/%{appid}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files apparmor
%config(noreplace) %{_sysconfdir}/apparmor.d/%{appid}

%files lang -f %{appid}.lang

%changelog
