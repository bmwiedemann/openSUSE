#
# spec file for package openttd-openmsx
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


Name:           openttd-openmsx
Version:        0.4.0
Release:        0
Summary:        An OpenTTD Music set
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://github.com/OpenTTD/OpenMSX
Source0:        https://github.com/OpenTTD/OpenMSX/archive/refs/tags/%{version}.tar.gz
Patch0:         0001-openmsx-fix-install-target.patch
BuildRequires:  python
Requires:       openttd-data >= 1.2
BuildArch:      noarch
%if 0%{?suse_version} || 0%{?mdkversion}
Recommends:     timidity
%endif

%description
OpenMSX is a base music set for OpenTTD.

%prep
%setup -q -n OpenMSX-%{version}
%patch0

%build
%make_build PYTHON=%{_bindir}/python3 REPO_VERSION=%{version} _V=

%install
%make_install INSTALL_DIR=%{buildroot}%{_datadir}/openttd/baseset PYTHON=%{_bindir}/python3 REPO_VERSION=%{version} _V=

%define omsxdir %{_datadir}/openttd/baseset/openmsx-%{version}

%files
%license %{omsxdir}/license.txt
%doc %{omsxdir}/changelog.txt
%doc %{omsxdir}/readme.txt
%dir %{_datadir}/openttd
%dir %{_datadir}/openttd/baseset
%dir %{omsxdir}
%{omsxdir}/openmsx.obm
%{omsxdir}/*.mid

%changelog
