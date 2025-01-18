#
# spec file for package minio-client
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


Name:           minio-client
Version:        20250117T232550Z
Release:        0
Summary:        Client for MinIO
License:        AGPL-3.0-only
URL:            https://github.com/minio/mc
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        README.SUSE
BuildRequires:  go1.23
# obsolete some other package we had in the past
Provides:       minio-mc = %{version}-%{release}
Obsoletes:      minio-mc < %{version}-%{release}

%description
MinIO Client is a replacement for ls, cp, mkdir, diff and rsync commands for
filesystems and object storage.

Please note: In contrast to upstream this package provides the executable as
`minio-client`.

%package as-mc
Summary:        Actually have an %{_bindir}/mc binary for minio-client
Conflicts:      mc
Requires:       %{name} = %{version}
BuildArch:      noarch

%description as-mc
MinIO Client is a replacement for ls, cp, mkdir, diff and rsync commands for
filesystems and object storage.

This package restores the %{_bindir}/mc again

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags=" \
   -X github.com/minio/mc/cmd.Version=%{version} \
   -X github.com/minio/mc/cmd.ReleaseTag=${COMMIT_HASH}" \
   -o bin/%{name}

cp %{SOURCE2} README.SUSE

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
ln -s %{name} %{buildroot}/%{_bindir}/mc

%files
%doc README.md README.SUSE
%license LICENSE
%{_bindir}/%{name}

%files as-mc
%doc README.md README.SUSE
%license LICENSE
%{_bindir}/mc

%changelog
