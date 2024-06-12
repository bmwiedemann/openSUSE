#
# spec file for package minio-client
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define archive_name mc
%define binary_name minio-client

Name:           minio-client
Version:        20240610T164415Z
Release:        0
Summary:        Client for MinIO
License:        AGPL-3.0-only
URL:            https://github.com/minio/mc
Source:         %{archive_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.21 >= 1.21.8

%description
MinIO Client is a replacement for ls, cp, mkdir, diff and rsync commands for filesystems and object storage.

Please note: In contrast to upstream this package provides the executable as `minio-client`.

%prep
%autosetup -p1 -a1 -n %{archive_name}-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath -tags kqueue \
   -ldflags="-s -w -X github.com/minio/mc/cmd.Version=%{version} \
	-X github.com/minio/mc/cmd.ReleaseTag=%{version}" \
   -o bin/%{binary_name}

%install
# Install the binary.
install -D -m 0755 bin/%{binary_name} "%{buildroot}/%{_bindir}/%{binary_name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{binary_name}

%changelog
