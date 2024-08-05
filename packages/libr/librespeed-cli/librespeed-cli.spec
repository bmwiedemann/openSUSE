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

Name:           librespeed-cli
Version:        1.0.10
Release:        0
Summary:        Command line client for LibreSpeed
License:        LGPL-3.0
Url:            https://github.com/librespeed/speedtest-cli
Source:         https://github.com/librespeed/speedtest-cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.14

%description 
Command line interface for LibreSpeed speed test backends, written in Go.

%prep 
%autosetup -a1 -n speedtest-cli-%{version}

%build 
go build -mod=vendor

%install 
install -Dm755 speedtest-cli %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
