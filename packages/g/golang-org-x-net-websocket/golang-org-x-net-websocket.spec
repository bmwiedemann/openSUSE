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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global provider        github
%global provider_tld    com
%global project         golang
%global repo            net
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/net

Name:           golang-org-x-%{repo}-websocket
Version:        1.12+git20190812.cdfb69a
Release:        0
Summary:        Websocket implements a client and server for the WebSocket protocol
License:        BSD-3-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

BuildRequires:  golang-packaging
BuildRequires:  xz

%{go_provides}

%description
Package websocket implements a client and server for the WebSocket protocol as specified in RFC 6455.

%prep
%setup -q -n %{repo}-%{version}
rm -rf $(find * -type d | grep -v '^websocket')

%build
%goprep %{import_path}
%gobuild ./websocket

%install
%goinstall
%gosrc
%gofilelist

%check
%gotest %{import_path}/websocket

%files -f file.lst
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README.md

%changelog
