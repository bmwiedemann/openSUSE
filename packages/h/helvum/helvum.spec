#
# spec file for package helvum
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

%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           helvum
Version:        0.3.0~git0.2ee7bca
Release:        0
Summary:        A GTK patchbay for pipewire
License:        GPL-3.0-only AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( Unlicense OR MIT ) AND Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            https://gitlab.freedesktop.org/ryuukyu/helvum
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  gtk4-devel
BuildRequires:  pipewire-devel
ExcludeArch:    s390 s390x ppc ppc64 ppc64le %{ix86}

%description
Helvum is a GTK-based patchbay for pipewire, inspired by the JACK tool catia.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release

%install
RUSTFLAGS=%{rustflags} cargo install --no-track --root=%{buildroot}%{_prefix} --path .
#install -D -d -m 0755 %{buildroot}%{_bindir}
#install -m 0755 %{_builddir}/%{name}-%{version}/target/release/helvum %{buildroot}%{_bindir}/helvum

%files
%{_bindir}/helvum

%changelog
