#
# spec file for package nebula
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


Name:           nebula
Version:        1.9.3
Release:        0
Summary:        A scalable overlay networking tool
License:        MIT
URL:            https://github.com/slackhq/nebula
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.service
Patch0:         enable-pie.patch
BuildRequires:  git-core
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.22

%description
Nebula is a scalable overlay networking tool with a focus on performance,
simplicity and security. It lets you seamlessly connect computers anywhere
in the world. It can be used to connect a small number of computers,
but is also able to connect tens of thousands of computers.

%package cert
Summary:        Seperate %{name}-cert package

%description cert
This package only includes the %{name}-cert binary.

%prep
%autosetup -p1 -a1

%build
%make_build

%install
install -Dm0755 -t %{buildroot}%{_sbindir} nebula
install -Dm0755 -t %{buildroot}%{_bindir} nebula-cert
install -Dm0644 -t %{buildroot}%{_unitdir} %{SOURCE2}
install -d %{buildroot}%{_sysconfdir}/%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check
%make_build test

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md LOGGING.md README.md SECURITY.md examples/config.yml
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/%{name}

%files cert
%license LICENSE
%{_bindir}/%{name}-cert

%changelog
