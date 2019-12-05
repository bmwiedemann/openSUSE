#
# spec file for package python-ec2metadata
#
# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# MUST remain Python 2 based until EOL of SLES 11 in March 2019

%define upstream_name ec2metadata
Name:           python3-ec2metadata
Version:        3.0.2
Release:        0
Summary:        Collect instance metadata in EC2
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/SUSE-Enceladus/ec2metadata
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python3
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       python-ec2metadata = %{version}
Obsoletes:      python-ec2metadata < %{version}


%description
Collect instance meta data in Amazon Compute CLoud instances

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/ec2metadata.1 %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/ec2metadata.1

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_mandir}/man*/*
%dir %{python3_sitelib}/%{upstream_name}
%dir %{python3_sitelib}/%{upstream_name}-%{version}-py%{py3_ver}.egg-info
%{_bindir}/*
%{python3_sitelib}/%{upstream_name}/*
%{python3_sitelib}/*egg-info/*

%changelog
