#
# spec file for package velero and velero-restic-restore-helper
#
# Copyright (c) 2019,2020 SUSE LLC, Nuernberg, Germany.
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

%define goipath github.com/vmware-tanzu/velero
%define commit 0665b05321eefeb7b7fdd6984750745b7429774f
%define gitstate clean

Name:           velero
Version:        1.3.1
Release:        0
Summary:        Backup program with deduplication and encryption
License:        Apache-2.0
Group:          Productivity/Archiving/Backup
URL:            https://velero.io
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12

%description
velero is a backup program. It supports verification, encryption,
snapshots and deduplication.

%package velero-restic-restore-helper
Summary:        Restic restore helper for %{name}
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Supplements:    packageand(velero:velero-restic-restore-helper)

%description velero-restic-restore-helper
Restic restore helper for %{name}.

%prep
%setup -q

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -installsuffix "static" -ldflags "-X %{goipath}/pkg/buildinfo.Version=%{version} -X %{goipath}/pkg/buildinfo.GitSHA=%{commit} -X %{goipath}/pkg/buildinfo.GitTreeState=%{gitstate}" cmd/velero
%gobuild -installsuffix "static" -ldflags "-X %{goipath}/pkg/buildinfo.Version=%{version} -X %{goipath}/pkg/buildinfo.GitSHA=%{commit} -X %{goipath}/pkg/buildinfo.GitTreeState=%{gitstate}" cmd/velero-restic-restore-helper

%install
%goinstall

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/velero
%{_bindir}/velero-restic-restore-helper

%changelog
