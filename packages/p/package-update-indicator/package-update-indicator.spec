#
# spec file for package package-update-indicator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 B1 Systems GmbH, Vohburg, Germany.
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


Name:           package-update-indicator
Version:        5
Release:        0
Summary:        Package update status notification applet
License:        MIT
Group:          System/Daemons
URL:            https://code.guido-berhoerster.org/projects/package-update-indicator
Source:         https://code.guido-berhoerster.org/projects/package-update-indicator/downloads/%{name}-%{version}.tar.gz
Source1:        10_opensuse_update_command.gschema.override
Patch0:         org.guido-berhoerster.code.package-update-indicator.desktop.in.patch
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gettext >= 0.19
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(appindicator3-0.1) >= 12.10.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  pkgconfig(packagekit-glib2) >= 0.8.17
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.105
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
Obsoletes:      pk-update-icon <= 3
Recommends:     gnome-packagekit

%description
The package-update-indicator utility regularly checks for software updates and notifies the user about available updates using desktop notifications and either a status notifier icon or a system tray icon.

%lang_package

%prep
%autosetup

%build
%make_build prefix=%{_prefix} GLIB_COMPILE_SCHEMAS=: CFLAGS="%{optflags}" CC=gcc

%install
%make_install prefix=%{_prefix} GLIB_COMPILE_SCHEMAS=:
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas/
%find_lang %{name} %{?no_lang_C}

%files
%doc README NEWS
%{_sysconfdir}/xdg/autostart/org.guido-berhoerster.code.package-update-indicator.desktop
%{_bindir}/package-update-indicator
%{_bindir}/package-update-indicator-prefs
%{_datadir}/applications/org.guido-berhoerster.code.package-update-indicator.preferences.desktop
%{_datadir}/glib-2.0/schemas/org.guido-berhoerster.code.package-update-indicator.gschema.xml
%{_datadir}/glib-2.0/schemas/10_opensuse_update_command.gschema.override
%{_mandir}/man1/package-update-indicator-prefs.1%{?ext_man}
%{_mandir}/man1/package-update-indicator.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
