#
# spec file for package patterns-cockpit
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


%bcond_with betatest
Name:           patterns-cockpit
Version:        16.0
Release:        0
Summary:        Pattern for Cockpit, a web based remote system management interface
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name.rpmlintrc
ExclusiveArch:  x86_64 %arm32 aarch64 ppc64le s390x riscv64
Provides:       pattern() = cockpit
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9060
Provides:       pattern-visible()
Obsoletes:      patterns-microos-cockpit
Provides:       patterns-microos-cockpit
Obsoletes:      patterns-base-cockpit
Provides:       patterns-base-cockpit
Requires:	cockpit
Requires:       cockpit-system
Requires:       cockpit-ws
Requires:       (cockpit-kdump if kdump)
Requires:       (cockpit-podman if podman)
Requires:       (cockpit-machines if libvirt-daemon-qemu)
Requires:       cockpit-networkmanager
Requires:       (cockpit-tukit if transactional-update)
Requires:       cockpit-storaged
Requires:       (cockpit-selinux if selinux-tools)
Requires:       (cockpit-packages if PackageKit)
Requires:       (cockpit-packagekit if PackageKit)
Requires:       cockpit-repos
Requires:       (cockpit-subscriptions if suseconnect-ng)
Requires:       (cockpit-firewalld if firewalld)
Requires:       sudo
BuildRequires:  patterns-rpm-macros
%pattern_advsysmgmt


%description
Packages required to run the Cockpit system management service.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-cockpit/
PATTERNS='cockpit'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/patterns-cockpit/${i}.txt
done

%files
%dir %{_docdir}/patterns-cockpit
%{_docdir}/patterns-cockpit/cockpit.txt

%changelog
