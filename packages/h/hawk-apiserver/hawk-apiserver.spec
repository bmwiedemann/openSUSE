#
# spec file for package hawk-apiserver
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hawk-apiserver
Version:        0.0.3
Release:        0
Summary:        Web server and API provider for Hawk
License:        GPL-3.0-or-later
Group:          Productivity/Clustering/HA
Url:            https://github.com/ClusterLabs/hawk-apiserver
Source:         %{name}-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  libpacemaker-devel >= 1.1.16
BuildRequires:  libqb-devel
BuildRequires:  libxml2-devel
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.9
Requires:       pacemaker >= 1.1.16
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390
%{go_provides}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
This package contains the Hawk API server
and reverse proxy. It is used by Hawk to
serve the API and static files as quickly
as possible.

%prep
%setup -q

%build
%{goprep} github.com/ClusterLabs/hawk-apiserver
%{gobuild}

%install
%{goinstall}
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}
install -Dm0644 man/hawk-apiserver.8 %{buildroot}%{_mandir}/man8/hawk-apiserver.8

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/man8/hawk-apiserver.8.gz
%if 0%{?suse_version} == 1315
%exclude %go_contribdir/github.com/ClusterLabs/hawk-apiserver/vendor/github.com/ClusterLabs/go-pacemaker.a
%exclude %go_contribdir/github.com/ClusterLabs/hawk-apiserver/vendor/github.com/sirupsen/logrus.a
%exclude %go_contribdir/github.com/ClusterLabs/hawk-apiserver/vendor/golang.org/x/crypto/ssh/terminal.a
%exclude %go_contribdir/github.com/ClusterLabs/hawk-apiserver/vendor/golang.org/x/sys/unix.a
%endif

%changelog
