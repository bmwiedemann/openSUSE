#
# spec file for package aws-cli
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


Name:           aws-cli
Version:        1.16.223
Release:        0
Summary:        Amazon Web Services Command Line Interface
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/aws/aws-cli
Source0:        %{name}-%{version}.tar.gz
Patch0:         hide_py_pckgmgmt.patch
Requires:       groff
BuildRequires:  fdupes
%if 0%{?suse_version} && 0%{?suse_version} > 1315
Requires:       python3
Requires:       python3-PyYAML     <= 6.0.0
Requires:       python3-PyYAML     >= 3.10
Requires:       python3-botocore  >= 1.12.213
Requires:       python3-colorama  <= 0.4.1
Requires:       python3-colorama  >= 0.2.5
Requires:       python3-docutils  >= 0.10
Requires:       python3-rsa       <  5.0.0
Requires:       python3-rsa       >= 3.1.2
Requires:       python3-s3transfer < 0.3.0
Requires:       python3-s3transfer >= 0.2.0
Requires:       python3-six
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%else
Requires:       python
Requires:       python-PyYAML     <= 3.13
Requires:       python-PyYAML     >= 3.10
Requires:       python-botocore  >= 1.12.93
Requires:       python-colorama  <= 0.3.9
Requires:       python-colorama  >= 0.2.5
Requires:       python-docutils  >= 0.10
Requires:       python-rsa       <= 3.5.0
Requires:       python-rsa       >= 3.1.2
Requires:       python-s3transfer < 0.3.0
Requires:       python-s3transfer >= 0.2.0
Requires:       python-six
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%endif
BuildArch:      noarch

%description
The AWS Command Line Interface (CLI) is a unified tool to manage AWS
services. With this tool, multiple AWS services can be controlled
from the command line and automated through scripts.

%prep
%setup -q
%patch0
sed -i 's/from botocore\.vendored //' awscli/customizations/awslambda.py
sed -i 's/botocore\.vendored\.//' awscli/customizations/configure/__init__.py

%build
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py build
%else
python setup.py build
%endif

%install
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-scripts=%{_bindir}
%fdupes %{buildroot}%{python3_sitelib}
find %{buildroot}%{python3_sitelib}/awscli/examples -type f -exec chmod 644 {} \;
%else
python setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-scripts=%{_bindir}
%fdupes %{buildroot}%{python_sitelib}
find %{buildroot}%{python_sitelib}/awscli/examples -type f -exec chmod 644 {} \;
%endif
# No DOS crap
rm %{buildroot}/%{_bindir}/aws.cmd

%files
%defattr(-,root,root,-)
%doc CHANGELOG.rst README.rst
%license LICENSE.txt 
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%dir %{python3_sitelib}/awscli
%dir %{python3_sitelib}/awscli-%{version}-py%{py3_ver}.egg-info
%{python3_sitelib}/awscli/*
%{python3_sitelib}/*egg-info/*
%else
%dir %{python_sitelib}/awscli
%dir %{python_sitelib}/awscli-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/awscli/*
%{python_sitelib}/*egg-info/*
%endif
%{_bindir}/*

%changelog
