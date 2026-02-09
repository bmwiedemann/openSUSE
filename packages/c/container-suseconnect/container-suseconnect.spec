#
# spec file for package container-suseconnect
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global project     container-suseconnect
%global import_path github.com/SUSE/%{project}
%global zypp_path   %{_prefix}/lib/zypp/plugins
%global zypp_services %{zypp_path}/services
%global zypp_urlresolver %{zypp_path}/urlresolver
%global use_fips_mode 0%{?suse_version} == 1500 || 0%{?suse_version} == 1600

Name:           %{project}
Version:        2.5.6
Release:        0
Summary:        Provides access to repositories inside containers
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://%{import_path}
Source0:        %{project}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        container-suseconnect-rpmlintrc
BuildRequires:  libzypp > 9.34
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.25
Requires:       libzypp > 9.34

%description
container-suseconnect gives access to package repositories inside containers
using the host machine entitlements.

%prep
%if 0%{?suse_version} && 0%{?suse_version} < 1500
export TAR_OPTIONS="-I zstd"
%endif
%setup -q -n %{project}-%{version} -a1

%build
%if %use_fips_mode
export GOFIPS140=v1.0.0
%endif
go build -o %{project} -mod=vendor -buildmode=pie -trimpath \
    -ldflags="-s -w -X %{import_path}/internal.version=%{version}" \
    ./cmd/container-suseconnect

%check
test "$(./%{project} -version)" = "%version"
%if %use_fips_mode
export GODEBUG=fips140=only GOFIPS140=v1.0.0
%endif
go test ./...

%install
install -D -m 755 %{project} %{buildroot}/%{_bindir}/%{project}
mkdir -p %{buildroot}/%{zypp_services}
mkdir -p %{buildroot}/%{zypp_urlresolver}
ln -s %{_bindir}/%{project} %{buildroot}/%{zypp_services}/%{project}-zypp
ln -s %{_bindir}/%{project} %{buildroot}/%{zypp_urlresolver}/susecloud

%files
%doc README.md
%license LICENSE
%{_bindir}/%{project}
%{zypp_services}/%{project}-zypp
%{zypp_urlresolver}/susecloud

%changelog
