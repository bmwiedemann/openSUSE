#
# spec file for package openttd-openmsx
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           openttd-openmsx
Version:        0.3.1
Release:        1%{?dist}
Summary:        An OpenTTD Music set
License:        GPL-2.0
Group:          Amusements/Games/Strategy/Other

Url:            http://dev.openttdcoop.org/projects/openmsx
Source0:        http://bundles.openttdcoop.org/openmsx/releases/%{version}/openmsx-%{version}-source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

BuildRequires:  python
Requires:       openttd-data >= 1.2
%if 0%{?suse_version} || 0%{?mdkversion}
Recommends:     timidity
%endif

%description
OpenMSX is an open source replacement for the original Transport Tycoon Deluxe (TTD) 
music. All contributions are licensed under the GPL v2.

%prep
%setup -qn openmsx-%{version}-source

%build
make %{?_smp_mflags} _V=

%install
%define omsxdir %{_datadir}/openttd/baseset
make install INSTALL_DIR=%{buildroot}%{omsxdir} _V=
#openmsx adds a versioned dir to the install dir
%define omsxdir %{_datadir}/openttd/baseset/openmsx-%{version}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/openttd
%dir %{_datadir}/openttd/baseset
%dir %{omsxdir}
%doc %{omsxdir}/changelog.txt
%doc %{omsxdir}/license.txt
%doc %{omsxdir}/readme.txt
%{omsxdir}/openmsx.obm
%{omsxdir}/*.mid

%changelog
