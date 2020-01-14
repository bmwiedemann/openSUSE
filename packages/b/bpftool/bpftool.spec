#
# spec file for package bpftool
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bpftool
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        Tool for inspection and manipulation of BPF programs and maps
License:        GPL-2.0-only
Group:          Development/Tools/Other
Url:            http://www.kernel.org/
BuildRequires:  docutils
BuildRequires:  kernel-source
BuildRequires:  libelf-devel

%description
bpftool allows for inspection and simple modification of BPF objects (programs
and maps) on the system.

%prep
(cd /usr/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} kernel/bpf lib) | tar -xf -
cp /usr/src/linux/LICENSES/preferred/GPL-2.0 .
sed -i -e 's/CFLAGS += -O2/CFLAGS = $(RPM_OPT_FLAGS)/' Makefile

%build
cd tools/bpf/bpftool
%make_build V=1 feature-reallocarray=1 all doc

%install
cd tools/bpf/bpftool
make install doc-install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}

%files
%license GPL-2.0
%{_sbindir}/bpftool
%{_datadir}/bash-completion/completions/bpftool
%{_mandir}/man?/*.gz

%changelog
