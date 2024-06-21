#
# spec file for package obs-service-set_version
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?rhel} || 0%{?amzn} || ( 0%{?suse_version} && 0%{?suse_version} <= 1315 )
%bcond_with obs_scm_testsuite
%else
%bcond_without obs_scm_testsuite
%endif
%define service set_version

Name:           obs-service-%{service}
Version:        0.6.5
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%if %{with obs_scm_testsuite}
BuildRequires:  python3-ddt
BuildRequires:  python3-flake8
BuildRequires:  python3-packaging
%endif

%if !0%{?suse_version}
Requires:       python3
%endif
%if 0%{?suse_version}
Recommends:     python3-packaging
%endif

%description
This is a source service for openSUSE Build Service.

Very simply script to update the version in .spec or .dsc files according to
a given version or to the existing files.

%prep
%setup -q

%build
%if %{with obs_scm_testsuite}
%check
make test PYTHON=python3
%endif

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 set_version %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 set_version.service %{buildroot}%{_prefix}/lib/obs/service
# Doing %%python3_fix_shebang_path old fashioned way for the backward compatibility
sed -i "1s@#\\!.*python\S*@#\\!$(realpath /usr/bin/python3)@" \
    %{buildroot}%{_prefix}/lib/obs/service/set_version

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
