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
%global project         exercism
%global repo            cli
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        2.4.0+git20170324.41427fc
Release:        0
Summary:        A Go based command line tool for exercism.io
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

%{go_nostrip}
%{go_provides}

%description
The CLI provides a way to do the problems on exercism.io.

%package -n exercism
Summary:        A Go based command line tool for exercism.io
Group:          Development/Languages/Golang
AutoReqProv:    Off

%{go_exclusivearch}

%description -n exercism
The CLI provides a way to do the problems on exercism.io.

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
%doc README.md CHANGELOG.md RELEASE.md LICENSE

%files -n exercism
%defattr(-,root,root)
%{_bindir}/exercism

%changelog
