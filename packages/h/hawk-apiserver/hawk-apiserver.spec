#
# spec file for package hawk-apiserver
#
# Copyright (c) 2026 SUSE LLC
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


%define www_base %{_datadir}/hawk

Name:           hawk-apiserver
Version:        0.1.0+git.1773237334.7d01e72
Release:        0
Summary:        Web server and API provider for Hawk
License:        GPL-3.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/ClusterLabs/hawk-apiserver
Source:         %{name}-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  libpacemaker-devel >= 1.1.16
BuildRequires:  libqb-devel
BuildRequires:  libxml2-devel
BuildRequires:  golang(API) >= 1.21
Requires:       pacemaker >= 1.1.16
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390

%{go_nostrip}

%description
This package contains the Hawk API server

%prep
%setup -q
%setup -q -T -D -a 3 # unpack go dependencies in vendor.tar.gz, which was prepared by the source services

%build
go build -mod=vendor \
         -buildmode=pie \
         -ldflags="-s -w -X main.version=%{version}" \
         -o hawk-apiserver

%install
install -D -m 0755 %{name} "%{buildroot}%{_sbindir}/%{name}"

# Web assets
install -d %{buildroot}%{www_base}/static
cp -a static/* %{buildroot}%{www_base}/static/

# Templates
install -d %{buildroot}%{www_base}/templates
cp -a templates/* %{buildroot}%{www_base}/templates/

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%dir %{www_base}
%dir %{www_base}/static
%{www_base}/static/*
%dir %{www_base}/templates
%{www_base}/templates/*

%changelog
