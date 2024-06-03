#
# spec file for package python-Flask-Security-Too
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
Name:           python-Flask-Security-Too
Version:        5.4.3
Release:        0
Summary:        Security for Flask apps
License:        MIT
URL:            https://github.com/Flask-Middleware/flask-security
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Security-Too/Flask-Security-Too-%{version}.tar.gz
Patch0:         no-mongodb.patch
# PATCH-FIX-OPENSUSE Use pyqrcodeng, we do not ship qrcode in OpenSUSE.
Patch1:         use-pyqrcodeng.patch
BuildRequires:  %{python_module Authlib}
BuildRequires:  %{python_module Babel >= 2.10.0}
BuildRequires:  %{python_module Flask >= 2.3.2}
BuildRequires:  %{python_module Flask-Babel >= 3.1.0}
BuildRequires:  %{python_module Flask-Login >= 0.6.2}
BuildRequires:  %{python_module Flask-Mailman >= 0.3.0}
BuildRequires:  %{python_module Flask-Principal >= 0.4.0}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 3.0.3}
BuildRequires:  %{python_module Flask-WTF >= 1.1.2}
BuildRequires:  %{python_module MarkupSafe >= 2.1.0}
BuildRequires:  %{python_module PyQRCode >= 1.2}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WTForms-lang}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module Werkzeug >= 2.3.3}
BuildRequires:  %{python_module argon2_cffi >= 21.3.0}
BuildRequires:  %{python_module bcrypt >= 4.0.1}
BuildRequires:  %{python_module bleach >= 6.0.0}
BuildRequires:  %{python_module cachetools >= 3.1.0}
BuildRequires:  %{python_module cryptography >= 40.0.2}
BuildRequires:  %{python_module email-validator >= 2.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module importlib_resources >= 5.10.0}
BuildRequires:  %{python_module itsdangerous >= 1.1.0}
BuildRequires:  %{python_module passlib >= 1.7.4}
BuildRequires:  %{python_module peewee >= 3.16.2}
BuildRequires:  %{python_module phonenumbers}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pony if %python-base < 3.11}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module webauthn >= 2.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zxcvbn >= 4.4.28}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 2.3.2
Requires:       python-Flask-Babel >= 3.1.0
Requires:       python-Flask-Login >= 0.6.2
Requires:       python-Flask-Principal >= 0.4.0
Requires:       python-Flask-WTF >= 1.1.2
Requires:       python-MarkupSafe >= 2.1.0
Requires:       python-WTForms >= 3.0.0
Requires:       python-Werkzeug >= 2.3.3
Requires:       python-bcrypt >= 4.0.1
Requires:       python-bleach >= 6.0.0
Requires:       python-cryptography >= 40.0.2
Requires:       python-email-validator >= 2.0
Requires:       python-importlib_resources >= 5.10.0
Requires:       python-itsdangerous >= 1.1.0
Requires:       python-passlib >= 1.7.4
Requires:       python-webauthn >= 2.0.0
Recommends:     python-PyQRCode >= 1.2
Recommends:     python-SQLAlchemy
Recommends:     python-zxcvbn >= 4.4.28
Suggests:       python-argon2_cffi >= 21.3.0
Suggests:       python-phonenumbers
Conflicts:      python-Flask-Security < 3.2.0
Obsoletes:      python-Flask-Security < 3.2.0
Provides:       python-Flask-Security = %{version}
BuildArch:      noarch
%python_subpackages

%description
Flask-Security-Too is a Python module to add security features to a Flask
application. This is a independently maintained version of Flask-Security
based on the 3.0.0 version of the original.

%prep
%autosetup -p1 -n Flask-Security-Too-%{version}

%if 0%{?suse_version} <= 1500
# test_trackable.py needs werkzeug.middleware.proxy_fix which is only available
# in newer werkzeug versions
rm tests/test_trackable.py
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_login_email_whatever'

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flask_security
%{python_sitelib}/Flask_Security_Too-%{version}.dist-info

%changelog
