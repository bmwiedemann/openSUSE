#
# spec file for package kvm_stat
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


Name:           kvm_stat
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        Monitoring Tool for KVM guests
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://www.kernel.org/
BuildArch:      noarch
BuildRequires:  asciidoc
BuildRequires:  kernel-source >= 5.2.0
BuildRequires:  libxslt-tools

Requires:       python3-curses

Recommends:     kernel >= 5.2.0
Conflicts:      qemu < 2.6.90
Conflicts:      qemu-kvm < 2.6.90
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Patch00:        tools-kvm_stat-explicitly-reference-python3.patch

%define XXX This package provides a userspace tool "kvm_stat", which displays KVM vm exit \
information as a means of monitoring vm behavior. The data is taken from the\
KVM debugfs files or the vm tracepoints and outputs them as a curses ui or\
simple text.

%description
%{XXX}

%prep
# copy necessary files from kernel-source
(tar -C /usr/src/linux -c COPYING tools scripts) | tar -x

%patch00 -p1

%build
make -C tools/kvm/kvm_stat %{?_smp_mflags}

%install
make -C tools kvm_stat_install INSTALL_ROOT=%{buildroot}

%files
%defattr(-, root, root)
%license COPYING
%{_bindir}/kvm_stat
%{_mandir}/man1/kvm_stat*

%changelog
