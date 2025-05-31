#
# spec file for package python-ec2imgutils
#
# Copyright (c) 2025 SUSE LLC
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

%define upstream_name ec2imgutils
Name:           python-ec2imgutils
Version:        10.0.4
Release:        0
Summary:        Image management utilities for AWS EC2
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/ec2imgutils
Source0:        %{upstream_name}-%{version}.tar.bz2
BuildRequires:  %{pythons}-boto3 >= 1.29.84
BuildRequires:  %{pythons}-dateutil
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-boto3 >= 1.29.84
Requires:       %{pythons}-dateutil
Requires:       %{pythons}-paramiko >= 2.2.0
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch

%if "%{python_provides}" == "python3" || (0%{?sle_version} > 150400 && 0%{?sle_version} < 160000)
# Package renamed in SLE 12 do not remove Provides, Obsolete
# directives until after SLE 12 EOL. This is for migration to SLE 15
Provides:       python-ec2utilsbase:/usr/lib/python2.7/site-packages/ec2utils
Obsoletes:      python-ec2utilsbase < %{version}
Provides:       python-ec2deprecateimg:%{_bindir}/ec2deprecateimg
Obsoletes:      python-ec2deprecateimg < %{version}
Provides:       python-ec2publishimg:%{_bindir}/ec2publishimg
Obsoletes:      python-ec2publishimg < %{version}
Provides:       python-ec2uploadimg:%{_bindir}/ec2uploadimg
Obsoletes:      python-ec2uploadimg < %{version}

# Package rename in SLE 15 GA do not remove Provides, Obsolete
# directives until after SLE 15 SP3 EOL
Provides:       python3-ec2utilsbase = %{version}
Obsoletes:      python3-ec2utilsbase < %{version}
Provides:       python3-ec2deprecateimg:%{_bindir}/ec2deprecateimg
Obsoletes:      python3-ec2deprecateimg < %{version}
Provides:       python3-ec2publishimg:%{_bindir}/ec2publishimg
Obsoletes:      python3-ec2publishimg < %{version}
Provides:       python3-ec2uploadimg:%{_bindir}/ec2uploadimg
Obsoletes:      python3-ec2uploadimg < %{version}

# Package rename in SLE 15 SP4 to comply with new naming convention
Obsoletes:      python3-ec2imgutils < %{version}
%endif

# For Factory
Obsoletes:      python310-ec2imgutils < %{version}
Obsoletes:      python311-ec2imgutils < %{version}
Obsoletes:      python312-ec2imgutils < %{version}
Obsoletes:      python313-ec2imgutils < %{version}

%description
A collection of image manipulation utilities for AWS EC2. These include:
- ec2deprecateimg: Deprecates images by applying tags per convention
- ec2publishimg: Set image visibility
- ec2uploadimg: Upload an image to AWS EC2

%prep
%autosetup -n %{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/* %{buildroot}/%{_mandir}/man1
%fdupes %{buildroot}%{_sitelibdir}

%files
%doc README.md
%license LICENSE
%{_bindir}/ec2deprecateimg
%{_bindir}/ec2listimg
%{_bindir}/ec2publishimg
%{_bindir}/ec2removeimg
%{_bindir}/ec2uploadimg
%{_mandir}/man1/ec2deprecateimg.1%{?ext_man}
%{_mandir}/man1/ec2listimg.1%{?ext_man}
%{_mandir}/man1/ec2publishimg.1%{?ext_man}
%{_mandir}/man1/ec2removeimg.1%{?ext_man}
%{_mandir}/man1/ec2uploadimg.1%{?ext_man}

%{_sitelibdir}/ec2imgutils/
%{_sitelibdir}/ec2imgutils-*.dist-info/

%changelog
