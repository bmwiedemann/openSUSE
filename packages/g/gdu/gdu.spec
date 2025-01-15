#
# spec file for package gdu
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


Name:           gdu
Version:        5.30.1
Release:        0
Summary:        Fast disk usage analyzer with console interface
License:        MIT
URL:            https://github.com/dundee/gdu
Source:         https://github.com/dundee/gdu/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
BuildRequires:  gzip
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.21

%description
Fast disk usage analyzer with console interface. Gdu is intended
primarily for SSD disks where it can fully utilize parallel
processing. HDDs work as well, but the performance gain is not so
huge.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
# construct a BUILD_DATE compatible with reproducible builds
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
# populate LDFLAGS -X metadata for bespoke gdu version output
# Not best practice for Go apps but gdu assumes this data is present
LDFLAGS="-X github.com/dundee/gdu/v5/build.Version=%{version} -X 'github.com/dundee/gdu/v5/build.Time=${BUILD_DATE}' -X github.com/dundee/gdu/v5/build.User=OBS"
go build -ldflags "$LDFLAGS" ./cmd/%{name}

# compress upstream provided man page
gzip %{name}.1

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m0755 -s %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
