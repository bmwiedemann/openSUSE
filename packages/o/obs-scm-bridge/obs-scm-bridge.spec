#
# spec file for package obs-scm-bridge
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?fedora} || 0%{?rhel}
%define build_pkg_name obs-build
%else
%define build_pkg_name build
%endif

# this needs to match the usd python in github test suite
%define our_python3_version 11

Name:           obs-scm-bridge
Version:        0.7.4
Release:        0
Summary:        A help service to work with git repositories in OBS
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-scm-bridge
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  python3%{our_python3_version}
BuildRequires:  python3%{our_python3_version}-PyYAML
Requires:       %{build_pkg_name} >= 20211125
# these are just recommends in build package, but we need it here
Requires:       perl(Date::Parse)
Requires:       git-lfs
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::SSL)
Requires:       perl(Pod::Usage)
Requires:       perl(Time::Zone)
Requires:       perl(URI)
Requires:       perl(XML::Parser)
Requires:       perl(YAML::LibYAML)
BuildArch:      noarch
Requires:       python3%{our_python3_version}-PyYAML
Recommends:     python3%{our_python3_version}-packaging

%description

%prep
%autosetup

%build
sed -i 's,^#!/usr/bin/python3.*,#!/usr/bin/python3.%our_python3_version,' obs_scm_bridge

%install
make DESTDIR=%{buildroot} install

mkdir -p %buildroot/etc/obs/services/scm-bridge
echo "src.opensuse.org" > %buildroot/etc/obs/services/scm-bridge/critical-instances
# we would need to configure permissions and owner ship for this file
# but we don't want to enforce obs server package for userid
#echo "" > %buildroot/etc/obs/services/scm-bridge/credentials

%files
%{_prefix}/lib/obs/service
%dir /etc/obs
%dir /etc/obs/services
%dir /etc/obs/services/scm-bridge
%config(noreplace) /etc/obs/services/scm-bridge/critical-instances

%check
# the test suite requires online resources unfortunatly
# so let's at least test if our python version understands our syntax
python3.%our_python3_version obs_scm_bridge --help

%changelog
