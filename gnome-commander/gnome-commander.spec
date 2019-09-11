#
# spec file for package gnome-commander
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


Name:           gnome-commander
Version:        1.10.2
Release:        0
Summary:        A file manager for the GNOME desktop environment
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://gcmd.github.io/
Source:         http://download.gnome.org/sources/gnome-commander/1.10/%{name}-%{version}.tar.xz
BuildRequires:  chmlib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  python-devel >= 2.5
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(exiv2) >= 0.14
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gnome-keyring-1) >= 2.22
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:  pkgconfig(libgnome-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libgnomeui-2.0) >= 2.4.0
BuildRequires:  pkgconfig(libgsf-1) >= 1.12.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.18
BuildRequires:  pkgconfig(taglib) >= 1.4
Recommends:     %{name}-doc
Recommends:     %{name}-lang
# For xdg-su
Recommends:     xdg-utils

%description
GNOME Commander is a "two-pane" graphical file manager for the Linux
desktop using GNOME libraries. In addition to basic file manager
functions, the program is also an FTP client and can browse SMB
networks.

%package doc
Summary:        A file manager for the GNOME desktop environment -- Documentation files
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
GNOME Commander is a "two-pane" graphical file manager for the Linux
desktop using GNOME libraries. In addition to basic file manager
functions, the program is also an FTP client and can browse SMB
networks.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure\
	--disable-static\
	--without-unique
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_datadir} -size 0 -delete
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.gschema.xml
%{_datadir}/pixmaps/*.svg
%{_datadir}/pixmaps/gnome-commander
%{_libdir}/gnome-commander
%{_mandir}/man1/gnome-commander.1%{ext_man}

%files doc
%dir %{_datadir}/help
%dir %{_datadir}/help/C
%doc %{_datadir}/help/C/%{name}

%files lang -f %{name}.lang

%changelog
