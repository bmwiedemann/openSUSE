#
# spec file for package silver-surfer
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

%define executable_name kubedd

Name:           silver-surfer
Version:        0.1.4
Release:        0
Summary:        Kubernetes objects api-version compatibility checker
License:        Apache-2.0
URL:            https://github.com/devtron-labs/silver-surfer
Source:         silver-surfer-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22
Provides:       kubedd = %{version}-%{release}

%description
Currently there is no easy way to upgrade Kubernetes objects in case of
Kubernetes newer versions. There are some tools which are available for this
purpose, but we found them inadequate for migration requirements.

kubedd is a tool to check issues in migration of Kubernetes yaml objects from
one Kubernetes version to another.

It uses openapi spec provided by the Kubernetes with releases, for eg. in case
of target kubernetes version 1.27 openapi spec for 1.27, to validate the
kubernetes objects for depreciation or non-conformity with openapi spec.

Supported input formats
* Directory containing files to be validated
* Read kubernetes objects directly from cluster. Uses
  kubectl.kubernetes.io/last-applied-configuration to get last applied
  configuration and in its absence uses the manifest itself.

It provides details of issues with the Kubernetes object in case they are
migrated to cluster with newer Kubernetes version.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/silver-surfer.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

sed -i '/^\sversion/ s/0.1.0/%{version}/' main.go
sed -i "/^\scommit/ s/none/${COMMIT_HASH}/" main.go
sed -i "/^\sdate/ s/unknown/${BUILD_DATE}/" main.go

CGO_ENABLED=0 go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{executable_name} .

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
