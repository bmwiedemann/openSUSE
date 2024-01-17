#
# spec file for package debianutils
#
# Copyright (c) 2023 SUSE LLC
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


Name:           debianutils
Version:        5.4
Release:        0
Summary:        Miscellaneous utilities specific to Debian
License:        GPL-2.0-only
Group:          System/Shells
URL:            https://packages.debian.org/%{name}
Source:         http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.orig.tar.xz

%description
* add-shell: add a shell to /etc/shells
* ischroot: etects if it is currently running in a chroot
* run-parts: run scripts or programs in a directory
* remove-shell: remove a shell to /etc/shells
* update-shells: update the list of valid login shells

%prep
%autosetup

%build
%configure
%make_build

%install
# savelog is under SMAIL license, don't install
install -Dt %{buildroot}%{_bindir} ischroot
install -Dt %{buildroot}%{_sbindir} add-shell
install -Dt %{buildroot}%{_sbindir} remove-shell
install -Dt %{buildroot}%{_bindir} run-parts
install -Dt %{buildroot}%{_sbindir} update-shells

install -m 0644 -Dt %{buildroot}%{_mandir}/man1 ischroot.1
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 add-shell.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 remove-shell.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 run-parts.8
install -m 0644 -Dt %{buildroot}%{_mandir}/man8 update-shells.8

%files
%{_bindir}/ischroot
%{_sbindir}/add-shell
%{_sbindir}/remove-shell
%{_bindir}/run-parts
%{_sbindir}/update-shells
%{_mandir}/man1/ischroot.1%{?ext_man}
%{_mandir}/man8/add-shell.8%{?ext_man}
%{_mandir}/man8/remove-shell.8%{?ext_man}
%{_mandir}/man8/run-parts.8%{?ext_man}
%{_mandir}/man8/update-shells.8%{?ext_man}

%changelog
