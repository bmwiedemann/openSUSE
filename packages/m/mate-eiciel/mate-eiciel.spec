#
# spec file for package mate-eiciel
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


Name:           mate-eiciel
Version:        1.20.1
Release:        0
Summary:        ACL viewer and editor for MATE
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/darkshram/mate-eiciel
Source:         https://github.com/darkshram/mate-eiciel/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE mate-eiciel-gtk-3.20.patch -- Restore GLib 2.48 and GTK+ 3.20 support.
Patch0:         mate-eiciel-gtk-3.20.patch
BuildRequires:  autoconf-archive
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  mate-common
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libcaja-extension) >= 1.18.0
Recommends:     %{name}-lang

%description
MATE eiciel is a Graphical editor for access control lists (ACLs)
and extended attributes (xattr), either as an extension within
Caja, or as a standalone utility.

%package -n caja-extension-eiciel
Summary:        Caja extension for the ACL viewer and editor
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(caja:%{name})

%description -n caja-extension-eiciel
A Caja extension that allows viewing and editing ACL permissions.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -r org.mate-desktop.mate-eiciel System Filesystem
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mate-eiciel
%{_datadir}/mate-eiciel/
%{_datadir}/applications/*mate-eiciel.desktop
%{_datadir}/icons/hicolor/*/apps/mate-eiciel.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*mate-eiciel.appdata.xml
%{_mandir}/man1/mate-eiciel.1%{?ext_man}
%{_datadir}/help/C/%{name}/

%files -n caja-extension-eiciel
%{_libdir}/caja/extensions-2.0/libeiciel-caja.so

%files lang -f %{name}.lang

%changelog
