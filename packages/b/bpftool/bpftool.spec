#
# spec file for package bpftool
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


%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Name:           bpftool
Version:        %{version}
Release:        0
Patch0:         binutils-2.40.patch
Summary:        Tool for inspection and manipulation of BPF programs and maps
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://www.kernel.org/
BuildRequires:  binutils-devel
BuildRequires:  docutils
BuildRequires:  kernel-source
BuildRequires:  libelf-devel

%description
bpftool allows for inspection and simple modification of BPF objects (programs
and maps) on the system.

%package bash-completion
Summary:        Bash completion for bpftool
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
bash command line completion support for bpftool.

%package rebuild
Summary:        Empty package to ensure rebuilding bpftool in OBS
Group:          System/Monitoring
%requires_eq    kernel-source

%description rebuild
This is empty package that ensures bpftool is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%prep
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} kernel/bpf lib) | tar -xf -
cp %{_prefix}/src/linux/LICENSES/preferred/GPL-2.0 .
sed -i -e 's/CFLAGS += -O2/CFLAGS = $(RPM_OPT_FLAGS)/' Makefile
%patch0 -p1

%build
cd tools/bpf/bpftool
%make_build \
    feature-reallocarray=1 \
    feature-libbfd-liberty=1 \
%if %(if gcc -lsframe -shared 2>/dev/null ; then echo 1 ; else echo 0; fi; )
    feature-libbfd-liberty-sframe=1 \
%endif
    feature-disassembler-four-args=1 \
    all \
    doc

%install
cd tools/bpf/bpftool
make install doc-install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}

%files
%license GPL-2.0
%{_sbindir}/bpftool
%{_mandir}/man?/*.gz

%files bash-completion
%{_datadir}/bash-completion/completions/bpftool

%files rebuild
%license GPL-2.0

%changelog
