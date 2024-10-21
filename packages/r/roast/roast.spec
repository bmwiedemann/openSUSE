#
# spec file for package roast
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

Name:           roast
Version:        4.5.0
Release:        0
Summary:        Simpler tar archiver and extractor
License:        MPL-2.0
URL:            https://github.com/openSUSE-Rust/roast
Source0:        https://github.com/openSUSE-Rust/roast/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)

%package -n obs-service-recomprizz
Version:        %{version}
Summary:        OBS Source Service for recomprizz-ion
License:        MPL-2.0

%description -n obs-service-recomprizz
Utility to recompress to other compression formats.

%description
Roast is a simple tar archiver and extractor with very high
compression settings for supported formats such as zstd.

It also supports recompression from an existing tarball.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
pushd roast-cli
%{cargo_install} --bins
popd
cp -v %{buildroot}%{_bindir}/recomprizz %{buildroot}%{_prefix}/lib/obs/service/recomprizz
install -m0644 recomprizz.service %{buildroot}%{_prefix}/lib/obs/service

%check
%{cargo_test}

%files
%{_bindir}/roast
%{_bindir}/raw
%{_bindir}/recomprizz
%license LICENCE
%doc     CHANGELOG README.md

%files -n obs-service-recomprizz
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/recomprizz
%{_prefix}/lib/obs/service/recomprizz.service
%license LICENCE
%doc     CHANGELOG README.md

%changelog
