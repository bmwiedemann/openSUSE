#
# spec file for package python-jaraco.mongodb
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-jaraco.mongodb
Version:        12.4.0
Release:        0
Summary:        Routines and classes supporting MongoDB environments
License:        MIT
URL:            https://github.com/jaraco/jaraco.mongodb
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.mongodb/jaraco_mongodb-12.4.0.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cachetools}
BuildRequires:  %{python_module CherryPy}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module jaraco.collections >= 2}
BuildRequires:  %{python_module jaraco.context >= 2}
BuildRequires:  %{python_module jaraco.functools >= 2}
BuildRequires:  %{python_module jaraco.itertools >= 2}
BuildRequires:  %{python_module jaraco.logging >= 2}
BuildRequires:  %{python_module jaraco.services >= 2}
BuildRequires:  %{python_module jaraco.ui >= 2.4}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pymongo >= 3.5}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytimeparse}
BuildRequires:  %{python_module tempora}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cachetools
Requires:       python-dnspython
Requires:       python-jaraco.collections >= 2
Requires:       python-jaraco.context >= 2
Requires:       python-jaraco.functools >= 2
Requires:       python-jaraco.itertools >= 2
Requires:       python-jaraco.logging >= 2
Requires:       python-jaraco.services >= 2
Requires:       python-jaraco.ui >= 2.4
Requires:       python-more-itertools
Requires:       python-portend
Requires:       python-pymongo >= 3.5
Requires:       python-python-dateutil
Requires:       python-pytimeparse
Requires:       python-tempora
%if 0%{?python_version_nodots} <= 311
Requires:       python-backports.tarfile
%endif
Suggests:       python-sphinx >= 3.5
Suggests:       python-jaraco.packaging >= 9.3
Suggests:       python-rst.linker >= 1.9
Suggests:       python-furo
Suggests:       python-sphinx-lint
Suggests:       python-cherrypy
Suggests:       python-pytest-checkdocs >= 2.4
Suggests:       python-pytest-ruff >= 0.2.1
Suggests:       python-pytest-cov
Suggests:       python-pytest-enabler >= 2.2
Suggests:       python-pytest-mypy
Suggests:       python-types-python-dateutil
Suggests:       python-types-cachetools
BuildArch:      noarch
%python_subpackages

%description
Routines and classes supporting MongoDB environments

%prep
%autosetup -p1 -n jaraco_mongodb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
ignore="--ignore tests/test_compat.py --ignore tests/test_testing.py"
ignore+=" --ignore tests/test_service.pie --ignore tests/test_manage.py"
ignore+=" --ignore tests/test_insert_doc.py --ignore tests/test_fields.py"
donttest="test_session_persists or test_locked_session "
donttest+=" or sampling.estimate or upsert_and_fetch or build_parser "
donttest+=" or server_version or test_fixture"
%pytest $ignore -k "not ($donttest)"

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/mongodb
%{python_sitelib}/jaraco_mongodb-%{version}.dist-info

%changelog
