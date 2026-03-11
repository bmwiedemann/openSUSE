#
# spec file for package krunvm
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


Name:           krunvm
Version:        0.2.6+git59f3673
Release:        0
Summary:        Manage lightweight VMs created from OCI images
License:        Apache-2.0
URL:            https://github.com/containers/krunvm
Source0:        krunvm-%{version}.tar.gz
Source1:        vendor.tar.zst
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo-packaging
BuildRequires:  libkrun-devel
BuildRequires:  zstd
BuildRequires:  rubygem(asciidoctor)
Requires:       buildah
Requires:       libkrun1 >= 1.4.4
Conflicts:      libkrun0

%description
Manage lightweight VMs created from OCI images

%files
%license LICENSE
%doc README.md
%doc CODE-OF-CONDUCT.md
%doc SECURITY.md
%{_mandir}/man1/krunvm*.1*
%{_bindir}/krunvm

%prep
%autosetup -p1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

# We need to deal with the manpages manually
install -d -m 0755 %{buildroot}%{_mandir}/man1
find target/release/build/krunvm-*/out -name "*.1" -exec install -m 0644 {} %{buildroot}%{_mandir}/man1/ \;

%changelog
