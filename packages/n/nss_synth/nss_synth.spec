#
# spec file for package nss_synth
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


Name:           nss_synth
Version:        0.1.0~git2.ed6985d
Release:        0
Summary:        A module that synthesises uid/gid's from bare uid's for container compatibility
License:        MPL-2.0
URL:            https://github.com/kanidm/nss_synth
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
# For SUSE BCI containers we need to support other arches.
# ExclusiveArch:  pct brkt rust_tier1_arches brkt

%description
NSS Synth is a module that synthesises uids/gids into real groups. This means that when you have a
container with bare uids/gids, these are able to resolve to a concrete user name and group name so
that calls like getpwnam() function correctly.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_libdir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/libnss_synth.so %{buildroot}%{_libdir}/libnss_synth.so.2

%files
%{_libdir}/libnss_synth.so.2

%changelog
