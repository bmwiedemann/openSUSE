#
# spec file for package python-django-otp-webauthn
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


Name:           python-django-otp-webauthn
Version:        0.4.0
Release:        0
Summary:        FIDO2 WebAuthn support for django-otp
License:        BSD-3-Clause
URL:            None
Source:         https://files.pythonhosted.org/packages/source/d/django-otp-webauthn/django_otp_webauthn-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  fdupes
Requires:       python-Django >= 4.2
Requires:       python-django-otp >= 1.4
Requires:       python-djangorestframework >= 3.14
Requires:       python-webauthn >= 2.1.0
BuildArch:      noarch
%python_subpackages

%description
This package provides an implementation of [WebAuthn Passkeys](https://passkeys.dev/) for Django.
It is written as a plugin for the [Django OTP framework](https://github.com/django-otp/django-otp) 
for multi-factor authentication. Under the hood, this package uses [py_webauth](https://github.com/duo-labs/py_webauthn/) 
to handle all cryptographic operations.

%prep
%autosetup -p1 -n django_otp_webauthn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no unit tests to run, just some sandbox

%files %{python_files}
%{python_sitelib}/django_otp_webauthn
%{python_sitelib}/django_otp_webauthn-%{version}.dist-info

%changelog
