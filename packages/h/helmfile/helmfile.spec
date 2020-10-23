#
# spec file for package helmfile
#
# Copyright (c) 2020 SUSE LLC
#		2020 Manfred Hollstein <manfred.h@gmx.net>
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

%define git_commit 9ec4a85821c06601dd3fe35c4effbed59089b48e
Name:           helmfile
Version:        0.132.0
Release:        0
Summary:        Deploy Kubernetes Helm Charts
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/roboll/helmfile
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:	helm
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.14
%{go_nostrip}
%{go_provides}

%description
Helmfile is a declarative spec for deploying helm charts. It lets you...

 * Keep a directory of chart value files and maintain changes in version control.
 * Apply CI/CD to configuration changes.
 * Periodically sync to avoid skew in environments.

To avoid upgrades for each iteration of helm, the helmfile executable
delegates to helm - as a result, helm must be installed.

%prep
%setup -qa1

%build
go build -mod=vendor -buildmode=pie

%install
make TAG=v%{version} install
mkdir -p %{buildroot}%{_bindir}
install -m755 ${HOME}/go/bin/helmfile %{buildroot}/%{_bindir}/helmfile

%files
%doc README.md
%license LICENSE
%{_bindir}/helmfile

%changelog
