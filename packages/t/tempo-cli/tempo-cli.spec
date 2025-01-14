#
# spec file for package tempo-cli
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


Name:           tempo-cli
Version:        2.7.0
Release:        0
Summary:        CLI for the Grafana Tempo tracing backend
License:        Apache-2.0
URL:            https://github.com/grafana/tempo
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz

BuildRequires:  go >= 1.23.3

%description
Tempo CLI is a separate executable that contains utility functions related to
the Tempo software. Although it is not required for a working installation,
Tempo CLI can be helpful for deeper analysis or for troubleshooting.

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.Branch=v%{version} \
   -X main.Revision=${COMMIT_HASH:0:8} \
   -X main.Version=%{version}" \
   -o bin/%{name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
