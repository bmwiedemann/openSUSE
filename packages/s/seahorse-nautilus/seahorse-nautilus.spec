#
# spec file for package seahorse-nautilus
#
# Copyright (c) 2022 SUSE LLC
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


Name:           seahorse-nautilus
Version:        3.11.92+95
Release:        0
Summary:        Extension for nautilus which allows encryption and decryption of files
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://live.gnome.org/Seahorse
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gpgme-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cryptui-0.0) >= 3.9.90
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3) > 3.4.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43.rc

%description
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%package -n nautilus-extension-seahorse
Summary:        Extension for nautilus which allows encryption and decryption of files
Group:          Productivity/Security
Supplements:    (seahorse and nautilus)
# For people looking for the upstream name, and to make lang package
# installable
Provides:       %{name} = %{version}

%description -n nautilus-extension-seahorse
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D check-compatible-gpg=false \
	-D libnotify=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%files -n nautilus-extension-seahorse
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md THANKS
%{_bindir}/seahorse-tool
%{_libdir}/nautilus/extensions-4/libnautilus-seahorse.so
%{_datadir}/applications/seahorse-pgp*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.window.gschema.xml
%{_mandir}/man1/seahorse-tool.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
