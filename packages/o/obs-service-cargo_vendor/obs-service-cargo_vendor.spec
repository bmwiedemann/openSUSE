#
# spec file for package obs-service-cargo_vendor
#
# Copyright (c) 2020 SUSE LLC
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


%define service cargo_vendor
Name:           obs-service-%{service}
Summary:        An OBS source service: Download, verify and vendor Rust crates (libraries)
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Version:        0.4.0~git0.d4f314f
Release:        0
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3
Requires:       gzip
Requires:       tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
An OBS Source Service that will download,
verify and vendor Rust crates (libraries)

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{service} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{service}.service %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
