#
# spec file for package butane
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Neal Gompa.
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


Name:           butane
Version:        0.17.0
Release:        0
Summary:        Tool to generate Ignition configs from Butane Configs
Group:          System/Management
License:        Apache-2.0
URL:            https://github.com/coreos/butane
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  golang(API) >= 1.15

# Upgrade from old fcct/ignition-config-transpiler
Obsoletes:      ignition-config-transpiler < %{version}-%{release}
Provides:       ignition-config-transpiler = %{version}-%{release}
Provides:       ignition-config-transpiler%{?_isa} = %{version}-%{release}

%description
Butane translates human-readable Butane Configs into machine-readable
Ignition configs for provisioning operating systems that use Ignition.

%prep
%autosetup -p1

%build
go build -mod=vendor -buildmode=pie -ldflags "-X github.com/coreos/butane/internal/version.Raw=%{version}" -a -v -x -o ./butane internal/main.go

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./butane %{buildroot}%{_bindir}
ln -s butane %{buildroot}%{_bindir}/ignition-config-transpiler
ln -s butane %{buildroot}%{_bindir}/fcct

%files
%license LICENSE
%doc docs README.md NEWS.md
%{_bindir}/butane
%{_bindir}/ignition-config-transpiler
%{_bindir}/fcct

%changelog
