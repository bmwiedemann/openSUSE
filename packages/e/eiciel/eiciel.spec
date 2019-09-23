#
# spec file for package eiciel
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _libnautilus_extensiondir %(pkg-config --variable extensiondir libnautilus-extension)

Name:           eiciel
Version:        0.9.12.1
Release:        0
Summary:        GNOME ACL viewer and editor
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://rofi.roger-ferrer.org/eiciel/
Source0:        http://rofi.roger-ferrer.org/eiciel/files/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM eiciel-sys-xattr.patch -- <attr/xattr.h> is deprecated, use <sys/xattr.h> instead
Patch0:         eiciel-sys-xattr.patch

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libnautilus-extension) >= 3.0.0
Recommends:     %{name}-lang

%description
Eiciel allows you to visually edit file ACL entries. You can add and
remove users and groups who will be granted permissions through the
graphical interface

%package -n nautilus-eiciel
Summary:        Nautilus ACL viewer and editor extension
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    packageand(eiciel:nautilus)

%description -n nautilus-eiciel
A Nautilus extension that allows viewing and editing ACL permissions.

%lang_package

%prep
%autosetup -p1
sed -i -e 's!attr/xattr\.h!sys/xattr\.h!g' configure
translation-update-upstream

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -r org.roger-ferrer.Eiciel System Filesystem
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%{_bindir}/eiciel
%{_mandir}/man1/eiciel.1%{?ext_man}
%{_datadir}/applications/org.roger-ferrer.Eiciel.desktop
%{_datadir}/eiciel/
%{_datadir}/icons/hicolor/*/apps/eiciel.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.roger-ferrer.Eiciel.appdata.xml

%files -n nautilus-eiciel
%{_libnautilus_extensiondir}/libeiciel-nautilus.so

%files lang -f %{name}.lang

%changelog
