#
# spec file for package chartmuseum
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define revision f388036

Name:           chartmuseum
Version:        0.2.8
Release:        0
Summary:        Helm Chart Repository with support for Amazon S3 and Google Cloud Storage
License:        MIT
Group:          Development/Languages/Other
Url:            https://github.com/kubernetes-helm/chartmuseum
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  go >= 1.7
BuildRequires:  golang-packaging
BuildRequires:  xz
%{go_nostrip}
%{go_provides}

%description
ChartMuseum is a Helm Chart Repository written in Go (Golang), with
support for Google Cloud Storage and Amazon S3.

%prep
mkdir -p %{_builddir}/src/github.com/kubernetes-helm
tar -C %{_builddir}/src/github.com/kubernetes-helm -xJf ../SOURCES/%{name}-%{version}.tar.xz
tar -C %{_builddir}/src/github.com/kubernetes-helm/chartmuseum -xJf %{SOURCE1}

%build
export GOPATH="%{_builddir}:$GOPATH"
go build -v -i --ldflags="-w -X main.Version=%{version} -X main.Revision=%{revision}" -o src/github.com/kubernetes-helm/chartmuseum/bin/linux/amd64/chartmuseum src/github.com/kubernetes-helm/chartmuseum/cmd/chartmuseum/main.go

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 src/github.com/kubernetes-helm/chartmuseum/bin/linux/amd64/chartmuseum %{buildroot}%{_bindir}/chartmuseum

%files
%defattr(-,root,root,-)
%doc src/github.com/kubernetes-helm/chartmuseum/README.md
%license src/github.com/kubernetes-helm/chartmuseum/LICENSE
%{_bindir}/chartmuseum

%changelog
