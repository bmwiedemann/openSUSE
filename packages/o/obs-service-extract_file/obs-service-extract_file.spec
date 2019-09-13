#
# spec file for package obs-service-extract_file
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           obs-service-extract_file
Summary:        An OBS source service: Extract a file from an archive
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        0.4
Release:        0
Source:         %{name}-%{version}.tar.gz
Requires:       bzip2
Requires:       gzip
Requires:       tar
Requires:       unzip
Requires:       xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports to extract a file from an archive, for example a spec file from a tar.


%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0755 extract_file $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0644 extract_file.service $RPM_BUILD_ROOT/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir /usr/lib/obs
/usr/lib/obs/service

%changelog
