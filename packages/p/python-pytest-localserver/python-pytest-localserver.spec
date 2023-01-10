#
# spec file for package python-pytest-localserver
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%bcond_with extras
Name:           python-pytest-localserver
Version:        0.7.0
Release:        0
Summary:        Plugin for py.test to test server connections locally
License:        MIT
URL:            https://github.com/pytest-dev/pytest-localserver
Source:         https://files.pythonhosted.org/packages/source/p/pytest-localserver/pytest-localserver-%{version}.tar.gz
BuildRequires:  %{python_module Werkzeug >= 0.10}
%if %{with extras}
BuildRequires:  %{python_module aiosmtpd}
%endif
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 2.0.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
%if 0%{?suse_version} <= 1500
# old setuptools_scm[toml] needs explicit extra
BuildRequires:  %{python_module toml}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Werkzeug >= 0.10
Requires:       python-pytest >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
The pytest-localserver package is a plugin for the `pytest`_ testing framework
which enables you to test server connections locally.

Sometimes `monkeypatching`_ ``urllib2.urlopen()`` just does not cut it, for
instance if you work with ``urllib2.Request``, define your own openers/handlers
or work with ``httplib``. In these cases it may come in handy to have an HTTP
server running locally which behaves just like the real thing. Well, look
no further!

%prep
%setup -q -n pytest-localserver-%{version}
%autopatch -p1
sed -i "1d" pytest_localserver/{plugin,smtp}.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_localserver
%{python_sitelib}/pytest_localserver-%{version}*-info

%changelog
