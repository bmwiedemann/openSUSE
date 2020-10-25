#
# spec file for package python-email_validator
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-email_validator
Version:        1.1.1
Release:        0
Summary:        A robust email syntax and deliverability validation library for Python
License:        CC0-1.0
Group:          Development/Languages/Python
URL:            https://github.com/JoshData/python-email-validator
Source:         https://github.com/JoshData/python-email-validator/archive/v%{version}.tar.gz
Patch0:         skip-tests-using-network.patch
Patch1:         fix-tests-strings.patch
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
%setup -q -n python-email-validator-%{version}
%patch0 -p1
%if %{?suse_version} <= 1500
%patch1 -p1
%endif

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/email_validator
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative email_validator

%postun
%python_uninstall_alternative email_validator

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/email_validator
%{python_sitelib}/*

%changelog
