#
# spec file for package zypper-docker
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define go_tool go
%define GO_BUILD_FLAGS ""

%define version_unconverted 2.0.0

Name:           zypper-docker
Version:        2.0.0
Release:        0
Summary:        Easy patch and update solution for Docker images
License:        Apache-2.0
Group:          Development/Languages/Other
Url:            https://github.com/SUSE/zypper-docker
Source0:        %{name}-%{version}.tar.xz
Source42:       zypper-docker-rpmlintrc
BuildRequires:  go >= 1.9
# Build fails with PIE enabled on ppc64le due to boo#1098017
%ifarch ppc64le
#!BuildIgnore: gcc-PIE
%endif
Requires:       libzypp > 9.34
BuildRequires:  libzypp > 9.34
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    %ix86

%description
The zypper-docker command line tool provides a quick way to patch and update
Docker images based either on SUSE Linux Enterprise or openSUSE.

zypper-docker mimics zypper command line syntax to ease its usage.

zypper-docker relies on zypper to perform the actual operations against Docker images.

%prep
%setup -q

%build
export GOPATH=$PWD/go
mkdir -p $GOPATH/src/github.com/SUSE

# Copy the vendor directory into the GOPATH.
cp -r $PWD/vendor/* $GOPATH/src
ln -s $PWD $GOPATH/src/github.com/SUSE/zypper-docker

%go_tool build %GO_BUILD_FLAGS

# build man pages
cd man
%go_tool run generate.go

%check
export GOPATH=$PWD/go
%go_tool test -v

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m755 zypper-docker-%{version} %{buildroot}%{_bindir}/zypper-docker

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/zypper-docker
%{_mandir}/man1/zypper-docker-*.1.gz
%{_mandir}/man1/zypper-docker.1.gz

%changelog
