#
# spec file for package python-jira
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-jira
Version:        2.0.0
Release:        0
Summary:        Python library for interacting with JIRA via REST APIs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pycontribs/jira
Source:         https://files.pythonhosted.org/packages/source/j/jira/jira-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pbr >= 3.0.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml
Requires:       python-oauthlib
Requires:       python-pbr >= 3.0.0
Requires:       python-requests >= 2.10.0
Requires:       python-requests-oauthlib >= 0.6.1
Requires:       python-requests-toolbelt
Requires:       python-setuptools >= 20.10.1
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
This library eases the use of the JIRA REST API from Python.

%prep
%setup -q -n jira-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python3_only %{_bindir}/jirashell
%{python_sitelib}/*

%changelog
