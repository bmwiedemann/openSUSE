#
# spec file for package tik
#
# Copyright (c) 2024 SUSE LLC
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


Name:           tik
Version:        1.0.6
Release:        0
Summary:        Transactional Installation Kit
License:        MIT
URL:            https://github.com/sysrich/tik
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       coreutils
Requires:       dbus-1-tools
Requires:       efibootmgr
Requires:       grep
Requires:       pkexec
Requires:       pv
Requires:       tik-config
Requires:       util-linux
Requires:       util-linux-systemd
Requires:       xz
Requires:       zenity

%description
A toolkit for deploying Operating System images to UEFI hardware from a USB stick.

%package config-generic
Summary:        Generic configuration for tik
Requires:       tik
Conflicts:      tik-config
Provides:       tik-config

%description config-generic
Generic configuration for tik. To be used for "distribution neutral" installation media or debug/experimentation.

%package module-welcome
Summary:        Welcome module for tik
Requires:       tik

%description module-welcome
Welcome module for tik. Greets the user before installation.

%package module-mig
Summary:        Migration module for tik
Requires:       tik

%description module-mig
Migration module for tik. Detects existing btrfs /home subvolumes and offers to backup/restore it using the tik USB stick.

%prep
%autosetup

%build

%install
install -D -m 755 usr/bin/tik %{buildroot}%{_bindir}/tik
install -D -m 644 usr/lib/tik/config %{buildroot}%{_prefix}/lib/tik/config
install -D -m 644 usr/lib/tik/lib/tik-functions %{buildroot}%{_prefix}/lib/tik/lib/tik-functions
install -D -m 644 etc/tik/config %{buildroot}%{_sysconfdir}/tik/config
install -d %{buildroot}%{_prefix}/lib/tik/modules/pre
install -d %{buildroot}%{_prefix}/lib/tik/modules/post
install -d %{buildroot}%{_prefix}/lib/tik/img
install -d %{buildroot}%{_sysconfdir}/tik/modules/pre
install -d %{buildroot}%{_sysconfdir}/tik/modules/post

install -D -m 644 usr/lib/tik/modules/pre/10-welcome %{buildroot}%{_prefix}/lib/tik/modules/pre

install -D -m 644 usr/lib/tik/modules/pre/20-mig %{buildroot}%{_prefix}/lib/tik/modules/pre
install -D -m 644 usr/lib/tik/modules/post/20-mig %{buildroot}%{_prefix}/lib/tik/modules/post

%files
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/tik
%dir %{_prefix}/lib/tik/modules
%dir %{_prefix}/lib/tik/modules/pre
%dir %{_prefix}/lib/tik/modules/post
%dir %{_prefix}/lib/tik/img
%dir %{_prefix}/lib/tik/lib
%{_prefix}/lib/tik/lib/tik-functions
%{_bindir}/tik

%files config-generic
%{_prefix}/lib/tik/config
%dir %{_sysconfdir}/tik
%dir %{_sysconfdir}/tik/modules
%dir %{_sysconfdir}/tik/modules/pre
%dir %{_sysconfdir}/tik/modules/post
%config(noreplace) %{_sysconfdir}/tik/config

%files module-welcome
%{_prefix}/lib/tik/modules/pre/10-welcome

%files module-mig
%{_prefix}/lib/tik/modules/pre/20-mig
%{_prefix}/lib/tik/modules/post/20-mig

%changelog
