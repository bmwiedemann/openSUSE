#
# spec file for package librespeed-cli
#
# Copyright (c) 2024 SUSE LLC
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


%define sname speedtest-cli
Name:           librespeed-cli
Version:        1.0.11
Release:        0
Summary:        Command line client for LibreSpeed
License:        LGPL-3.0-only
URL:            https://github.com/librespeed/speedtest-cli
Source:         %{sname}-%{version}.tar.zst
Source1:        vendor.tar.gz
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.18

%description
Command line interface for LibreSpeed speed test backends, written in Go.

%prep
%autosetup -a1 -n %{sname}-%{version}

%build
DEFS_PATH="github.com/librespeed/speedtest-cli"
test -n "$SOURCE_DATE_EPOCH" || SOURCE_DATE_EPOCH=$(date +%%s)
go build -mod=vendor -buildmode=pie -ldflags "-w -s \
  -X \"${DEFS_PATH}/defs.ProgName=%{name}\" \
  -X \"${DEFS_PATH}/defs.ProgVersion=%{version}\" \
  -X \"${DEFS_PATH}/defs.BuildDate=$(date -u -d "@$SOURCE_DATE_EPOCH" '+%%Y-%%m-%%d %%H:%%M:%%S %%Z')\" \
" -trimpath

%install
install -Dm755 %{sname} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
