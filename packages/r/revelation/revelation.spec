#
# spec file for package revelation
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


Name:           revelation
Version:        0.5.3
Release:        0
Summary:        Password manager for GNOME
License:        GPL-2.0
Group:          Productivity/Security
Url:            http://revelation.olasagasti.info
Source:         https://github.com/mikelolasagasti/revelation/releases/download/revelation-%{version}/revelation-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM https://github.com/mikelolasagasti/revelation/pull/61
Patch0:         desktop.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool >= 0.35.0
BuildRequires:  perl-XML-Parser
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pwquality
BuildRequires:  gobject-introspection
Requires:       python3-gobject
Requires:       python3-pwquality
Requires:       python3-pycryptodomex
Requires:       python3-gobject-Gdk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Revelation is a password manager. It organizes accounts in
a tree structure, and stores them as AES-encrypted XML files.

%lang_package
%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-schemas-install --disable-desktop-update --disable-mime-update
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%files
%defattr(-, root, root)
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/revelation
%{_datadir}/applications/info.olasagasti.revelation.desktop
%{_datadir}/metainfo/info.olasagasti.revelation.appdata.xml
%{_datadir}/revelation/
%{_datadir}/icons/hicolor/*/apps/info.olasagasti.revelation*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-application-x-revelation.png
%{_datadir}/mime/packages/*
%{python3_sitelib}/revelation/
%{_datadir}/glib-2.0/schemas/org.revelation.gschema.xml

%files lang -f %{name}.lang

%changelog
