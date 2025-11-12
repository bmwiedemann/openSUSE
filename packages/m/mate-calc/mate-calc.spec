#
# spec file for package mate-calc
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


%define _version 1.28

Name:           mate-calc
Version:        1.28.0
Release:        0
Summary:        MATE Desktop calculator application
License:        GPL-2.0-or-later
URL:            https://mate-desktop.org/
Group:          system/GUI/Other
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  mate-common >= %{_version}
BuildRequires:  mpc-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mpfr)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
mate-calc is a calculator application that was part of the
OpenWindows Deskset of the Solaris 8 operating system.
It incorporates multiple precision arithmetic packages based on the
work of Professor Richard Brent.

%lang_package

%prep
%setup -q

%build
%if %{pkg_vcmp gettext-devel >= 0.24.1}
export ACLOCAL_PATH=/usr/share/gettext/m4/
%endif
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/help/*/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-cmd.1%{?ext_man}

%files lang -f %{name}.lang
%exclude %{_datadir}/help/*

%changelog
