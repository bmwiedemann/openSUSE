#
# spec file for package obs-service-format_spec_file
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


Name:           obs-service-format_spec_file
Version:        20190411
Release:        0
Summary:        An OBS source service: reformats a spec file to SUSE standard
License:        GPL-2.0-only
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-format_spec_file
# osc service dr
Source:         %{name}-%{version}.tar.bz2
Requires:       obs-service-source_validator
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

This source service is formating the spec file to SUSE standard. The rational
behind is to make it easier to review spec files from unknown packagers.

This should be used in "trylocal" mode, so that osc is adapting the existing
spec file instead of creating a new one.

%prep

%setup -q

%build

%install
%make_install

%check
perl prepare_spec %{_topdir}/SOURCES/%{name}.spec

%files
%license COPYING
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
