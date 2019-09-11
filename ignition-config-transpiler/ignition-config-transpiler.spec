#
# spec file for package config-transpiler
#
# Copyright (c) 2018, 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:           ignition-config-transpiler
Version:        0.1.0+git20190723.2c075d6
Release:        0
Group:          System/Management
Summary:        Convert a yaml config file into a Ignition configuration
License:        Apache-2.0
URL:            https://github.com/coreos/fcct
Source:         fcct-%{version}.tar.xz
BuildRequires:  golang(API) >= 1.12

%description
The Ignition Config Transpiler ("fcct" for short) is the utility
responsible for transforming a human-friendly yaml config file
into a JSON file for ignition. This resulting file can be provided
to a machine with Ignition installed when it first boots to provision
the machine.

%prep
%setup -q -n fcct-%{version}

%build
go build -o fcct -mod vendor -buildmode=pie -ldflags "-X github.com/coreos/fcct/internal/version.Raw=%{version}" internal/main.go

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 fcct %{buildroot}%{_bindir}/ignition-config-transpiler
ln -sf ignition-config-transpiler %{buildroot}%{_bindir}/fcct

%files
%license LICENSE
%doc README.md NEWS docs
%{_bindir}/ignition-config-transpiler
%{_bindir}/fcct

%changelog
