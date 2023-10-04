#
# spec file for <package name>
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


Name:           amber-cli
Version:        0.3.0+git20230728.955f78d
Release:        0
Summary:        CLI tool for tenants to use and access Amber services
License:        BSD-3-Clause
URL:            https://github.com/intel/amber-cli
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.zstd
BuildRequires:  golang(API) >= 1.20
BuildRequires:  zstd

%description
CLI tool for tenants to use and access Amber services.
Amber remotely verifies trustworthiness of Intel SGX and Intel TDX TEEs.

All files are stored in user's home directory. Following are the details:
* Configuration: $HOME/.config/tenantctl/config.yaml
* Logs: $HOME/.config/tenantctl/logs/tac.log
* Bin: $HOME/.local/bin/tenantctl

%prep
%autosetup -p1 -a1

%build
# From the Makefile
GITCOMMIT="HEAD"
BUILDDATE="$(TZ=UTC date +%Y-%m-%dT%H:%M:%%S%z)"
VERSION="%{version}"
GOOS=linux CGO_CPPFLAGS="-D_FORTIFY_SOURCE=2" go build \
	   -mod=vendor \
	   -buildmode=pie \
	   -ldflags "-X intel/amber/tac/v1/utils.BuildDate=${BUILDDATE} -X intel/amber/tac/v1/utils.Version=${VERSION} -X intel/amber/tac/v1/utils.GitHash=${GITCOMMIT} -linkmode=external -s -extldflags '-Wl,-z,relro,-z,now'"\
	   -o tenantctl

%install
install -D -m0755 tenantctl %{buildroot}%{_bindir}/tenantctl

%files
%license LICENSE
%doc README.md
%{_bindir}/tenantctl

%changelog
