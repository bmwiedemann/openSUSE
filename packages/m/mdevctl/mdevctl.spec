#
# spec file for package mdevctl
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


Name:           mdevctl
Version:        1.4.0
Release:        0
Summary:        Mediated device management and persistence utility
License:        LGPL-2.1-or-later
URL:            https://github.com/mdevctl/mdevctl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(udev)

%description
mdevctl is a utility for managing and persisting devices in the mediated device
framework of the Linux kernel. Mediated devices are sub-devices of a parent
device (e.g. a vGPU) which can be dynamically created and potentially used by
drivers like vfio-mdev for assignment to virtual machines.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
%{make_install}

%check
export MDEVCTL_LOG=debug RUST_BACKTRACE=full
%{cargo_test}

%files
%license COPYING
%doc README.md
%{_sbindir}/mdevctl
%{_sbindir}/lsmdev
%{_udevrulesdir}/60-mdevctl.rules
%dir %{_sysconfdir}/mdevctl.d
%dir %{_prefix}/lib/mdevctl
%dir %{_prefix}/lib/mdevctl/scripts.d
%dir %{_prefix}/lib/mdevctl/scripts.d/callouts
%dir %{_prefix}/lib/mdevctl/scripts.d/notifiers
%{_mandir}/man8/mdevctl.8%{?ext_man}
%{_mandir}/man8/lsmdev.8%{?ext_man}
%{_datadir}/bash-completion/completions/mdevctl
%{_datadir}/bash-completion/completions/lsmdev

%changelog
