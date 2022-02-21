#
# spec file for package velero-plugin-for-gcp
#
# Copyright (c) 2022 SUSE LLC
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


%define goipath github.com/vmware-tanzu/velero-plugin-for-gcp

Name:           velero-plugin-for-gcp
Version:        1.4.0
Release:        0
Summary:        Velero plugin for GCP
License:        Apache-2.0
Group:          Productivity/Archiving/Backup
URL:            https://velero.io
Source0:        https://github.com/vmware-tanzu/velero-plugin-for-gcp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14

%description
Plugins to support Velero on Google Cloud Platform (GCP)

%prep
%setup -q -a1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor -installsuffix "static" %{name}

%install
%goinstall

%files
%defattr(-,root,root)
%doc README.md
%%license LICENSE
%{_bindir}/%{name}

%changelog
