#
# spec file for package python-django-otp
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


Name:           python-django-otp
Version:        1.5.2
Release:        0
Summary:        Add two-factor authentication to Django using one-time passwords
License:        Unlicense
URL:            https://github.com/django-otp/django-otp
Source:         https://files.pythonhosted.org/packages/source/d/django-otp/django_otp-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
Suggests:       python-segno
Suggests:       python-qrcode
BuildArch:      noarch
%python_subpackages

%description
This project makes it easy to add support for `one-time passwords
<http://en.wikipedia.org/wiki/One-time_password>`_ (OTPs) to Django. It can be
integrated at various levels, depending on how much customization is required.
It integrates with ``django.contrib.auth``, although it is not a Django
authentication backend. The primary target is developers wishing to incorporate
OTPs into their Django projects as a form of `two-factor authentication
<http://en.wikipedia.org/wiki/Two-factor_authentication>`_.

Several simple OTP plugins are included and more are available separately. This
package also includes an implementation of OATH `HOTP
<http://tools.ietf.org/html/rfc4226>`_ and `TOTP
<http://tools.ietf.org/html/rfc6238>`_ for convenience, as these are standard
OTP algorithms used by multiple plugins.

If you're looking for a higher-level or more opinionated solution, you might be
interested in `django-two-factor-auth
<https://github.com/Bouke/django-two-factor-auth>`_.

%prep
%autosetup -p1 -n django_otp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no unit tests, just a test project which I didn't manage to launch

%files %{python_files}
%{python_sitelib}/django_otp
%{python_sitelib}/django_otp-%{version}.dist-info

%changelog
