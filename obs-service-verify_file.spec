#
# spec file for package obs-service-verify_file
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


Name:           obs-service-verify_file
Version:        0.1.1
Release:        0
URL:            http://build.opensuse.org
Summary:        An OBS source service: file verification
License:        MIT
Group:          Development/Tools/Building
Source:         verify_file
Source1:        verify_file.service
Source2:        LICENSE.txt
Requires:       coreutils
%if 0%{?fedora_version} >= 17
Requires:       perl-MD5
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It allows to verify a file with a given sha256sum

%prep
%setup -q -D -T 0 -c
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{SOURCE0} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%doc LICENSE.txt
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
