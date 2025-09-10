#
# spec file for package python-susepubliccloudinfo
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

%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%{?sle15_python_module_pythons}
%endif
%global _sitelibdir %{%{pythons}_sitelib}

%define upstream_name susepubliccloudinfo
Name:           python-susepubliccloudinfo
Version:        1.4.2
Release:        0
Summary:        Query SUSE Public Cloud Info Service
License:        GPL-3.0-or-later
Group:          System/Management
Url:            https://github.com/SUSE-Enceladus/public-cloud-info-client
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       %{pythons}
Requires:       %{pythons}-docopt
Requires:       %{pythons}-lxml
Requires:       %{pythons}-requests
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Obsoletes:      python3-susepubliccloudinfo < %{version}

%description
Query the SUSE Public Cloud Information Service REST API

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/pint.1 %{buildroot}/%{_mandir}/man1
%fdupes %{buildroot}%{$python_sitelib}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/pint
%{_mandir}/man1/*
%dir %{_sitelibdir}/susepubliccloudinfoclient
%{_sitelibdir}/*

%changelog
