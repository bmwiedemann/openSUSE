#
# spec file for package obs-service-source_validator
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


%if 0%{?suse_version}
%define build_pkg_name build
%else
%define build_pkg_name obs-build
%endif

Name:           obs-service-source_validator
Version:        0.37
Release:        0
Summary:        An OBS source service: running all the osc source-validator checks
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-source_validator
# use osc service mr to update
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  %{build_pkg_name}
BuildRequires:  zstd
Requires:       %{_bindir}/cpio
Requires:       %{_bindir}/xmllint
Requires:       %{build_pkg_name}
Requires:       patch
Requires:       perl-TimeDate
Requires:       unzip
Provides:       osc-source_validator = %{version}
Obsoletes:      osc-source_validator <= 0.1
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       gpg2
%else
# Fedora
Requires:       gnupg2
%endif

%description
This is a source service for openSUSE Build Service.

This service runs all checks as required by openSUSE:Factory project. This can be used
to guarantee that all checks succeed also on the service side. This plugin can be
used via project wide defined services.

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/licenses
%make_install

%check
%make_build test

%files
%license COPYING
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/licenses
%endif
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
