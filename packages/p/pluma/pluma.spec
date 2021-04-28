#
# spec file for package pluma
#
# Copyright (c) 2021 SUSE LLC
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


%define typelib typelib-1_0-Pluma-1_0
%define _version 1.24

Name:           pluma
Version:        1.24.2
Release:        0
Summary:        Text editor for the MATE desktop
License:        GPL-2.0-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source99:       https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  fdupes
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(sm)
Requires:       mate-desktop-gsettings-schemas
%glib2_gsettings_schema_requires

%description
Pluma is a small, but powerful text editor designed specifically
for the MATE desktop. It has most standard text editor functions
and fully supports international text in Unicode. Advanced features
include syntax highlighting and automatic indentation of source
code, printing and editing of multiple documents in one window.

Pluma is extensible through a plugin system, which currently
includes support for spell checking, comparing files, viewing VCS
ChangeLogs, and adjusting indentation levels.

%package devel
Summary:        Small and lightweight UTF-8 text editor
Requires:       %{name} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(gtksourceview-3.0)

%description devel
pluma is a small, but powerful text editor designed specifically
for the MATE desktop. It has most standard text editor functions
and fully supports international text in Unicode. Advanced features
include syntax highlighting and automatic indentation of source
code, printing and editing of multiple documents in one window.

%package -n %{typelib}
Summary:        Small and lightweight UTF-8 text editor introspection

%description -n %{typelib}
pluma is a small, but powerful text editor designed specifically
for the MATE desktop. It has most standard text editor functions
and fully supports international text in Unicode. Advanced features
include syntax highlighting and automatic indentation of source
code, printing and editing of multiple documents in one window.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/help/C/%{name}/

%files devel
%doc %{_datadir}/gtk-doc/html/
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Pluma-1.0.gir

%files -n %{typelib}
%{_libdir}/girepository-1.0/Pluma-1.0.typelib

%files lang -f %{name}.lang

%changelog
