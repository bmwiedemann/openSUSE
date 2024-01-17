#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


%define service refresh_patches

Name:           obs-service-%{service}
Version:        0.3.9+git.1625238904.d59f20e
Release:        0
Summary:        An OBS source service: Refreshs local patches
%if 0%{?mageia}
# Careful: Don't run the spec-cleaner service on this one (osc commit --noservice)
License:        ASL 2.0
Group:          Development/Tools
%else
License:        Apache-2.0
Group:          Development/Tools/Building
%endif
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3
Requires:       python3
Requires:       quilt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It refreshes locals patches by using quilt.

%prep
%setup -q
# fix rpmlint error for script interpreter lines
sed -i '1 s/env python.*/python3/' refresh_patches

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 refresh_patches %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 refresh_patches.service %{buildroot}%{_prefix}/lib/obs/service
%if 0%{?_licensedir:%{?suse_version} < 1500}
mkdir -p %{buildroot}%{_datadir}/licenses
%endif

%check
# check the script interpreter line and imports
./refresh_patches -h

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%{!?_licensedir:%global license %%doc}
%license LICENSE-2.0
%if 0%{?_licensedir:%{?suse_version} < 1500}
%dir %{_datadir}/licenses
%endif

%changelog
