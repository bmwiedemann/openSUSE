#
# spec file for package roast
#
# Copyright (c) 2025 SUSE LLC
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
Version:        6.1.1
Release:        0
Summary:        Simpler tar archiver and extractor
License:        MPL-2.0
URL:            https://github.com/openSUSE-Rust/roast
Source0:        %{name}-v%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)

%package -n obs-service-recomprizz
Version:        %{version}
Summary:        OBS Source Service for recomprizz-ion
License:        MPL-2.0

%description -n obs-service-recomprizz
Utility to recompress to other compression formats.

%package -n obs-service-roast
Version:        %{version}
Summary:        OBS Source Service for roast
License:        MPL-2.0

%description -n obs-service-roast
Utility to roast source directories into highly compressed tape archives.

%package -n obs-service-raw
Version:        %{version}
Summary:        OBS Source Service for raw
License:        MPL-2.0

%description -n obs-service-raw
Utility to raw decompress tape archives to unarchived sources.

%package -n obs-service-roast_scm
Version:        %{version}
Summary:        OBS Source Service for roast_scm
License:        MPL-2.0

%description -n obs-service-roast_scm
Utility to roast remote git repositories as tarball sources.

%description
Roast is a simple tar archiver and extractor with very high
compression settings for supported formats such as zstd.

It also supports recompression from an existing tarball.

%prep
%autosetup -a1 -n %{name}-v%{version}

%build
%{cargo_build}

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
pushd roast-cli
%{cargo_install} --bins
popd
cp -v %{buildroot}%{_bindir}/roast %{buildroot}%{_prefix}/lib/obs/service/roast
install -m0644 roast.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{buildroot}%{_bindir}/recomprizz %{buildroot}%{_prefix}/lib/obs/service/recomprizz
install -m0644 recomprizz.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{buildroot}%{_bindir}/raw %{buildroot}%{_prefix}/lib/obs/service/raw
install -m0644 raw.service %{buildroot}%{_prefix}/lib/obs/service
cp -v %{buildroot}%{_bindir}/roast_scm %{buildroot}%{_prefix}/lib/obs/service/roast_scm
install -m0644 roast_scm.service %{buildroot}%{_prefix}/lib/obs/service

%check
%{cargo_test}

%files
%{_bindir}/roast
%{_bindir}/raw
%{_bindir}/recomprizz
%{_bindir}/roast_scm
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-roast
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/roast
%{_prefix}/lib/obs/service/roast.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-recomprizz
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/recomprizz
%{_prefix}/lib/obs/service/recomprizz.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-raw
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/raw
%{_prefix}/lib/obs/service/raw.service
%license LICENCE
%doc     CHANGELOG.md README.md

%files -n obs-service-roast_scm
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/roast_scm
%{_prefix}/lib/obs/service/roast_scm.service
%license LICENCE
%doc     CHANGELOG.md README.md

%changelog
