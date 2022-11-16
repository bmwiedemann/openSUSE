#
# spec file for package obs-scm-bridge
#
# Copyright (c) 2022 SUSE LLC
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

Name:           obs-scm-bridge
Version:        0.2.1
Release:        0
Summary:        A help service to work with git repositories in OBS
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-scm-bridge
Source0:        %{name}-%{version}.tar.xz
Requires:       %{build_pkg_name} >= 20211125
# these are just recommends in build package, but we need it here
Requires:       perl(Date::Parse)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::SSL)
Requires:       perl(Pod::Usage)
Requires:       perl(Time::Zone)
Requires:       perl(URI)
Requires:       perl(XML::Parser)
Requires:       perl(YAML::LibYAML)
BuildArch:      noarch
Recommends:     python3-packaging

%description

%prep
%autosetup

%build

%install
make DESTDIR=%{buildroot} install

%files
%{_prefix}/lib/obs/service

%changelog
