#
# spec file for package combustion
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           combustion
Version:        1.5+git3
Release:        0
Summary:        System for initial configuration of appliances
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/openSUSE/combustion
Source0:        %{name}-%{version}.tar.xz
# This doesn't work with old ignition, conflict with the old firstboot mechanism.
Conflicts:      ignition-dracut-grub2
Requires:       awk
# For VMware guestinfo
Suggests:       open-vm-tools
Requires:       (gzip if open-vm-tools)
BuildArch:      noarch

%description
Combustion is a minimal module for dracut, which runs a user provided script on
the first boot of a transactional system.

You can use this to create additional files, install packages, set up devices
or even re-partition the hard disk. The configuration can be provided as a
shell script, loaded from an external storage media and is run during boot in a
new system snapshot. On success, the system will directly boot into that new
snapshot, so that no reboot is needed.

%prep
%autosetup -p1

%build

%install
%make_install

%post
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/dracut/
%dir %{_prefix}/lib/dracut/modules.d/
# Also used by ignition. Could be split into a separate package,
# but ignition depends on combustion anyway.
%{_prefix}/lib/dracut/modules.d/30firstboot/
%{_prefix}/lib/dracut/modules.d/35combustion/

%changelog
