#
# spec file for package numad
#
# Copyright (c) 2021 SUSE LLC
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


Name:           numa-preplace
URL:            https://gitlab.suse.de/virtualization/numa-preplace.git
Summary:        Userspace tool for binding VMs to NUMA nodes
License:        LGPL-2.1-only
Group:          System/Daemons
Version:        0.1
Release:        0
Source0:        numa-preplace-0.1.tar.bz2
Obsoletes:      numad <= 0.5.20130522

%description
Once upon a time, there was numad. These days, there is no need of having it
running as a daemon. However, the service of "pre-placement" of a VM (i.e.,
deciding on which NUMA node[s] place the VM, while it's being created) is
still valuable. And that's what this package aims at offering.

%prep
%autosetup -p1

%build
%make_build

%install
%make_build install prefix=%{buildroot}/usr

%files
%defattr(-,root,root)
%{_sbindir}/numa-preplace
%{_mandir}/man8/numa-preplace.8.gz

%changelog
