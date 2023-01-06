#
# spec file for package kernel-install-tools
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


Name:           kernel-install-tools
Version:        0.3.0
Release:        0
Summary:        Useful tools for installing self-built kernels
Group:          Development/Tools/Other
License:        GPL-2.0-only
URL:            https://github.com/jeffmahoney/kernel-install-tools
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Requires:       openssl
%ifarch ia64 %ix86 x86_64 aarch64 %arm riscv64
Requires:       mozilla-nss-tools
Requires:       pesign
%else
Requires:       kernel-default-devel
%endif

%description
A collection of tools useful for installing self-built kernels.

In addition to the baseline /sbin/installkernel, this package includes
several tools for properly signing and installing kernels and certificates
for use on systems with UEFI Secure Boot enabled.

%prep
%setup -q

%build

%install
%make_install

%if 0%{?suse_version} >= 1550
mv %{buildroot}/sbin/installkernel %{buildroot}/usr/sbin/installkernel
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/sbtool-genkey
%{_bindir}/sbtool-sign-kernel
%{_sbindir}/sbtool-enroll-key
%if 0%{?suse_version} >= 1550
%{_sbindir}/installkernel
%else
/sbin/installkernel
%endif

%changelog
