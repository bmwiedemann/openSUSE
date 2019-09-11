#
# spec file for package golang-gopkgin-check
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global project         go-check
%global repo            check
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/check.v1

Name:           golang-gopkgin-check
Version:        0.0.0+git20161122.aa8c435
Release:        0
Summary:        Rich testing framework for the Go language
License:        BSD-3-Clause
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
The Go language provides an internal testing library, named "testing", which is
relatively slim due to the fact that the standard library correctness by itself
is verified using it. The gocheck package, on the other hand, expects the
standard library from Go to be working correctly, and builds on it to offer a
richer testing framework for libraries and applications to use.

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
#gotest %{import_path}...

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md TODO LICENSE

%changelog
