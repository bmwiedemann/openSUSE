#
# spec file for package python-pbr
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pbr%{psuffix}
Version:        5.4.5
Release:        0
Summary:        Python Build Reasonableness
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://pypi.python.org/pypi/pbr
Source:         https://files.pythonhosted.org/packages/source/p/pbr/pbr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Recommends:     git-core
Recommends:     python-reno >= 2.5.0
Suggests:       python-nose
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-pbr-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module mock >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 2.0.2}
BuildRequires:  %{python_module reno >= 2.5.0}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module stestr >= 2.1.0}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testresources >= 2.0.0}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  %{python_module virtualenv >= 14.0.6}
BuildRequires:  %{python_module wheel >= 0.32.0}
BuildRequires:  git-core
BuildRequires:  gpg2
%endif
%python_subpackages

%description
PBR is a library to automatically do a bunch of standard
things you want in your setup.py without you having to repeat
them every time. It will set versions, process requirements
files and generate AUTHORS and ChangeLog file all from git
information.

%prep
%setup -q -n pbr-%{version}

sed -i '/coverage/d;/hacking/d' test-requirements.txt

%build
%python_build

%if %{with test}
%check
export OS_TEST_TIMEOUT=60
# test_requirement_parsing - syntax based on old virtualenv
%python_exec -m stestr run --black-regex 'test_requirement_parsing'
%endif

%if !%{with test}
%install
%python_install
%python_expand rm -r  %{buildroot}%{$python_sitelib}/pbr/tests
%python_clone -a %{buildroot}%{_bindir}/pbr

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pbr

%postun
%python_uninstall_alternative pbr

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog CONTRIBUTING.rst README.rst
%python_alternative %{_bindir}/pbr
%{python_sitelib}/pbr
%{python_sitelib}/pbr-%{version}-py%{python_version}.egg-info
%endif

%changelog
