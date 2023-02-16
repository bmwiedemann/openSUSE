#
# spec file for package fscrypt
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


Name:           fscrypt
Version:        0.3.4
Release:        0
Summary:        Go tool for managing Linux filesystem encryption
License:        Apache-2.0
Group:          System/Base
URL:            https://github.com/google/fscrypt
Source:         https://github.com/google/fscrypt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        %name.pam
BuildRequires:  golang-packaging
BuildRequires:  m4
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  golang(API) >= 1.16
BuildRequires:  pkgconfig(bash-completion)
Requires:       pam-fscrypt = %{version}

%description
fscrypt is a high-level tool for the management of Linux filesystem encryption.
This tool manages metadata, key generation, key wrapping, PAM integration, and
provides a uniform interface for creating and modifying encrypted directories.

%package -n pam-fscrypt
#
Summary:        Go tool for managing Linux filesystem encryption (the pam module)
Group:          System/Base
Requires(pre):  fscrypt = %{version}

%description -n pam-fscrypt
fscrypt is a high-level tool for the management of Linux filesystem encryption.
This tool manages metadata, key generation, key wrapping, PAM integration, and
provides a uniform interface for creating and modifying encrypted directories.

This package holds the pam module for fscrypt.

%prep
%autosetup -p1 -a 1

%build
%global make_args GO_FLAGS="-mod=vendor -buildmode=pie" PAM_MODULE_DIR="%{_pam_moduledir}" PREFIX="%{_prefix}"
%make_build %{make_args}

%install
%make_install %{make_args}
# not needed on SUSE
rm -rvf %{buildroot}%{_datadir}/pam-configs
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/fscrypt
%{_datadir}/bash-completion/completions/fscrypt

%files -n pam-fscrypt
%license LICENSE
%{_pam_moduledir}/pam_fscrypt.so
%{_sysconfdir}/pam.d/%{name}

%changelog
