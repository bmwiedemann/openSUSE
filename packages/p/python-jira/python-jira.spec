#
# spec file for package python-jira
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-jira
Version:        3.5.2
Release:        0
Summary:        Python library for interacting with JIRA via REST APIs
License:        BSD-3-Clause
URL:            https://github.com/pycontribs/jira
Source:         https://files.pythonhosted.org/packages/source/j/jira/jira-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pbr >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml
Requires:       python-keyring
Requires:       python-oauthlib
Requires:       python-packaging
Requires:       python-requests >= 2.10.0
Requires:       python-requests-oauthlib >= 0.6.1
Requires:       python-requests-toolbelt
Requires:       python-typing_extensions >= 3.7.4.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This library eases the use of the JIRA REST API from Python.

%prep
%setup -q -n jira-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jirashell
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Right, no test suite running, because the package tests against the
# real instance of Jira. gh#pycontribs/jira#1262

%post
%python_install_alternative jirashell

%postun
%python_uninstall_alternative jirashell

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/jirashell
%{python_sitelib}/jira
%{python_sitelib}/jira-%{version}*info

%changelog
