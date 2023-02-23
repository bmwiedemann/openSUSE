#
# spec file for package cargo-audit-advisory-db
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


Name:           cargo-audit-advisory-db
Version:        20230223
Release:        0
Summary:        A database of known security issues for Rust depedencies
License:        CC0-1.0
URL:            https://github.com/RustSec/advisory-db
Source0:        advisory-db-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Requires:       cargo-audit
ExclusiveArch:  %{rust_tier1_arches}

%description
The RustSec Advisory Database is a repository of security advisories filed against Rust crates
published via https://crates.io. A human-readable version of the advisory database can be
found at https://rustsec.org/advisories/.

%prep
%setup -q -n advisory-db-%{version}

%build
# No op
true

%install
mkdir -p %{buildroot}%{_datadir}
cp -R %{_builddir}/advisory-db-%{version} %{buildroot}%{_datadir}/%{name}

%files
%{_datadir}/%{name}

%changelog
