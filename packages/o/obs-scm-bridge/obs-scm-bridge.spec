#
# spec file for package obs-scm-bridge
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if %{undefined primary_python}
%define primary_python python3
%endif

%if 0%{?fedora} || 0%{?rhel}
%define build_pkg_name obs-build
%else
%define build_pkg_name build
%endif

Name:           obs-scm-bridge
Version:        0.7.4
Release:        0
Summary:        A help service to work with git repositories in OBS
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-scm-bridge
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  %{primary_python}
BuildRequires:  %{primary_python}-PyYAML
Requires:       %{build_pkg_name} >= 20211125
# these are just recommends in build package, but we need it here
Requires:       perl(Date::Parse)
Requires:       git-lfs
%if 0%{?opensuse_version}
BuildRequires:  git-core >= 2.46
Requires:       git-core >= 2.46
%else
BuildRequires:  git >= 2.46
Requires:       git >= 2.46
%endif
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::SSL)
Requires:       perl(Pod::Usage)
Requires:       perl(Time::Zone)
Requires:       perl(URI)
Requires:       perl(XML::Parser)
Requires:       perl(YAML::LibYAML)
BuildArch:      noarch
Requires:       %{primary_python}-PyYAML
Recommends:     %{primary_python}-packaging

%description

%prep
%autosetup

%build

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
python3 obs_scm_bridge --help

%changelog
