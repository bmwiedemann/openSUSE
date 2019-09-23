#
# spec file for package seahorse-nautilus
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           seahorse-nautilus
Version:        3.11.92
Release:        0
Summary:        Extension for nautilus which allows encryption and decryption of files
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://live.gnome.org/Seahorse
Source:         http://download.gnome.org/sources/seahorse-nautilus/3.11/%{name}-%{version}.tar.xz
BuildRequires:  gpgme-devel
BuildRequires:  intltool >= 0.35.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cryptui-0.0) >= 3.9.90
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3) > 3.4.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(libnautilus-extension) >= 2.12.0
%glib2_gsettings_schema_requires

%description
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%package -n nautilus-extension-seahorse
Summary:        Extension for nautilus which allows encryption and decryption of files
Group:          Productivity/Security
Recommends:     %{name}-lang
Supplements:    packageand(seahorse:nautilus)
# For people looking for the upstream name, and to make lang package
# installable
Provides:       %{name} = %{version}

%description -n nautilus-extension-seahorse
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%lang_package

%prep
%setup -q
sed -i "s:1.2 1.4 2.0:1.2 1.4 2.0 2.1 2.2:" configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file seahorse-pgp-signature
%suse_update_desktop_file seahorse-pgp-keys
%suse_update_desktop_file seahorse-pgp-encrypted
%find_lang %{name}

%post -n nautilus-extension-seahorse
%desktop_database_post
%glib2_gsettings_schema_post

%postun -n nautilus-extension-seahorse
%desktop_database_postun
%glib2_gsettings_schema_postun

%files -n nautilus-extension-seahorse
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/seahorse-tool
%{_libdir}/nautilus/extensions-3.0/libnautilus-seahorse.so
%{_datadir}/applications/seahorse-pgp*.desktop
%{_datadir}/%{name}/
%{_datadir}/GConf/gsettings/org.gnome.seahorse.nautilus.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.window.gschema.xml
%{_mandir}/man1/seahorse-tool.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
