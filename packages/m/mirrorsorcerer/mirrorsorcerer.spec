#
# spec file for package mirrorsorcerer
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


Name:           mirrorsorcerer
Version:        0.1.1~3
Release:        0
Summary:        Mirror Sorcerer tool to magically make OpenSUSE mirror sources more magic-er
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND BSD-3-Clause AND MIT AND MPL-2.0
Group:          System/Management
URL:            https://github.com/Firstyear/mirrorsorcerer
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  zstd
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
This tool will profile official instances of OpenSUSE mirrorcache to determine the
fastest repositories for your system 🧙

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
# find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build}

%install
# manual process
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}/%{_datadir}/mirrorsorcerer

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/mirrorsorcerer %{buildroot}%{_sbindir}/mirrorsorcerer
install -m 0644 %{_builddir}/%{name}-%{version}/pool.json %{buildroot}%{_datadir}/mirrorsorcerer/pool.json
install -m 0644 %{_builddir}/%{name}-%{version}/mirrorsorcerer.service %{buildroot}%{_unitdir}/mirrorsorcerer.service

%pre
%service_add_pre mirrorsorcerer.service

%post
%service_add_post mirrorsorcerer.service

%preun
%service_del_preun mirrorsorcerer.service

%postun
%service_del_postun mirrorsorcerer.service

%files
%defattr(-,root,root)
%{_sbindir}/mirrorsorcerer
%dir %{_datadir}/mirrorsorcerer
%{_datadir}/mirrorsorcerer/pool.json
%{_unitdir}/mirrorsorcerer.service

%changelog
