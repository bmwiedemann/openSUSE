#
# spec file for package mate-calc
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


%define _version 1.23
Name:           mate-calc
Version:        1.23.0
Release:        0
Summary:        MATE Desktop calculator application
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
# set to version macro when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500
BuildRequires:  python2-libxml2-python
%else
BuildRequires:  libxml2-python
%endif

%description
mate-calc is a calculator application that was part of the
OpenWindows Deskset of the Solaris 8 operating system.
It incorporates multiple precision arithmetic packages based on the
work of Professor Richard Brent.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/help/C/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-cmd.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
