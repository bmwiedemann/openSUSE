#
# spec file for package python-email-validator
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-email-validator
Version:        2.1.1
Release:        0
Summary:        A robust email syntax and deliverability validation library for Python
License:        CC0-1.0
URL:            https://github.com/JoshData/python-email-validator
Source:         https://github.com/JoshData/python-email-validator/archive/refs/tags/v%{version}.tar.gz#/email_validator-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Ignore DeprecationWarning until requests-toolbelt is fixed
# (Pulled in by dnspython)
Patch0:         ignore-urllib3-pyopenssl-warning.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module idna >= 2.0.0}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython >= 1.15.0
Requires:       python-idna >= 2.0.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-email_validator = %{version}-%{release}
Obsoletes:      python-email_validator < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
A robust email address syntax and deliverability validation library
for Python 2.7/3.4 by Joshua Tauberer.

This library validates that address are of the form ``x@y.com``. This is
the sort of validation you would want for a login form on a website.

Key features:

* Good for validating email addresses used for logins/identity.
* Friendly error messages when validation fails (appropriate to show to end users).
* (optionally) Checks deliverability: Does the domain name resolve?
* Supports internationalized domain names and (optionally) internationalized local parts.
* Normalizes email addresses (super important for internationalized addresses! see below).

%prep
%autosetup -p1 -n python-email-validator-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/email_validator
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
echo "nameserver 1.1.1.1" > resolv.conf
export RESOLV_FILE=$PWD/resolv.conf
# test_caching_dns_resolver fails when running with kvm
donttest="test_caching_dns_resolver"
%pytest tests -k "not ($donttest)"

%post
%python_install_alternative email_validator

%postun
%python_uninstall_alternative email_validator

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/email_validator
%{python_sitelib}/email_validator
%{python_sitelib}/email_validator-%{version}*-info

%changelog
