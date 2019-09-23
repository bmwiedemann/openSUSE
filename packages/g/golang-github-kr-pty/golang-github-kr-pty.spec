#
# spec file for package golang
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


%global provider        github
%global provider_tld    com
%global project         kr
%global repo            pty
# https://github.com/kr/pty
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.1.3
Release:        0
Summary:        PTY interface for Go
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{url}/archive/v%{version}/%{repo}-%{version}.tar.gz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildArch:      noarch
%{go_nostrip}
%{go_provides}

%description
Pty is a Go package for using unix pseudo-terminals.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%fdupes %{buildroot}

%check
%gotest %{import_path}...

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md License

%changelog
