#
# spec file for package opencloud-server
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


%define executable_name opencloud-server
%define web_assets_version v5.1.0

Name:           opencloud-server
Version:        5.1.0
Release:        0
Summary:        Secure and private way to store, access, and share your files
License:        Apache-2.0
URL:            https://github.com/opencloud-eu/opencloud
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        https://github.com/opencloud-eu/web/releases/download/%{web_assets_version}/web.tar.gz#/web-%{web_assets_version}.tar.gz
Source3:        https://github.com/opencloud-eu/web/releases/download/%{web_assets_version}/third-party-licenses.tar.gz#/third-party-licenses-%{web_assets_version}.tar.gz
Source4:        idp-%{version}.tar.gz
Source11:       %{name}.service
Source12:       environment-file
Source21:       system-user-%{name}.conf
Source31:       Makefile
Source32:       PACKAGING_README.md
BuildRequires:  go1.24 >= 1.24.6
BuildRequires:  make
BuildRequires:  pnpm
BuildRequires:  ncurses-utils
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  sysuser-tools
#
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(vips) >= 8.16.0
%endif
#
Provides:       %{executable_name} = %{version}

%description
OpenCloud is an open-source project that gives you a secure and private way to
store, access, and share your files.

Excellent file management and collaboration for public authorities, providers
and business - or anyone who values ease of use and digital sovereignty.

This package contains the server component.

%prep
%autosetup -p 1 -a 1
tar xf %{SOURCE2} -C services/web/assets/core/
mkdir -p third-party-licenses/node/web
tar xf %{SOURCE3} -C third-party-licenses/node/web
tar xf %{SOURCE4} -C services/idp/

%build
###########################################################################
# services/idp/ directory
#
cd services/idp/ || exit 1

mkdir -p assets/identifier/static/
cp src/images/favicon.svg assets/identifier/static/favicon.svg
rm -f assets/identifier/static/favicon.ico
cp src/images/icon-lilac.svg assets/identifier/static/icon-lilac.svg

# change pnpm version to match ours
PNPM_VERSION="$(rpm -q pnpm | awk -F '-' '{print $2}')"
sed -i "/packageManager/ s/\"pnpm@.*\"/\"pnpm@${PNPM_VERSION}\"/g" package.json
grep packageManager package.json

# Creating an optimized production build...
pnpm build

cd ../../ || exit 1

###########################################################################
# opencloud/ directory
#
cd opencloud || exit 1

# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
%if 0%{?suse_version} > 1600
   -tags="disable_crypt,enable_vips" \
%else
   -tags="disable_crypt" \
%endif
   -ldflags=" \
   -X google.golang.org/protobuf/reflect/protoregistry.conflictPolicy=warn \
   -X github.com/opencloud-eu/opencloud/pkg/version.Edition=rolling \
   -X github.com/opencloud-eu/opencloud/pkg/version.String=${COMMIT_HASH:0:8} \
   -X github.com/opencloud-eu/opencloud/pkg/version.Tag=v%{version} \
   -X github.com/opencloud-eu/opencloud/pkg/version.Date=${BUILD_DATE}" \
   -o ../bin/%{executable_name} ./cmd/opencloud

###########################################################################
# base directory
#
cd ../ || exit 1

# system-user
%sysusers_generate_pre %{SOURCE21} user

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

# systemd unit
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_unitdir}/%{name}.service

# configuration directory
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}

# environment file
install -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/default/%{name}

# working directory
install -d -m 0770 %{buildroot}/%{_sharedstatedir}/%{name}
install -d -m 0770 %{buildroot}/%{_sharedstatedir}/%{name}/data/

# system user
install -Dm644 %{SOURCE21} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

%check
# run the binary to check if it works
%{buildroot}/%{_bindir}/%{executable_name} --help

%pre -f user.pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}
%{_unitdir}/%{name}.service
%dir %attr(770,root,opencloud-server) %config %{_sysconfdir}/%{name}
%dir %attr(770,opencloud-server,opencloud-server) %{_sharedstatedir}/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%{_sysusersdir}/system-user-%{name}.conf

%changelog
