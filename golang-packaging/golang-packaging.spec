#
# spec file for package golang-packaging
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


Name:           golang-packaging
Version:        15.0.11
Release:        0
Summary:        A toolchain to help packaging golang
License:        GPL-3.0-only
Group:          Development/Languages/Golang
Url:            https://github.com/openSUSE/%{name}
Source:         %{name}-%{version}.tar.xz
Patch:          ppc64-nopie.patch

BuildRequires:  rpm
BuildRequires:  xz
Requires:       go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A toolchain to help packaging golang, written in bash.

%prep
%setup -q
%patch -p1

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
mkdir -p %{buildroot}%{_prefix}/lib/rpm/

install -m0755 golang.prov %{buildroot}%{_prefix}/lib/rpm/
install -m0755 golang.req %{buildroot}%{_prefix}/lib/rpm/
install -m0755 golang.sh %{buildroot}%{_prefix}/lib/rpm/
install -m0644 macros.go %{buildroot}%{_sysconfdir}/rpm/

%if 0%{?suse_version} >= 1320
mkdir -p %{buildroot}%{_prefix}/lib/rpm/fileattrs
install -m0644 golang.attr %{buildroot}%{_prefix}/lib/rpm/fileattrs/
%endif

%files
%defattr(-,root,root)
%doc README.md CHANGELOG COPYING
%{_prefix}/lib/rpm/golang.prov
%{_prefix}/lib/rpm/golang.req
%{_prefix}/lib/rpm/golang.sh
%config %{_sysconfdir}/rpm/macros.go

%if %{?suse_version} >= 1320
%{_prefix}/lib/rpm/fileattrs/golang.attr
%endif

%changelog
