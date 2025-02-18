#
# spec file for package k9s
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


Name:           k9s
Version:        0.40.4
Release:        0
Summary:        Curses based terminal UI for Kubernetes clusters
License:        Apache-2.0
URL:            https://github.com/derailed/k9s
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.23
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
K9s provides a curses based terminal UI to interact with your Kubernetes
clusters. The aim of this project is to make it easier to navigate, observe
and manage your applications in the wild. K9s continually watches Kubernetes
for changes and offers subsequent commands to interact with observed
Kubernetes resources.

%prep
%setup -qa1

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

%ifarch i586 s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl riscv64
export CGO_ENABLED=1
%else
export CGO_ENABLED=0
%endif
make GO_FLAGS="-mod=vendor -buildmode=pie" GIT_REV="${COMMIT_HASH:0:8}" VERSION="%{version}" DATE="${BUILD_DATE}" build

%install
# Install the binary.
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 execs/k9s %{buildroot}%{_bindir}/k9s

%files
%license LICENSE
%doc README.md
%{_bindir}/k9s

%changelog
