#
# spec file for package golang
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


%global provider        github
%global provider_tld    com
%global project         shurcool
%global repo            sanitized_anchor_name
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.%{provider_tld}/shurcooL/%{repo}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.0.0+git20151027.10ef21a
Release:        0
Summary:        Go function to create sanitized anchor names
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz
ExcludeArch:    s390

%{go_nostrip}
%{go_provides}

%description
Package sanitized_anchor_name provides a func to create sanitized anchor names.
Its logic can be reused by multiple packages to create interoperable anchor
names and links to those anchors. At this time, it does not try to ensure that
generated anchor names are unique, that responsibility falls on the caller.

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
