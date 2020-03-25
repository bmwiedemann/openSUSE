#
# spec file for package python-Flask-Security-Too
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Security-Too
Version:        3.3.3
Release:        0
License:        MIT
Summary:        Security for Flask apps
Url:            https://github.com/jwag956/flask-security
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Security-Too/Flask-Security-Too-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module pytest-runner >= 2.6.2}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Flask >= 1.0.2
Requires:       python-Flask-BabelEx >= 0.9.3
Requires:       python-Flask-Login >= 0.4.1
Requires:       python-Flask-Mail >= 0.9.1
Requires:       python-Flask-Principal >= 0.4.0
Requires:       python-Flask-WTF >= 0.14.2
Requires:       python-itsdangerous >= 1.1.0
Requires:       python-passlib >= 1.7.1
Requires:       python-Werkzeug >= 0.15.5
Requires:       python-speaklater
Suggests:       python-Flask-SQLAlchemy >= 2.3
Suggests:       python-bcrypt >= 3.1.5
Suggests:       python-SQLAlchemy >= 1.2.6
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests were disabled, just like in python-Flask-Security

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flask_security
%{python_sitelib}/Flask_Security_Too-%{version}-py%{python_version}.egg-info

%changelog
