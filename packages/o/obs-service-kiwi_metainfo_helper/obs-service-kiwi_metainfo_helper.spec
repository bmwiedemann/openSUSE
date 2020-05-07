#
# spec file for package obs-service-kiwi_metainfo_helper
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


Name:           obs-service-kiwi_metainfo_helper
Version:        0.0
Release:        0
Summary:        Service for substituting various variables in kiwi recipes
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://build.opensuse.org
Source0:        kiwi_metainfo_helper.service
Source1:        kiwi_metainfo_helper
Source2:        README
Requires:       sed
# For os-release
%if 0%{?is_opensuse}
Requires:       openSUSE-release
%else
Requires:       sles-release
%endif
BuildArch:      noarch

%description
This service can be used during buildtime to gain access to various variables
in kiwi recipes.

%prep
%setup -q -D -T -n .
cp %{SOURCE2} .

%build

%install

mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{SOURCE0} %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{SOURCE1} %{buildroot}%{_prefix}/lib/obs/service

%files
%doc README
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
