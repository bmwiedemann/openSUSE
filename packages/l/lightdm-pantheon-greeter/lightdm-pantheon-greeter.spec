#
# spec file for package lightdm-pantheon-greeter
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


%define         appid io.elementary.greeter
Name:           lightdm-pantheon-greeter
Version:        8.0.1
Release:        0
Summary:        Pantheon's LightDM Login Screen
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/greeter
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-mutter45.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  lightdm
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libmutter-15)
%else
BuildRequires:  pkgconfig(libmutter-13)
%endif
Provides:       lightdm-elementary-greeter = %{version}
Obsoletes:      lightdm-elementary-greeter < %{version}

%description
Pantheon Greeter is a pantheon-styled Login Screen for LightDM.

%lang_package

%prep
%autosetup -N -n greeter-%{version}
%if 0%{?suse_version} < 1600
%patch -P0 -p1
%endif

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}
%find_lang %{appid}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}-compositor
%{_sbindir}/%{appid}
%{_sbindir}/%{appid}-session-manager
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appid}-compositor.gschema.xml
%{_datadir}/lightdm/lightdm.conf.d/40-%{appid}.conf
%config %{_sysconfdir}/lightdm/%{appid}.conf
%{_datadir}/xgreeters/%{appid}.desktop

%files lang -f %{appid}.lang

%changelog
