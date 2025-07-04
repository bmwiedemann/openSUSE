#
# spec file for package bolt
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


%global _hardened_build 1
Name:           bolt
Version:        0.9.10
Release:        0
Summary:        Thunderbolt 3 device manager
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://gitlab.freedesktop.org/bolt/bolt
Source0:        https://gitlab.freedesktop.org/bolt/bolt/-/archive/%{version}/bolt-%{version}.tar.bz2
BuildRequires:  asciidoc
BuildRequires:  c_compiler
BuildRequires:  meson >= 0.60
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(udev)

%description
Userspace system daemon to enable security levels for Thunderbolt 3
on GNU/Linux.

%package        tools
Summary:        Bolt Tools
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains optional tools from the Bolt
software framework.

%prep
%autosetup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

# move polkit rules to doc folder: the wheel group does not have special
# meaning on SUSE based distros
mkdir -p %{buildroot}/%{_docdir}/bolt/
mv %{buildroot}%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules %{buildroot}/%{_docdir}/bolt/

%preun
%service_del_preun bolt.service

%post
%service_add_post bolt.service

%postun
%service_del_postun bolt.service

%pre
%service_add_pre bolt.service

%files
%doc README.md INSTALL.md BUGS.md
%license COPYING
%{_mandir}/man8/boltd.8%{?ext_man}
%{_libexecdir}/boltd
%{_unitdir}/bolt.service
%{_datadir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_udevrulesdir}/90-bolt.rules
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
%{_docdir}/bolt/org.freedesktop.bolt.rules

%files tools
%{_bindir}/boltctl
%{_mandir}/man1/boltctl.1%{?ext_man}

%changelog
