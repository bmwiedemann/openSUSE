#
# spec file for package ntsync-autoload
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


Name:           ntsync-autoload
Version:        0.0.2
Release:        0
Summary:        Automatically load the ntsync kernel module
License:        MIT
URL:            https://www.opensuse.org/
Source1:        70-ntsync.rules
Source2:        README.SUSE
BuildRequires:  pkgconfig(systemd)
BuildArch:      noarch
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
Recommends:     ntsync-autoload-udev-rules = %{version}
%description
Automatically load the ntsync kernel module.

The module allows wine to handle the translations of some Windows specific
primitives in a more efficient way.

%package udev-rules
Summary:        udev rules for tighter permissions of /dev/ntsync
Requires:       ntsync-autoload = %{version}
%description udev-rules
Automatically load the ntsync kernel module.

The module allows wine to handle the translations of some Windows specific
primitives in a more efficient way.

This package provides udev rules to restrict /dev/ntsync to locally logged in users.

%prep
cp %{SOURCE2} .

%build

%install
install -D -d -m 0755 %{buildroot}%{_modulesloaddir}
echo ntsync > %{buildroot}%{_modulesloaddir}/enable-ntsync.conf
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} ${RPM_SOURCE_DIR}/70-ntsync.rules

%files
%doc README.SUSE
%dir %{_modulesloaddir}/
%{_modulesloaddir}/enable-ntsync.conf

%files udev-rules
%doc README.SUSE
%{_udevrulesdir}/70-ntsync.rules

%changelog
