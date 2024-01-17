#
# spec file for package golang-org-x-sys
#
# Copyright (c) 2020 SUSE LLC
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


%global provider        github
%global provider_tld    com
%global project         golang
%global repo            sys
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/sys

Name:           golang-org-x-%{repo}
Version:        0.0.0+git20200420.1957bb5
Release:        0
Summary:        Go packages for low-level interaction with the operating system
License:        BSD-3-Clause
Group:          Development/Languages/Golang
URL:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

%{go_nostrip}
%{go_provides}

%description
This repository holds supplemental Go packages for low-level interactions with
the operating system.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%files -f file.lst
%license LICENSE
%{_bindir}/*
%doc README.md PATENTS AUTHORS CONTRIBUTORS CONTRIBUTING.md  

%changelog
