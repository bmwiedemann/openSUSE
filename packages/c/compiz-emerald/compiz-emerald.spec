#
# spec file for package compiz-emerald
#
# Copyright (c) 2020 SUSE LLC
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


%define _rev    64c02befbf3a2fee2e1a7ab266938f9a
%define _name   emerald
Name:           compiz-emerald
Version:        0.8.18
Release:        0
Summary:        Themeable window decorator for Compiz
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/emerald
Source:         https://gitlab.com/compiz/emerald/uploads/%{_rev}/%{_name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libdecoration) < 0.9
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xrender) >= 0.8.4
Requires:       compiz < 0.9
Recommends:     %{name}-theme-manager >= %{version}
Recommends:     %{name}-themes
Provides:       compiz-decorator = 0.8

%description
Emerald is a themeable window decorator for Compiz.

%lang_package

%package theme-manager
Summary:        Graphical theme manager for Emerald
Requires:       %{name} >= %{version}

%description theme-manager
Emerald is a themeable window decorator for Compiz.

This package contains a graphical theme manager.

%package devel
Summary:        Development files for compiz-emerald
Requires:       %{name} = %{version}
Requires:       gcc-c++
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(libdecoration) < 0.9
Requires:       pkgconfig(libwnck-3.0)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(xrender) >= 0.8.4

%description devel
Emerald is a themeable window decorator for Compiz.

This package holds the development files for compiz-emerald.

%prep
%setup -q -n %{_name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --with-gtk=3.0        \
  --disable-static      \
  --disable-mime-update
%make_build

%install
%make_install
# /usr/share/mime-info was GNOME 1 infrastructure. These times are long gone
rm -rf %{buildroot}%{_datadir}/mime-info
%suse_update_desktop_file %{_name}-theme-manager DesktopSettings
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/
%find_lang %{_name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{_name}
%{_libdir}/%{_name}/
%{_libdir}/libemeraldengine.so.*
%{_datadir}/%{_name}/
%{_datadir}/icons/hicolor/*/mimetypes/*%{_name}*
%{_datadir}/mime/packages/%{_name}.xml
%{_mandir}/man1/%{_name}.1%{?ext_man}

%files lang -f %{_name}.lang

%files theme-manager
%{_bindir}/%{_name}-theme-manager
%{_datadir}/applications/*%{_name}*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{_name}-theme-manager*
%{_mandir}/man1/%{_name}-theme-manager.1%{?ext_man}

%files devel
%{_includedir}/%{_name}/
%{_libdir}/libemeraldengine.so
%{_libdir}/pkgconfig/%{_name}*.pc

%changelog
