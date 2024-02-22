#
# spec file for package pesign-obs-integration
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
# needssslcertforbuild


Name:           pesign-obs-integration
Version:        10.2+git20240216.1e15ef4
Release:        0
Summary:        Macros and scripts to sign the kernel and bootloader
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://en.opensuse.org/openSUSE:UEFI_Image_File_Sign_Tools
Source:         %{name}-%{version}.tar.gz
BuildRequires:  openssl
Requires:       fipscheck
Requires:       mozilla-nss-tools
Requires:       openssl
# suse-module-tools <= 15.0.10 contains modsign-verify
Requires:       suse-module-tools >= 15.0.10
%ifarch %{ix86} x86_64 ia64 aarch64 %{arm} riscv64
Requires:       pesign
%endif

%description
This package provides scripts and rpm macros to automate signing of the
boot loader, kernel and kernel modules in the openSUSE Buildservice.

%prep
%setup -q -D
%autopatch -p1

%build

%install

mkdir -p %{buildroot}%{_prefix}/lib/rpm/brp-suse.d %{buildroot}%{_prefix}/lib/rpm/pesign
install pesign-gen-repackage-spec kernel-sign-file gen-hmac %{buildroot}%{_prefix}/lib/rpm/pesign
install brp-99-pesign %{buildroot}%{_prefix}/lib/rpm/brp-suse.d
# brp-99-compress-vmlinux has nothing to do with signing. It is packaged in
# pesign-obs-integration because this package is already used by the kernel
# build
install brp-99-compress-vmlinux %{buildroot}%{_prefix}/lib/rpm/brp-suse.d
install -m644 pesign-repackage.spec.in %{buildroot}%{_prefix}/lib/rpm/pesign
mkdir -p %{buildroot}%{_bindir}
install modsign-repackage %{buildroot}%{_bindir}/
install -pm 755 modsign-verify %{buildroot}%{_bindir}/
if test -e _projectcert.crt; then
	openssl x509 -inform PEM -in _projectcert.crt \
		-outform DER -out %{buildroot}%{_prefix}/lib/rpm/pesign/pesign-cert.x509
else
	echo "No buildservice project certificate available"
fi

%files
%license COPYING
%doc README.md
%{_bindir}/modsign-repackage
%{_bindir}/modsign-verify
%{_prefix}/lib/rpm/*

%changelog
