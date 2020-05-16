#
# spec file for package golang-org-x-sync
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
%global repo            sync
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/sync

Name:           golang-org-x-%{repo}
Version:        0.0.0+git20200317.43a5402
Release:        0
Summary:        Go concurrency primitives
License:        BSD-3-Clause
Group:          Development/Languages/Golang
URL:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  golang(golang.org/x/net/context)
Requires:       golang(golang.org/x/net/context)

BuildArch:      noarch

%{go_nostrip}
%{go_provides}

%description
This repository provides Go concurrency primitives in addition to the ones
provided by the language and "sync" and "sync/atomic" packages.

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
%defattr(-,root,root,-)
%doc README.md PATENTS AUTHORS CONTRIBUTORS CONTRIBUTING.md
%license LICENSE

%changelog
