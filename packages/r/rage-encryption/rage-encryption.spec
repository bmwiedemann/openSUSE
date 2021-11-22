#
# spec file for package rage
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

Name:           rage-encryption
#               This will be set by osc services, that will run after this.
Version:        0.7.0~git0.c93b914
Release:        0
Summary:        Simple, modern, and secure file encryption tool
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-3-Clause AND CDDL-1.0 AND MIT
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Productivity/Security
Url:            https://github.com/str4d/rage
Source0:        rage-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
Conflicts:      rage
ExclusiveArch:  %{rust_tier1_arches}

%description
Rage is a simple, modern, and secure file encryption tool, using the age format. It features small
explicit keys, no config options, and UNIX-style composability.

%prep
%setup -q -a 0 -n rage-%{version}
%setup -q -n rage-%{version} -a 1 -D -T
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/rage-%{version}/target/release/rage %{buildroot}%{_bindir}/rage
install -m 0755 %{_builddir}/rage-%{version}/target/release/rage-keygen %{buildroot}%{_bindir}/rage-keygen

%files
%{_bindir}/rage
%{_bindir}/rage-keygen

%changelog

