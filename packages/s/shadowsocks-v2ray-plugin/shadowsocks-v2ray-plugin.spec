#
# spec file for package shadowsocks-v2ray-plugin
#
# Copyright (c) 2020 SUSE LLC
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


%define   provider        github
%define   provider_tld    com
%define   project         shadowsocks
%define   repo            v2ray-plugin
# https://github.com/shadowsocks/v2ray-plugin
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     %{provider_prefix}

Name:           shadowsocks-%{repo}
Version:        1.3.1
Release:        0
Summary:        SIP003 plugin for shadowsocks
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://github.com/shadowsocks/v2ray-plugin
Source0:        https://github.com/shadowsocks/v2ray-plugin/archive/v%{version}/%{repo}-%{version}.tar.gz
Source1:        vendor.tar.xz
# PATCH-FIX-UPSTEAM switch-to-v2fly.patch hillwood@opensuse.org - Switch to v2fly
Patch0:         switch-to-v2fly.patch
BuildRequires:  fdupes
BuildRequires:  golang-github-v2fly-v2ray-core
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.15
BuildRequires:  golang(v2ray.com/core)
AutoReqProv:    Off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Additional mobile libraries
Group:          Development/Languages/Golang
Requires:       golang(v2ray.com/core)
BuildRequires:  golang-github-v2fly-v2ray-core
BuildArch:      noarch

%description -n golang-%{provider}-%{project}-%{repo}
Yet another SIP003 plugin for shadowsocks, based on v2ray

This package provide source code for shadowsocks-%{repo}

%prep
%autosetup -p1 -a1 -n %{repo}-%{version}
rm go.sum go.mod

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/v2ray-plugin

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%defattr(-,root,root)
%doc README.md
%license LICENSE

%changelog
