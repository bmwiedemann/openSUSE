#
# spec file for package python-ara
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
# plugin for Ansible package
%define pythons python3
%bcond_without libalternatives
Name:           python-ara
Version:        1.7.4
Release:        0
Summary:        ARA Records Ansible
License:        GPL-3.0-or-later
# Old project URL: https://github.com/ansible-community/ara
# Project moved from github to codeberg gh#ansible-community/ara#603
URL:            https://codeberg.org/ansible-community/ara
Source:         https://files.pythonhosted.org/packages/source/a/ara/ara-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-cliff
Requires:       python-pbr
Requires:       python-requests >= 2.14.2
Recommends:     python-Django >= 3.2
Recommends:     python-django-cors-headers
Recommends:     python-django-filter
Recommends:     python-djangorestframework >= 3.9.1
Recommends:     python-dynaconf
Recommends:     python-whitenoise
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module ara >= %{version}}
BuildRequires:  %{python_module django-cors-headers}
BuildRequires:  %{python_module django-filter}
BuildRequires:  %{python_module django-health-check}
BuildRequires:  %{python_module djangorestframework >= 3.9.1}
BuildRequires:  %{python_module dynaconf}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  %{python_module whitenoise}
%endif
%python_subpackages

%description
ARA saves playbook results to a local or remote database by using an
Ansible callback plugin and provides an API to integrate this data in
tools and interfaces.

%prep
%setup -q -n ara-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ara
%python_clone -a %{buildroot}%{_bindir}/ara-manage
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
ara-manage test -v 2 ara
%endif

%if !%{with test}
%pre
%python_libalternatives_reset_alternative ara
%python_libalternatives_reset_alternative ara-manage

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/ara
%python_alternative %{_bindir}/ara-manage
%{python_sitelib}/ara-%{version}.dist-info
%{python_sitelib}/ara
%endif

%changelog
