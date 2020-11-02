#
# spec file for package selinux-autorelabel
#
# Copyright (c) 2020 SUSE LLC
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

Name:           selinux-autorelabel
Version:        3.1
Release:        0
Summary:        Systemd services to relabel SELinux labels
License:        GPL-2.0-only
Source1:        selinux-autorelabel
Source2:        selinux-autorelabel.service
Source3:        selinux-autorelabel-mark.service
Source4:        selinux-autorelabel.target
Source5:        selinux-autorelabel-generator.sh
Requires:       policycoreutils >= 3.1
BuildArch:      noarch

%description
This package contains the systemd target, service files and generator
to auto-relabel a SELinux system.

%prep

%build

%install
mkdir -p %{buildroot}%{_libexecdir}/selinux/
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_systemdgeneratordir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_libexecdir}/selinux/
install -m 644 -p %{SOURCE2} %{buildroot}%{_unitdir}/
install -m 644 -p %{SOURCE3} %{buildroot}%{_unitdir}/
install -m 644 -p %{SOURCE4} %{buildroot}%{_unitdir}/
install -m 755 -p %{SOURCE5} %{buildroot}%{_systemdgeneratordir}/

%files
%dir %{_libexecdir}/selinux/
%{_libexecdir}/selinux/selinux-autorelabel
%{_unitdir}/selinux-autorelabel-mark.service
%{_unitdir}/selinux-autorelabel.service
%{_unitdir}/selinux-autorelabel.target
%dir %{_systemdgeneratordir}
%{_systemdgeneratordir}/selinux-autorelabel-generator.sh

%changelog
