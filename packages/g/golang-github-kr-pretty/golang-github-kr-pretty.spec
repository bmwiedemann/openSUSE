#
# spec file for package golang
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
%global project         kr
%global repo            pretty
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.0.0+git20160823.cfb55aa
Release:        0
Summary:        Pretty printing for Go values
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  golang(github.com/kr/text)
Requires:       golang(github.com/kr/text)

%{go_nostrip}
%{go_provides}

%description
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal. It provides a
function, Formatter, that can be used with any function that accepts a format
string. This package also provides a convenience wrapper for each function in
package fmt that takes a format string.

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
%doc Readme License

%changelog
