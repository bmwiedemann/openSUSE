#
# spec file for package python-pbr
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pbr%{psuffix}
Version:        6.1.1
Release:        0
Summary:        Python Build Reasonableness
License:        Apache-2.0
URL:            https://docs.openstack.org/pbr/latest/
Source:         https://files.pythonhosted.org/packages/source/p/pbr/pbr-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools >= 64.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     git-core
Obsoletes:      python-pbr-doc
BuildArch:      noarch
%if %{with test}
# Package originates from OpenStack and depends on other OpenStack packages for testing.
# These are only available for the primary python3 interpreter in TW, but optional.
# --> Only test in default python3 flavor.  gh#openSUSE/python-rpm-macros#66
# Python 2 packages on Leap are too outdated to test, either (stestr, subunit).
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module pbr = %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.12.0}
BuildRequires:  %{python_module testresources >= 2.0.0}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  %{python_module virtualenv >= 20.0.3}
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
%autosetup -p1 -n pbr-%{version}

sed -i '/coverage/d;/hacking/d' test-requirements.txt

%build
%pyproject_wheel

%if %{with test}
%check
export OS_TEST_TIMEOUT=60
exclude="parse_requirements|requirement_parsing|pep_517_support|"
exclude+="write_git_changelog|build_doc|cmd_builder_override|"
exclude+="extras_parsing|project_url_parsing|keywords_parsing|"
exclude+="test_handling_of_whitespace_in_data_files"
# Run tests with pytest to do not depend on python-stestr, that's no
# available on SLFO:Main
# stestr run -E "($exclude)"
%pytest -k "not (${exclude//|/ or })"
%endif

%if !%{with test}
%install
%pyproject_install
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
%{python_sitelib}/pbr-%{version}.dist-info
%endif

%changelog
