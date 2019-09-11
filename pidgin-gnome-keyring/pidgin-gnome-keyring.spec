#
# spec file for package pidgin-gnome-keyring
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pidgin-gnome-keyring
Version:        2.0
Release:        0
Summary:        Save pidgin passwords to the system keyring instead of as plaintext
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/aebrahim/pidgin-gnome-keyring
Source:         https://github.com/aebrahim/pidgin-gnome-keyring/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/aebrahim/pidgin-gnome-keyring/pull/13
Patch0:         install.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(purple)

%description
Pidgin usually stores passwords as plaintext. This plugin instead
saves all passwords to the system keyring, which some would argue
is a more secure form of password storage.

%package -n libpurple-plugin-gnome-keyring
Summary:        GNOME system keyring plugin for Purple
Group:          Productivity/Networking/Instant Messenger

%description -n libpurple-plugin-gnome-keyring
After the plugin is enabled, whenever an account with a pidgin-stored
password signs on, its password will automatically be saved to the
keyring and removed from the plaintext accounts.xml file.

%prep
%setup -q
%patch0 -p1
echo "%{version}" > VERSION

%build
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libpurple-plugin-gnome-keyring
%defattr(-,root,root)
%doc deb_copyright README.md
%{_libdir}/purple-2/gnome-keyring.so

%changelog
