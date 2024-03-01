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
Version:        10.0.3
Release:        0
Summary:        Image management utilities for AWS EC2
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/SUSE-Enceladus/ec2imgutils
Source0:        %{upstream_name}-%{version}.tar.bz2
%if 0%{?sle_version} >= 150400
Requires:       python311
Requires:       python311-boto3 >= 1.29.84
Requires:       python311-dateutil
Requires:       python311-paramiko >= 2.2.0
BuildRequires:  python311-boto3 >= 1.29.84
BuildRequires:  python311-dateutil
BuildRequires:  python311-pip
BuildRequires:  python311-setuptools
BuildRequires:  python311-wheel
%else
Requires:       python3
Requires:       python3-boto3 >= 1.29.84
Requires:       python3-dateutil
Requires:       python3-paramiko >= 2.2.0
BuildRequires:  python3-boto3 >= 1.29.84
BuildRequires:  python3-dateutil
BuildRequires:  python3-setuptools
%endif
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
%if 0%{?sle_version} >= 150400
find . -type f -name "ec2*" | xargs grep -l '/usr/bin/' | xargs sed -i 's/python3/python3.11/'
%endif

%build
%if 0%{?sle_version} >= 150400
%python311_pyproject_wheel
%else
python3 setup.py build
%endif

%install
%if 0%{?sle_version} >= 150400
%python311_pyproject_install
%else
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/* %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/*

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_mandir}/man*/*
%if 0%{?sle_version} >= 150400
%dir %{python311_sitelib}/ec2imgutils
%{python311_sitelib}/*
%else
%dir %{python3_sitelib}/ec2imgutils
%{python3_sitelib}/*
%endif
%{_bindir}/*

%changelog
