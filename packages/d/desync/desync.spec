#
# spec file for package desync
#
# Copyright (c) 2026 openSUSE Contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           desync
Version:        1.1.3
Release:        0
Summary:        Content-addressed binary distribution tool compatible with casync
License:        BSD-3-Clause
URL:            https://github.com/folbricht/desync
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25

%description
desync is a content-addressed binary distribution tool and Go library that
implements casync-compatible chunk stores, index files, and archives. It can
chunk and reconstruct large files, reuse existing data as seeds, and access
local and remote chunk stores including HTTP(S), S3, GCS, SFTP, SSH, and OCI.

%prep
%autosetup -a1

%build
export GOFLAGS="-mod=vendor -trimpath"
%ifnarch ppc64
export GOFLAGS="${GOFLAGS} -buildmode=pie"
%endif

go build \
    -ldflags="-X main.version=v%{version}" \
    -o %{name} \
    ./cmd/desync

./%{name} manpage man

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -pm0644 man/*.1 %{buildroot}%{_mandir}/man1/

%check
export GOFLAGS="-mod=vendor"
go test ./...

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1%{?ext_man}

%changelog
