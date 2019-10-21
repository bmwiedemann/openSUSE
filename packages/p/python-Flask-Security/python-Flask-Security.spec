#
# spec file for package python-Flask-Security
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Flask-Security
Version:        3.0.0
Release:        0
Summary:        Security for Flask apps
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/mattupstate/flask-security
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Security/Flask-Security-%{version}.tar.gz
Patch0:         fix-requirements.patch
Patch2:         fix-tests.patch
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask >= 0.11}
BuildRequires:  %{python_module Flask-BabelEx >= 0.9.3}
BuildRequires:  %{python_module Flask-Login >= 0.3.0}
BuildRequires:  %{python_module Flask-Mail >= 0.7.3}
BuildRequires:  %{python_module Flask-Principal >= 0.3.3}
BuildRequires:  %{python_module Flask-SQLAlchemy >= 1.0}
BuildRequires:  %{python_module Flask-WTF >= 0.13.1}
BuildRequires:  %{python_module SQLAlchemy >= 0.8.0}
BuildRequires:  %{python_module bcrypt >= 1.0.2}
BuildRequires:  %{python_module check-manifest >= 0.25}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module flask-peewee >= 0.6.5}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module itsdangerous >= 0.21}
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module passlib >= 1.7}
BuildRequires:  %{python_module pydocstyle >= 1.0.0}
BuildRequires:  %{python_module pytest < 4}
BuildRequires:  %{python_module pytest-runner >= 2.6.2}
BuildRequires:  %{python_module pytest-translations >= 1.0.4}
# Don't require python modules just needed for testing that are not available in SLE
%if 0%{?is_opensuse}
%if 0%{suse_version} > 1500
%ifarch %x86_64 %power64 %s390x %ia64 %aarch64 %riscv64
BuildRequires:  %{python_module flask-mongoengine >= 0.7.0}
%endif
%endif
BuildRequires:  %{python_module mongoengine >= 0.10.0}
BuildRequires:  %{python_module pony >= 0.7.1}
%endif
# End of test requirements
BuildRequires:  fdupes
Requires:       python-Flask >= 0.11
Requires:       python-Flask-BabelEx >= 0.9.3
Requires:       python-Flask-Login >= 0.3.0
Requires:       python-Flask-Mail >= 0.7.3
Requires:       python-Flask-Principal >= 0.3.3
Requires:       python-Flask-WTF >= 0.13.1
Requires:       python-itsdangerous >= 0.21
Requires:       python-passlib >= 1.7
Suggests:       python-Flask-SQLAlchemy >= 1.0
Suggests:       python-bcrypt >= 1.0.2
Suggests:       python-sqlalchemy >= 0.8.0
BuildArch:      noarch

%python_subpackages

%description
Flask-Security is a Python module to add security features to a Flask
application.

%prep
%setup -q -n Flask-Security-%{version}
%patch0 -p1
%patch2 -p1
rm tests/test_cli.py
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_CTYPE=en_US@UTF-8
rm -Rf tests/__pycache__
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
