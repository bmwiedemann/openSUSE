#
# spec file for package docky
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           docky
Version:        2.2.1.1
Release:        0
Summary:        A Dock Application
License:        GPL-3.0+
Group:          Productivity/Other
Url:            https://launchpad.net/docky
Source:         http://launchpad.net/docky/2.2/%{version}/+download/%{name}-%{version}.tar.xz
# PATCH-HACK-OPENSUSE docky-mono-3.10.0.patch dimstar@opensuse.org -- Work around build issues with mono 3.10.0; no idea why it would not like the original code
Patch0:         docky-mono-3.10.0.patch
BuildRequires:  fdupes
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  intltool
BuildRequires:  mono
BuildRequires:  mono-devel
BuildRequires:  pkgconfig(dbus-sharp-2.0) >= 0.7
BuildRequires:  pkgconfig(dbus-sharp-glib-2.0) >= 0.5
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.14.3
BuildRequires:  pkgconfig(gio-sharp-2.0)
BuildRequires:  pkgconfig(gkeyfile-sharp)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gnome-keyring-sharp-1.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.14.3
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(libwnck-1.0) >= 2.20
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(mono-addins-gui)
BuildRequires:  pkgconfig(mono-addins-setup)
BuildRequires:  pkgconfig(mono-cairo)
BuildRequires:  pkgconfig(notify-sharp)
# docky brings an own, patched version of wnck-sharp, the .config file references libwnck-1.so.22
Requires:       libwnck-1-22
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%else
%define suse_update_desktop_file true
%endif
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{gconf_schemas_prereq}

%description
Docky is a full fledged dock application that makes opening common applications and managing windows easier and quicker. Docky is fully integrated into the GNOME Desktop and features a no non-sense approach to configuration and usage. It just works.

%package devel
Summary:        A Dock Application
Group:          Development/Languages/Mono
Requires:       %{name} = %version

%description devel
Docky is a full fledged dock application that makes opening common applications and managing windows easier and quicker. Docky is fully integrated into the GNOME Desktop and features a no non-sense approach to configuration and usage. It just works.

%lang_package
%prep
%setup -q
%patch0 -p1

%build
%configure --disable-schemas-install
make

%install
%makeinstall
# Directories SUSE doesn't support
%__rm -rf %{buildroot}%{_datadir}/locale/fil
# System-wide autostart can conflict w/ user autostart
%__rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
%suse_update_desktop_file %{name} DesktopUtility
%fdupes -s %{buildroot}
%find_lang %{name}
%find_gconf_schemas

%pre -f %{name}.schemas_pre

%posttrans -f %{name}.schemas_posttrans

%preun -f %{name}.schemas_preun

%files -f %{name}.schemas_list
%defattr(-, root, root)
%doc COPYING AUTHORS COPYRIGHT
%doc %{_mandir}/man1/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/%{name}

%files lang -f %{name}.lang

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/%{name}.*.pc

%changelog
