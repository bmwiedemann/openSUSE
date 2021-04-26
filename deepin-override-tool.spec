#
# spec file for package deepin-override-tool
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define   import_path     github.com/linuxdeepin/deepin-desktop-schemas
%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            deepin-desktop-schemas

Name:           deepin-override-tool
Version:        5.9.5
Release:        0
Summary:        Deepin override tool
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        https://github.com/linuxdeepin/deepin-desktop-schemas/archive/%{version}/%{repo}-%{version}.tar.gz
Group:          System/GUI/Other
# BuildRequires:  golang(API) = 1.11
BuildRequires:  golang-packaging
BuildRequires:  golang(pkg.deepin.io/lib/keyfile)
Requires:       dconf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a tool for Deepin to creat schemas override profiles.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Deepin override tool codes
Group:          Development/Languages/Golang
Requires:       golang(pkg.deepin.io/lib/keyfile)
BuildArch:      noarch
AutoReqProv:    On
AutoReq:        Off
%{go_provides}

%description -n golang-%{provider}-%{project}-%{repo}
This is a tool for Deepin to creat schemas override profiles.

This package contains library source intended forbuilding other packages which
use import path with github.com/linuxdeepin/deepin-desktop-schemas prefix.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/*

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%defattr(-,root,root,-)

%changelog
