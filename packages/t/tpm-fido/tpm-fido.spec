#
# spec file for package tpm-fido
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

# Prepare sources and vendor bundle with: osc service mr

Name:           tpm-fido
Version:        20230621.5f8828b
Release:        0
Summary:        Use your TPM2 as a FIDO 2FA token
License:        MIT
URL:            https://github.com/psanford/tpm-fido
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
Source2:        tpm-fido.rules
Source3:        tpm-fido.service
BuildRequires:  golang(API) >= 1.16
BuildRequires:  zstd
Requires:       pinentry-gui
Provides:       tpm2-fido

%description
tpm-fido is FIDO token implementation for Linux that protects the token keys by using your system's TPM. tpm-fido uses Linux's uhid facility to emulate a USB HID device so that it is properly detected by browsers.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 $RPM_SOURCE_DIR/tpm-fido.rules %{buildroot}%{_prefix}/lib/udev/rules.d/91-tpm-fido.rules
install -D -m0644 $RPM_SOURCE_DIR/tpm-fido.service %{buildroot}%{_prefix}/lib/systemd/user/tpm-fido.service

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}
%{_prefix}/lib/udev/rules.d/91-tpm-fido.rules
%{_prefix}/lib/systemd/user/tpm-fido.service

%post
printf "To use tpm-fido, add your user to the tss group and run:\n"
printf "systemctl --user enable --now tpm-fido.service\n"

%changelog
