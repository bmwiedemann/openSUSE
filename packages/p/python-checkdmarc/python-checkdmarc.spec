#
# spec file for package python-checkdmarc
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           python-checkdmarc
Version:        5.7.8
Release:        0
Summary:        A Python module and command line parser for SPF and DMARC records
License:        Apache-2.0
URL:            https://domainaware.github.io/checkdmarc
Source:         https://github.com/domainaware/checkdmarc/archive/refs/tags/%{version}.tar.gz#/checkdmarc-%{version}.tar.gz
Patch0:         skip-network-tests.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-dnspython >= 2.0.0
Requires:       python-expiringdict >= 1.1.4
Requires:       python-pem >= 23.1.0
Requires:       python-publicsuffixlist
Requires:       python-pyOpenSSL >= 24.2.1
Requires:       python-pyleri >= 1.3.2
Requires:       python-requests >= 2.25.0
Requires:       python-timeout-decorator >= 0.4.1
Requires:       python-xmltodict
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dnspython >= 2.0.0}
BuildRequires:  %{python_module expiringdict >= 1.1.4}
BuildRequires:  %{python_module pem >= 23.1.0}
BuildRequires:  %{python_module publicsuffixlist}
BuildRequires:  %{python_module pyOpenSSL >= 24.2.1}
BuildRequires:  %{python_module pyleri >= 1.3.2}
BuildRequires:  %{python_module requests >= 2.25.0}
BuildRequires:  %{python_module timeout-decorator >= 0.4.1}
BuildRequires:  %{python_module xmltodict}
# /SECTION
%python_subpackages

%description
A Python module and command line parser for SPF and DMARC records.

%prep
%setup -q -n checkdmarc-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/checkdmarc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative checkdmarc

%postun
%python_uninstall_alternative checkdmarc

%check
%pyunittest -v tests.py

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/checkdmarc
%{python_sitelib}/checkdmarc
%{python_sitelib}/checkdmarc-*.dist-info

%changelog
