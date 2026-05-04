#
# spec file for package stern
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


Name:           stern
Version:        1.34.0
Release:        0
Summary:        Multi pod and container log tailing for Kubernetes
License:        Apache-2.0
URL:            https://github.com/stern/stern
Source:         stern-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.26 >= 1.26.2

%description
Stern allows you to tail multiple pods on Kubernetes and multiple containers
within the pod. Each result is color coded for quicker debugging.

The query is a regular expression so the pod name can easily be filtered and
you don't need to specify the exact id (for instance omitting the deployment
id). If a pod is deleted it gets removed from tail and if a new pod is added it
automatically gets tailed.

When a pod contains multiple containers Stern can tail all of them too without
having to do this manually for each one. Simply specify the container flag to
limit what containers to show. By default all containers are listened to.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/stern/stern/cmd.version=%{version} \
   -X github.com/stern/stern/cmd.commit=${COMMIT_HASH} \
   -X github.com/stern/stern/cmd.date=${BUILD_DATE}" \
   -o bin/stern .

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
