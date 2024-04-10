#
# spec file for package sysctl-logger
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

# Use default LLVM on openSUSE
%if 0%{?suse_version} >= 1600 || 0%{?is_opensuse}
 %define llvm_major_version %{nil}
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

Name:           sysctl-logger
Version:        0.0.6
Release:        0
Summary:        A sysctl monitoring tool based on BPF
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/shunghsiyu/sysctl-logger
Source:         https://github.com/shunghsiyu/sysctl-logger/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bpftool
BuildRequires:  clang%{llvm_major_version} > 9
BuildRequires:  gettext-runtime
BuildRequires:  make
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  systemd-rpm-macros


%description
sysctl-logger is a sysctl monitoring tool that tracks changes to sysctl value.

%prep
%setup -q
%autosetup -p1

%build
%set_build_flags
export LIBDIR='%{_libdir}'
export UNITDIR='%{_unitdir}'
export CLANG=%{_bindir}/clang
export FORCE_SYSTEM_LIBBPF=1
export PATH="$PATH:/usr/sbin" # So bpftool can be found
%make_build

%install
export SBINDIR='%{_sbindir}'
%make_install

%pre
%service_add_pre sysctl-logger.service

%post
%service_add_post sysctl-logger.service

%preun
%service_del_preun sysctl-logger.service

%postun
%service_del_postun sysctl-logger.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/sysctl-logger
%{_unitdir}/sysctl-logger.service

%changelog

