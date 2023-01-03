#
# spec file for package CoreFreq
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


Name:           CoreFreq
Version:        1.94.1
Release:        0
Summary:        CPU monitoring software for 64-bit processors
License:        GPL-2.0-or-later
URL:            https://github.com/cyring/CoreFreq
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      corefreqd.service
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires:       CoreFreq-kmp
ExclusiveArch:  x86_64
%systemd_ordering
%kernel_module_package -x preempt

%description
A CPU monitoring software with BIOS-like functionalities for
64-bit processors like Intel Atom, Core2, Nehalem, SandyBridge
and superiors, and AMD Families 0Fh–17h (Zen), 18h (Hygon
Dhyana).

%prep
%setup -q

%build
%make_build

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
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

%changelog
