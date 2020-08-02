#
# spec file for package obs-service-rust2rpm
#
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


%global service rust2rpm

Name:           obs-service-%{service}
Version:        1
Release:        0
Summary:        An OBS source service: Generate rpm packaging for Rust crates
Group:          Development/Languages/Rust
License:        MIT
URL:            https://pagure.io/fedora-rust/%{name}
Source0:        https://releases.pagure.org/fedora-rust/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  rust-srpm-macros >= 9
Requires:       rust2rpm >= 9
Requires:       python3
Supplements:    ((obs-source_service or osc) and rust2rpm)

BuildArch:      noarch
ExclusiveArch:  %{rust_arches} noarch

%description
This is a source service for openSUSE Build Service.

This simply runs rust2rpm for a given Rust crate on crates.io
to generate RPM packaging to build packages for crates.

%prep
%autosetup


%build
# Nothing to build

%install
%make_install


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/rust2rpm*
%dir %{_localstatedir}/cache/obs
%dir %{_localstatedir}/cache/obs/rust2rpm

%changelog
