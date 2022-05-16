#
# spec file for package gdmd
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


%if 0%{?suse_version} < 1550
%global gdc_version 10
%global gdc_suffix -%{gdc_version}
%endif

Name:           gdmd%{?gdc_suffix}
Version:        20210818T144245
Release:        0
Summary:        DMD compatible wrapper for the GDC D compiler
License:        BSL-1.0
URL:            https://github.com/D-Programming-GDC/gdmd
Source:         gdmd-%{version}.tar.xz
Requires:       gcc%{?gdc_version}-d
BuildArch:      noarch

%description
GDMD is a wrapper for the GDC D compiler to provide a DMD compatible interface.

%prep
%autosetup -p1 -n gdmd-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%make_install prefix=%{_prefix} program_suffix=%{?gdc_suffix}

%files
%{_bindir}/gdmd%{?gdc_suffix}
%{_mandir}/man1/gdmd%{?gdc_suffix}.1*

%changelog
