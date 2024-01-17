#
# spec file for package signon-ui
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


# webengine branch
%define commit 4368bb77d9d1abc2978af514225ba4a42c29a646

Name:           signon-ui
Version:        0.17+20171022
Release:        0
Summary:        Single Sign On UI
License:        GPL-3.0-only
Group:          System/GUI/Other
Url:            https://gitlab.com/accounts-sso/signon-ui
Source:         https://gitlab.com/accounts-sso/signon-ui/-/archive/%{commit}/signon-ui-%{commit}.tar.bz2
# Patches for upstream, but upstream is dead
Patch1:         0001-Fix-WebEngine-cache-directory-path.patch
Patch2:         0001-Reintroduce-the-username-field-reading-with-webkit-o.patch
BuildRequires:  libaccounts-qt5-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  signon-plugins-devel
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires:       libQt5WebChannel5-imports

%description
This package contains the user interface for the signond Single Sign On service.

%prep
%setup -q -n %{name}-%{commit}
%autopatch -p1

# Don't build tests
sed -i '/tests/d' signon-ui.pro

# Fix libdir
sed -i 's/\/lib/\/%{_lib}/g' common-installs-config.pri

%build
%qmake5 \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%make_jobs

%install
%qmake5_install
# The .desktop file is useless
rm -rf %{buildroot}%{_datadir}/applications

%files
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/com.canonical.indicators.webcredentials.service
%{_datadir}/dbus-1/services/com.nokia.singlesignonui.service

%changelog
