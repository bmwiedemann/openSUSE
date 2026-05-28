#
# spec file for package CoreFreq
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           CoreFreq
Version:        2.1.1
Release:        0
Summary:        CPU monitoring software for 64-bit processors
License:        GPL-2.0-or-later
URL:            https://github.com/cyring/CoreFreq
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      corefreqd.service
Source101:      preamble
# PATCH-FIX-UPSTREAM -- Commit 69b4a29
Patch:          fix-leap16-compilation.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires:       CoreFreq-kmp = %{version}
ExclusiveArch:  x86_64 aarch64 ppc64le
%systemd_ordering
%kernel_module_package -p preamble -x preempt 64kb

%description
CPU monitoring software with BIOS like functionalities designed for
64-bit processors of architecture Intel Atom, Core2, Nehalem, SandyBridge and superiors;
AMD Families from 0Fh ... up to 17h (Zen , Zen+ , Zen 2), 18h (Hygon Dhyana),
19h (Zen 3, Zen 3+, Zen 4, Zen 4c), 1Ah (Zen 5, Zen 5c);
Arm A64; RISC-V RV64; PowerPC64 (LE)

%prep
%autosetup -p1

%build
%make_build

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates

mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_unitdir} %{buildroot}%{_sbindir}

PREFIX=%{buildroot}%{_prefix} make install

cp %{SOURCE100} %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rccorefreqd

%files
%license LICENSE
%doc README.md
%{_bindir}/corefreq-cli
%{_bindir}/corefreqd
%{_unitdir}/corefreqd.service
%{_sbindir}/rccorefreqd

%pre
%service_add_pre corefreqd.service

%post
%service_add_post corefreqd.service

%preun
%service_del_preun corefreqd.service

%postun
%service_del_postun corefreqd.service

%check

%changelog
