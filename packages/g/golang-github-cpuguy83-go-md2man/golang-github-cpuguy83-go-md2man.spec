#
# spec file for package golang-github-cpuguy83-go-md2man
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
%global project         cpuguy83
%global repo            go-md2man
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        2.0.0+git20190314.f79a8a8
Release:        0
Summary:        Convert markdown into man pages
License:        MIT
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
Tool to converts markdown into man pages.

%package -n go-md2man
Summary:        Tool to converts markdown into man pages
Group:          Development/Languages/Golang
Provides:       go-go-md2man = %{version}
AutoReqProv:    Off

%{go_exclusivearch}

%description -n go-md2man
Tool to converts markdown into man pages.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild --mod=vendor "" ...

%install
%goinstall
%gosrc
%gofilelist

%check
%gotest --mod=vendor "" ...

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.md

%files -n go-md2man
%defattr(-,root,root)
%{_bindir}/go-md2man

%changelog
