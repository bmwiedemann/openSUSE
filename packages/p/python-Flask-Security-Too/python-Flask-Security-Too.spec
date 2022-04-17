#
# spec file for package python-Flask-Security-Too
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Security-Too
Version:        4.1.3
Release:        0
Summary:        Security for Flask apps
License:        MIT
URL:            https://github.com/jwag956/flask-security
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Security-Too/Flask-Security-Too-%{version}.tar.gz
Patch0:         no-mongodb.patch
Patch1:         use-pyqrcodeng.patch
# PATCH-FIX-UPSTREAM endswith-assert.patch gh#Flask-Middleware/flask-security#605 mcepl@suse.com
# don't test for euqality of response.headers['Location'], just for .endswith
Patch2:         endswith-assert.patch
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module Flask >= 1.1.1}
BuildRequires:  %{python_module Flask-Babel}
BuildRequires:  %{python_module Flask-Login >= 0.4.1}
BuildRequires:  %{python_module Flask-Mail >= 0.9.1}
BuildRequires:  %{python_module Flask-Principal >= 0.4.0}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 2.3}
BuildRequires:  %{python_module Flask-WTF >= 0.14.3}
BuildRequires:  %{python_module PyQRCode >= 1.2}
BuildRequires:  %{python_module SQLAlchemy >= 1.2.6}
BuildRequires:  %{python_module WTForms-lang}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module Werkzeug >= 0.14.1}
BuildRequires:  %{python_module argon2_cffi >= 19.1.0}
BuildRequires:  %{python_module bcrypt >= 3.1.4}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module blinker >= 1.4}
BuildRequires:  %{python_module cachetools >= 3.1.0}
BuildRequires:  %{python_module cryptography >= 2.1.4}
BuildRequires:  %{python_module email_validator >= 1.1.1}
BuildRequires:  %{python_module itsdangerous >= 1.1.0}
BuildRequires:  %{python_module passlib >= 1.7.2}
BuildRequires:  %{python_module peewee >= 3.7.1}
BuildRequires:  %{python_module phonenumbers >= 8.11.1}
BuildRequires:  %{python_module pony}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zxcvbn >= 4.4.28}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.1.1
Requires:       python-Flask-Babel
Requires:       python-Flask-Login >= 0.4.1
Requires:       python-Flask-Principal >= 0.4.0
Requires:       python-Flask-WTF >= 0.14.3
Requires:       python-Werkzeug >= 0.14.1
Requires:       python-bcrypt >= 3.1.4
Requires:       python-blinker >= 1.4
Requires:       python-cryptography >= 2.1.4
Requires:       python-email_validator >= 1.1.1
Requires:       python-itsdangerous >= 1.1.0
Requires:       python-passlib >= 1.7.2
Recommends:     python-PyQRCode >= 1.2
Recommends:     python-SQLAlchemy >= 1.2.6
Recommends:     python-zxcvbn >= 4.4.28
Suggests:       python-argon2_cffi >= 19.1.0
Suggests:       python-phonenumbers >= 8.11.1
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#Flask-Middleware/flask-security#605 for test_two_factor_flag
%pytest -k 'not test_two_factor_flag'

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flask_security
%{python_sitelib}/Flask_Security_Too-%{version}-py%{python_version}.egg-info

%changelog
