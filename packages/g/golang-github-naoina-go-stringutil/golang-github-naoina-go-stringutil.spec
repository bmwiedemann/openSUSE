#
# spec file for package golang
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global provider        github
%global provider_tld    com
%global project         naoina
%global repo            go-stringutil
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-naoina-%{repo}
Version:        0.1.0
Release:        0
Summary:        String functions for Golang
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.gz
#Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  golang-packaging

%{go_nostrip}
%{go_provides}

%description
This library contains various string manipulation functions for Golang.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%check
%gotest %{import_path}...

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE

%changelog
