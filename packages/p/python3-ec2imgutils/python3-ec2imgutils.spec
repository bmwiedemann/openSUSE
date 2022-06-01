#
# spec file for package python3-ec2imgutils
#
# Copyright (c) 2018 SUSE Linux GmbH, Nuernberg, Germany.
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


%define upstream_name ec2imgutils

Name:           python3-ec2imgutils
Version:        10.0.1
Release:        0
Summary:        Image management utilities for AWS EC2
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/SUSE-Enceladus/ec2imgutils
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python3
Requires:       python3-boto3 >= 1.22.11
Requires:       python3-dateutil
Requires:       python3-paramiko
BuildRequires:  python3-boto3 >= 1.22.11
BuildRequires:  python3-dateutil
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# Package renamed in SLE 12 do not remove Provides, Obsolete
# directives until after SLE 12 EOL
Provides:       python-ec2utilsbase = %{version}
Obsoletes:      python-ec2utilsbase < %{version}
Provides:       python-ec2deprecateimg = %{version}
Obsoletes:      python-ec2deprecateimg < %{version}
Provides:       python-ec2publishimg = %{version}
Obsoletes:      python-ec2publishimg < %{version}
Provides:       python-ec2uploadimg = %{version}
Obsoletes:      python-ec2uploadimg < %{version}

# Package rename in SLE 15 GA do not remove Provides, Obsolete
# directives until after SLE 15 SP3 EOL
Provides:       python3-ec2utilsbase = %{version}
Obsoletes:      python3-ec2utilsbase < %{version}
Provides:       python3-ec2deprecateimg = %{version}
Obsoletes:      python3-ec2deprecateimg < %{version}
Provides:       python3-ec2publishimg = %{version}
Obsoletes:      python3-ec2publishimg < %{version}
Provides:       python3-ec2uploadimg = %{version}
Obsoletes:      python3-ec2uploadimg < %{version}

%description
A collection of image manipulation utilities for AWS EC2. These include:
- ec2deprecateimg: Deprecates images by applying tags per convention
- ec2publishimg: Set image visibility
- ec2uploadimg: Upload an image to AWS EC2

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/* %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/*

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_mandir}/man*/*
%dir %{python3_sitelib}/ec2imgutils
%{python3_sitelib}/*
%{_bindir}/*

%changelog


