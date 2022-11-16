#
# spec file for package helmfile
#
# Copyright (c) 2022 SUSE LLC
#               2021 Manfred Hollstein <manfred.h@gmx.net>
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


%define git_commit f09ec18aa9d555f6c8f668bfbcf084a6e5e8ee6b
Name:           helmfile
Version:        0.148.1
Release:        0
Summary:        Deploy Kubernetes Helm Charts
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/helmfile/helmfile
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:       helm
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.19
Obsoletes:      %{name}-bash-completion < %{version}
Obsoletes:      %{name}-zsh-completion < %{version}

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
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
SOURCE_DATE_EPOCH=$(date -u -d "${modified}" "+%s")
export SOURCE_DATE_EPOCH
rm -f source_date_epoch
echo SOURCE_DATE_EPOCH=$SOURCE_DATE_EPOCH > source_date_epoch
go build -mod=vendor -buildmode=pie

%install
. ./source_date_epoch
export SOURCE_DATE_EPOCH
make TAG=v%{version} install
mkdir -p %{buildroot}%{_bindir}
install -m755 ${HOME}/go/bin/helmfile %{buildroot}/%{_bindir}/helmfile

%files
%doc README.md
%license LICENSE
%{_bindir}/helmfile

%changelog
