#
# spec file for package kopia
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


Name:           kopia
Version:        0.18.1
Release:        0
Summary:        Cross-platform backup tool with fast incremental backups
License:        Apache-2.0
URL:            https://github.com/kopia/kopia
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Kopia is a fast and secure open-source backup/restore tool that allows you to
create encrypted snapshots of your data and save the snapshots to remote or
cloud storage of your choice, to network-attached storage or server, or locally
on your machine. Kopia does not 'image' your whole machine. Rather, Kopia
allows you to backup/restore any and all files/directories that you deem are
important or critical.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/kopia/kopia/repo.BuildVersion=%{version} \
   -X github.com/kopia/kopia/repo.BuildInfo=${COMMIT_HASH} \
   -X github.com/kopia/kopia/repo.BuildGitHubRepo=kopia/kopia" \
   -o bin/%{name} github.com/kopia/kopia

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
