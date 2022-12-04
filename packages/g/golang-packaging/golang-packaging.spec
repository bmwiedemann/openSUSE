#
# spec file for package golang-packaging
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


%{?!_rpmmacrodir:%define _rpmmacrodir /etc/rpm}

Name:           golang-packaging
Version:        15.0.17
Release:        0
Summary:        A toolchain to help packaging golang
License:        GPL-3.0-only
Group:          Development/Languages/Golang
URL:            https://github.com/openSUSE/%{name}
Source:         %{name}-%{version}.tar.xz

BuildRequires:  rpm
BuildRequires:  xz
Requires:       go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A toolchain to help packaging golang, written in bash.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}

install -m0755 golang.prov %{buildroot}%{_rpmconfigdir}
install -m0755 golang.req %{buildroot}%{_rpmconfigdir}
install -m0755 golang.sh %{buildroot}%{_rpmconfigdir}
install -m0644 macros.go %{buildroot}%{_rpmmacrodir}

%if 0%{?suse_version} >= 1320
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -m0644 golang.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
%endif

%files
%defattr(-,root,root)
%doc README.md CHANGELOG
%license COPYING
%{_rpmconfigdir}/golang.prov
%{_rpmconfigdir}/golang.req
%{_rpmconfigdir}/golang.sh
%{_rpmmacrodir}/macros.go

%if 0%{?suse_version} >= 1320
%{_rpmconfigdir}/fileattrs/golang.attr
%endif

%changelog
