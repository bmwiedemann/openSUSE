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
%global project         russross
%global repo            blackfriday
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.4.0+git20151230.c8875c0
Release:        0
Summary:        Markdown processor implemented in Go
License:        BSD-2-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  golang(github.com/shurcooL/sanitized_anchor_name)
Requires:       golang(github.com/shurcooL/sanitized_anchor_name)
ExcludeArch:    s390

%{go_nostrip}
%{go_provides}

%description
Blackfriday is a Markdown processor implemented in Go. It is paranoid about its
input (so you can safely feed it user-supplied data), it is fast, it supports
common extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input. HTML output is currently supported, along
with Smartypants extensions. An experimental LaTeX output engine is also
included.

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
%doc README.md LICENSE.txt

%changelog
