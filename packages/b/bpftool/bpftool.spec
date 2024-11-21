#
# spec file for package bpftool
#
# Copyright (c) 2024 SUSE LLC
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


# Use default LLVM on openSUSE unless it is not yet supported
%if 0%{?suse_version} >= 1600 || 0%{?is_opensuse}
 %if 0%{?product_libs_llvm_ver} > 17
 %define llvm_major_version 17
 %else
 %define llvm_major_version %{nil}
 %endif
%else
 # Hard-code latest LLVM for SLES, the default version is too old
 %if 0%{?sle_version} == 150600
  %define llvm_major_version 17
 %else
 %if 0%{?sle_version} == 150500
  %define llvm_major_version 15
 %else
 %if 0%{?sle_version} == 150400
  %define llvm_major_version 11
 %endif
 %endif
 %endif
%endif

Name:           bpftool
Version:        7.5.0
Release:        0
Summary:        Tool for inspection and manipulation of BPF programs and maps
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://www.kernel.org/
Source0:        https://github.com/libbpf/bpftool/releases/download/v%{version}/bpftool-libbpf-v%{version}-sources.tar.gz
Patch0:         binutils-2.40.patch
BuildRequires:  binutils-devel
# Needed for compiling included BPF program (i.e. skeletons)
BuildRequires:  clang%{llvm_major_version}
BuildRequires:  docutils
BuildRequires:  libcap-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
# llvm-strip is needed for the included BPF program (i.e. skeletons)
BuildRequires:  llvm%{llvm_major_version}

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

%prep
%autosetup -p1 -n bpftool-libbpf-v%{version}-sources
sed -i -e 's/CFLAGS += -O2/CFLAGS = $(RPM_OPT_FLAGS)/' src/Makefile

%build
%make_build -C src V=1 \
    feature-reallocarray=1 \
    feature-libbfd-liberty=1 \
%if %(if gcc -lsframe -shared 2>/dev/null ; then echo 1 ; else echo 0; fi; )
    feature-libbfd-liberty-sframe=1 \
%endif
    feature-disassembler-four-args=1 \
    all
%make_build -C docs V=1 \
    man

%install
make -C src  V=1 install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}
make -C docs V=1 install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}

%files
%license LICENSE LICENSE.BSD-2-Clause LICENSE.GPL-2.0
%doc README.md CHECKPOINT-COMMIT BPF-CHECKPOINT-COMMIT
%{_sbindir}/bpftool
%{_mandir}/man?/*.gz

%files bash-completion
%{_datadir}/bash-completion/completions/bpftool

%changelog
