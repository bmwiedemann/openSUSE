#
# spec file for package python3-img-proof
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


%bcond_without test
Name:           python3-img-proof
Version:        6.1.0
Release:        0
Summary:        Command line and API for testing custom images
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/SUSE-Enceladus/img-proof
Source:         https://files.pythonhosted.org/packages/source/i/img-proof/img-proof-%{version}.tar.gz
BuildRequires:  python3-PyYAML
BuildRequires:  python3-azure-common
BuildRequires:  python3-azure-mgmt-compute
BuildRequires:  python3-azure-mgmt-network
BuildRequires:  python3-azure-mgmt-resource
BuildRequires:  python3-boto3
BuildRequires:  python3-click
BuildRequires:  python3-click-man
BuildRequires:  python3-devel
BuildRequires:  python3-google-api-python-client
BuildRequires:  python3-google-auth
BuildRequires:  python3-oci-sdk
BuildRequires:  python3-paramiko
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-testinfra
%if %{with test}
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest-cov
%endif
Requires:       python3-PyYAML
Requires:       python3-azure-common
Requires:       python3-azure-mgmt-compute
Requires:       python3-azure-mgmt-network
Requires:       python3-azure-mgmt-resource
Requires:       python3-boto3
Requires:       python3-click
Requires:       python3-google-api-python-client
Requires:       python3-google-auth
Requires:       python3-oci-sdk
Requires:       python3-paramiko
Requires:       python3-pytest
Requires:       python3-testinfra
BuildArch:      noarch
Obsoletes:      python3-ipa < 6.1.0

%description
img-proof provides a command line utility to test images in
the Public Cloud (AWS, Azure, GCE, etc.).

%package tests
Summary:        Infrastructure tests for img-proof
Group:          Development/Languages/Python
Requires:       python3-susepubliccloudinfo
PreReq:         python3-img-proof = %{version}
Obsoletes:      python3-ipa-tests < 6.1.0

%description tests
Directory of infrastructure tests for testing images.

%prep
%setup -q -n img-proof-%{version}

%build
python3 setup.py build
mkdir -p man/man1
python3 setup.py --command-packages=click_man.commands man_pages --target man/man1

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/*.1 %{buildroot}/%{_mandir}/man1

install -d -m 755 %{buildroot}%{_prefix}
cp -r usr/* %{buildroot}%{_prefix}/

%check
%if %{with test}
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
python3 -m pytest --cov=img_proof --ignore=tests/data --ignore=usr
%endif

%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGES.md CONTRIBUTING.md README.md
%{_mandir}/man1/*
%{_bindir}/img-proof
%{python3_sitelib}/*

%files tests
%defattr(-,root,root)
%dir %{_datadir}/lib
%dir %{_datadir}/lib/img_proof
%{_datadir}/lib/img_proof/*

%changelog
