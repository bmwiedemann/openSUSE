#
# spec file for package golang-github-linuxdeepin-go-dbus-factory
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
%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            go-dbus-factory
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.8.6
Release:        0
Summary:        Golang DBus factory
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/go-dbus-factory
Source0:        https://github.com/linuxdeepin/go-dbus-factory/archive/%{version}/%{repo}-%{version}.tar.gz
Group:          Development/Languages/Golang
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  golang-github-linuxdeepin-go-lib
BuildRequires:  golang-github-linuxdeepin-go-gir-generator
BuildRequires:  jq
BuildRequires:  libxml2-tools
Requires:       golang(github.com/linuxdeepin/go-x11-client)
Requires:       golang-github-linuxdeepin-go-x11-client
BuildArch:      noarch
Autoreq:        Off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}

%description
Golang DBus factory for Deepin Desktop Environment.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}

%install
%gosrc
%gofilelist

%fdupes %{buildroot}

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
