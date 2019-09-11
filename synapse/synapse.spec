#
# spec file for package synapse
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


Name:           synapse
Version:        0.2.99.4
Release:        0
Summary:        A semantic launcher for GNOME
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://launchpad.net/synapse-project
Source:         https://launchpad.net/synapse-project/0.3/%{version}/+download/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.14.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.5.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkhotkey-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.10.0
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(zeitgeist-2.0)
Recommends:     %{name}-lang

%description
Synapse is a semantic launcher written in Vala that you can use to start
applications as well as find and access relevant documents and files by
making use of the Zeitgeist engine.

%lang_package

%prep
%autosetup

%build
%configure \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
%suse_update_desktop_file %{name} X-SuSE-DesktopUtility

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%license COPYING COPYING.GPL2
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
