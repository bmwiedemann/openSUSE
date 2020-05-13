#
# spec file for package python-Flask-Security-Too
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Security-Too
Version:        3.4.2
Release:        0
Summary:        Security for Flask apps
License:        MIT
URL:            https://github.com/jwag956/flask-security
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Security-Too/Flask-Security-Too-%{version}.tar.gz
Patch0:         no-mongodb.patch
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module Flask >= 1.0.2}
BuildRequires:  %{python_module Flask-BabelEx >= 0.9.3}
BuildRequires:  %{python_module Flask-Login >= 0.4.1}
BuildRequires:  %{python_module Flask-Mail >= 0.9.1}
BuildRequires:  %{python_module Flask-Principal >= 0.4.0}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 2.3}
BuildRequires:  %{python_module Flask-WTF >= 0.14.2}
BuildRequires:  %{python_module PyQRCode >= 1.2}
BuildRequires:  %{python_module SQLAlchemy >= 1.2.6}
BuildRequires:  %{python_module Werkzeug >= 0.15.5}
BuildRequires:  %{python_module argon2_cffi >= 19.1.0}
BuildRequires:  %{python_module bcrypt >= 3.1.5}
BuildRequires:  %{python_module cachetools >= 3.1.0}
BuildRequires:  %{python_module email_validator >= 1.0.5}
BuildRequires:  %{python_module itsdangerous >= 1.1.0}
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module passlib >= 1.7.1}
BuildRequires:  %{python_module peewee >= 3.11.2}
BuildRequires:  %{python_module phonenumbers >= 8.11.1}
BuildRequires:  %{python_module pony >= 0.7.11}
BuildRequires:  %{python_module pytest-runner >= 2.6.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zxcvbn >= 4.4.28}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0.2
Requires:       python-Flask-BabelEx >= 0.9.3
Requires:       python-Flask-Login >= 0.4.1
Requires:       python-Flask-Mail >= 0.9.1
Requires:       python-Flask-Principal >= 0.4.0
Requires:       python-Flask-WTF >= 0.14.2
Requires:       python-Werkzeug >= 0.15.5
Requires:       python-bcrypt >= 3.1.5
Requires:       python-email_validator >= 1.0.5
Requires:       python-itsdangerous >= 1.1.0
Requires:       python-passlib >= 1.7.1
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
%setup -q -n Flask-Security-Too-%{version}
%patch0 -p1
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flask_security
%{python_sitelib}/Flask_Security_Too-%{version}-py%{python_version}.egg-info

%changelog
