#
# spec file for package slim
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


Name:           slim
Version:        1.40.11
Release:        0
Summary:        Minify your container images without changes
License:        Apache-2.0
URL:            https://github.com/slimtoolkit/slim
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  golang(API) >= 1.23
BuildRequires:  zsh

# can be used with podman by setting
# DOCKER_SOCK and DOCKER_HOST
Requires:       (docker or podman)

# old name
Provides:       docker-slim = %{version}

#
# [  233s] pkg/app/sensor/monitor/fanotify/monitor.go:123:14: nd.Mark undefined
# (type *"github.com/slimtoolkit/slim/pkg/third_party/madmo/fanotify".NotifyFD
# has no field or method Mark)
#
ExclusiveArch:  x86_64 aarch64

%description
Slim helps you build optimized containers, while Root.io automatically fixes
vulnerabilities without disrupting your workflows. Use Slim's open source
toolkit to optimize containers, then keep them secure with Root's automated
vulnerability remediation – from optimization to continuous security in one
seamless journey.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go generate github.com/slimtoolkit/slim/pkg/appbom

go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -tags="netgo,osusergo" \
   -ldflags=" \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionTag=%{version} \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionRev=${COMMIT_HASH} \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionTime=${BUILD_DATE}" \
   -o bin/%{name} ./cmd/slim/

go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -tags="netgo,osusergo" \
   -ldflags=" \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionTag=%{version} \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionRev=${COMMIT_HASH} \
   -X github.com/slimtoolkit/slim/pkg/version.appVersionTime=${BUILD_DATE}" \
   -o bin/%{name}-sensor ./cmd/slim-sensor/

%install
# Install the binaries
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0755 bin/%{name}-sensor %{buildroot}/%{_bindir}/%{name}-sensor

%check
%{buildroot}/%{_bindir}/%{name} --version
# the slim-sensor executable does not have a --version flag

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-sensor

%changelog
