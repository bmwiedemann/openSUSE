#
# spec file for package python3-gcemetadata
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


%define upstream_name gcemetadata
Name:           python3-gcemetadata
Version:        1.0.3
Release:        0
Summary:        Python module for collecting instance metadata from GCE
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE/Enceladus
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python3
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       python-gcemetadata = %{version}
Obsoletes:      python-gcemetadata < %{version}

%description
A module for collecting instance metadata from Google Compute Engine.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/gcemetadata.1 %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/gcemetadata.1

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_mandir}/man*/*
%dir %{python3_sitelib}/%{upstream_name}
%dir %{python3_sitelib}/%{upstream_name}-%{version}-py%{py3_ver}.egg-info
%{_bindir}/*
%{python3_sitelib}/*

%changelog
