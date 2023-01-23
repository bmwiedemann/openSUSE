#
# spec file
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
Version:        5.11.1
Release:        0
Summary:        Python Build Reasonableness
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/pbr/latest/
Source:         https://files.pythonhosted.org/packages/source/p/pbr/pbr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Recommends:     git-core
Suggests:       python-nose
Requires(post): update-alternatives
Requires(postun):update-alternatives
Obsoletes:      python-pbr-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  git-core
BuildRequires:  gpg2
# Package originates from OpenStack and depends on other OpenStack packages for testing.
# These are only available for the primary python3 interpreter in TW, but optional.
# --> Only test in default python3 flavor.  gh#openSUSE/python-rpm-macros#66
# Python 2 packages on Leap are too outdated to test, either (stestr, subunit).
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-pep517
BuildRequires:  python3-pip
BuildRequires:  python3-six >= 1.12.0
BuildRequires:  python3-stestr >= 2.1.0
BuildRequires:  python3-testresources >= 2.0.0
BuildRequires:  python3-testscenarios >= 0.4
BuildRequires:  python3-testtools >= 2.2.0
BuildRequires:  python3-virtualenv >= 20.0.3
BuildRequires:  python3-wheel >= 0.32.0
%endif
%python_subpackages

%description
PBR is a library to automatically do a bunch of standard
things you want in your setup.py without you having to repeat
them every time. It will set versions, process requirements
files and generate AUTHORS and ChangeLog file all from git
information.

%prep
%autosetup -p1 -n pbr-%{version}

sed -i '/coverage/d;/hacking/d' test-requirements.txt

%build
%python_build

%if %{with test}
%check
export OS_TEST_TIMEOUT=60
python3 -m stestr run --suppress-attachments --exclude-regex '(pbr.tests.test_packaging.TestPEP517Support|pbr.tests.test_packaging.TestRequirementParsing.test_requirement_parsing)'
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
