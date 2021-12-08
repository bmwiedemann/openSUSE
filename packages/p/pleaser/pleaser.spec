#
# spec file for package pleaser
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without check

%global crate pleaser

Name:           pleaser
Version:        0.5.1~git0.ce9627c
Release:        0%{?dist}
Group:          Productivity/Security
Summary:        Alternative to sudo (root command execution) with regex support
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND Apache-2.0 AND MIT AND GPL-3.0-or-later
URL:            https://gitlab.com/edneville/please/-/archive/v%{version}/please-v%{version}.tar.gz
Source0:        please-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch0:         please-0.5.1_fix_syslog.patch
ExclusiveArch:  %{rust_arches}

%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  cargo
BuildRequires:  pam-devel
BuildRequires:  rust
BuildRequires:  rust-packaging

Requires:       pam

Requires(post): permissions
Requires(verify):permissions

%description
please is a regex-capable alternative to sudo, a command for allowing
users to execute some subsequent commands as the root (or another) user.
pleaseedit is a method to permit editing of files without
elevation.

%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

%prep
%setup -qa1 -n please-%{version}
%patch0 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release

%post
%set_permissions /usr/bin/please
%set_permissions /usr/bin/pleaseedit

%verifyscript
%verify_permissions -e /usr/bin/please -e /usr/bin/pleaseedit

%install
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .

# remove crate file
rm %{buildroot}%{_prefix}/.crates.toml
rm -f %{buildroot}%{_prefix}/.crates2.json

install -Dpm4755 -t %{buildroot}%{_bindir} target/release/please
install -Dpm4755 -t %{buildroot}%{_bindir} target/release/pleaseedit
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/please.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man5 man/please.ini.5
install -Dpm0600 -t %{buildroot}%{_sysconfdir}/ examples/please.ini

mkdir -m 700 -p %{buildroot}%{_sysconfdir}/please.d

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/please << EOF
auth       include      common-auth
account    include      common-account
password   include      common-password
session    optional     pam_keyinit.so revoke
session    include      common-session
EOF

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/pleaseedit << EOF
auth       include      common-auth
account    include      common-account
password   include      common-password
session    optional     pam_keyinit.so revoke
session    include      common-session
EOF

%files
%doc README.md
%license LICENSE
%verify(not mode) %attr(4755,root,root) %{_bindir}/please
%verify(not mode) %attr(4755,root,root) %{_bindir}/pleaseedit
%{_mandir}/man1/please.1*
%{_mandir}/man5/please.ini.5*
%config(noreplace) %{_sysconfdir}/pam.d/please
%config(noreplace) %{_sysconfdir}/pam.d/pleaseedit
%config(noreplace) %{_sysconfdir}/please.ini
%config(noreplace) %{_sysconfdir}/please.d

%changelog
