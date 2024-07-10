#
# spec file for package nautilus-dropbox
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%global nautilus_extdir %( pkg-config libnautilus-extension-4 --variable extensiondir )
Name:           nautilus-dropbox
Version:        2020.03.04
Release:        0
Summary:        Dropbox client integrated into Nautilus
License:        GPL-3.0-or-later AND CC-BY-ND-3.0
Group:          Productivity/File utilities
URL:            https://www.dropbox.com
Source:         https://www.dropbox.com/download?dl=packages/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE 98.patch dimstar@opensuse.org -- Hack together something to accept GNOME 40 version schemes
Patch0:         https://patch-diff.githubusercontent.com/raw/dropbox/nautilus-dropbox/pull/98.patch
# PATCH-FIX-UPSTREAM 105.patch -- Port to libnautilus-extension-4
Patch1:         https://patch-diff.githubusercontent.com/raw/dropbox/nautilus-dropbox/pull/105.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gobject-introspection
BuildRequires:  python3-docutils
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43.rc

%description
Dropbox is a free service that lets you bring your photos, docs, and videos anywhere
and share them easily. Never email yourself a file again!

%package -n dropbox-cli
Summary:        Dropbox command line interface
Group:          Productivity/File utilities
Requires:       python3-gpg
Requires:       python3-gobject-Gdk
Provides:       dropbox = %{version}
Obsoletes:      dropbox <= 2015.10.28

%description -n dropbox-cli
Dropbox is a free service that lets you bring your photos, docs, and videos anywhere
and share them easily. Never email yourself a file again!

This package provides a basic dropbox command line interface for desktop and downloads a proprietary dropbox client.

%package -n nautilus-extension-dropbox
Summary:        Dropbox client integrated into Nautilus
Group:          Productivity/File utilities
Requires:       dropbox >= %{version}
Supplements:    (nautilus and dropbox-cli)

%description -n nautilus-extension-dropbox
Dropbox is a free service that lets you bring your photos, docs, and videos anywhere
and share them easily. Never email yourself a file again!

This package integrates dropbox seamless into nautilus.

%prep
%autosetup -p1

%build
# Needed for patch0
autoreconf -fiv
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

sed -i '1s|env python|python|' %{buildroot}%{_bindir}/dropbox

%files -n dropbox-cli
%license COPYING
%doc ChangeLog
%{_bindir}/dropbox
%{_datadir}/applications/dropbox.desktop
%{_datadir}/icons/hicolor/*/apps/dropbox.png
%{_mandir}/man1/dropbox.1%{?ext_man}
%{_datadir}/%{name}/

%files -n nautilus-extension-dropbox
%license COPYING
%doc ChangeLog
%{nautilus_extdir}/libnautilus-dropbox.so

%changelog
