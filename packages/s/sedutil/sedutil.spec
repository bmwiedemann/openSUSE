#
# spec file for package sedutil
#
# Copyright (c) 2022 SUSE LLC
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


%define _dracutmodulesdir %{_prefix}/lib/dracut/modules.d
Name:           sedutil
Version:        1.20.0
Release:        0
Summary:        Tools to manage the activation and use of self encrypting drives
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/Drive-Trust-Alliance/sedutil/wiki
Source0:        https://github.com/Drive-Trust-Alliance/%{name}/archive/%{version}.tar.gz
Source1:        module-setup.sh
Source2:        linuxpba.sh
Source3:        sedutil-pba.pl
Patch0:         kernel_nvme_header.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
ExclusiveArch:  x86_64

%description
sedutil is a Self-Encrypting Drive (SED) management program and
Pre-Boot Authorization (PBA) image that will allow the activation and
use of self encrypting drives that comply with the Trusted Computing
Group Opal 2.0 SSC.

This package provides the sedutil-cli and linuxpba binaries, but not
the PBA image itself.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

install -m 0755 -d %{buildroot}%{_dracutmodulesdir}/00sedutil/
install -m 0755 %{SOURCE1} %{buildroot}%{_dracutmodulesdir}/00sedutil/
install -m 0755 %{SOURCE2} %{buildroot}%{_dracutmodulesdir}/00sedutil/
install -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}/

%files
%doc README.md Common/Copyright.txt Common/ReadMe.txt linux/PSIDRevert_LINUX.txt
%license Common/LICENSE.txt
%{_mandir}/man8/sedutil-cli.8%{?ext_man}
%{_sbindir}/sedutil-cli
%{_sbindir}/linuxpba
%dir %{_prefix}/lib/dracut
%dir %{_dracutmodulesdir}
%dir %{_dracutmodulesdir}/00sedutil/
%{_dracutmodulesdir}/00sedutil/module-setup.sh
%{_dracutmodulesdir}/00sedutil/linuxpba.sh
%{_sbindir}/sedutil-pba.pl

%changelog
