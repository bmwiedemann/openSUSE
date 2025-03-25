#
# spec file for package usermode
#
# Copyright (c) 2025 SUSE LLC
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


Name:           usermode
Version:        1.114
Release:        0
Summary:        Tools for certain user account management tasks
License:        LGPL-2.0-or-later
URL:            https://pagure.io/usermode
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  selinux-policy-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libuser)
BuildRequires:  pkgconfig(pam)

%description
usermode contains the userhelper program, which can be used to allow configured
programs to be run with superuser privileges by ordinary users, and several
graphical tools for users:
* userinfo allows users to change their finger information. usermount lets
* users mount, unmount, and format filesystems. userpasswd allows users to
  change their passwords.

%lang_package

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
./autogen.sh
%configure \
  --with-selinux \
  --with-fexecve \
  --without-efence \
  --enable-debug \
  --enable-deprecation \
  --without-gtk
%make_build

%install
%make_install
%find_lang %{name}

%files
%license COPYING
%doc ChangeLog NEWS README
%{_bindir}/consolehelper
%{_sbindir}/userhelper
%{_mandir}/man?/consolehelper.?%{?ext_man}
%{_mandir}/man?/userhelper.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
