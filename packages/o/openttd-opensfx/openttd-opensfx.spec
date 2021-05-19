#
# spec file for package openttd-opensfx
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


Name:           openttd-opensfx
Version:        1.0.1
Release:        0
Summary:        OpenSFX replacement sounds for OpenTTD
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later AND CDDL-1.1
Group:          Amusements/Games/Strategy/Other
URL:            https://github.com/OpenTTD/OpenSFX
Source0:        https://github.com/OpenTTD/OpenSFX/archive/refs/tags/%{version}.tar.gz
BuildRequires:  catcodec
Requires:       openttd-data
Provides:       opensfx
BuildArch:      noarch

%description
OpenSFX replacement sounds for OpenTTD. The last required step
to make OpenTTD independent.

%prep
%setup -q -n OpenSFX-%{version}

%build
%make_build REPO_VERSION=%{version} _V=

%install
make install INSTALL_DIR=%{buildroot}%{_datadir}/openttd/data REPO_VERSION=%{version} _V= TAR_FLAGS='--mtime="@${SOURCE_DATE_EPOCH}" --sort=name --owner=0 --group=0 --numeric-owner --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime,delete=mtime -cf'

%files
%license docs/license.txt
%doc docs/changelog.txt docs/readme.txt
%dir %{_datadir}/openttd
%dir %{_datadir}/openttd/data
%{_datadir}/openttd/data/opensfx-%{version}.tar

%changelog
