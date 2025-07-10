#
# spec file for package python-hatch-fancy-pypi-readme
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-hatch-fancy-pypi-readme%{psuffix}
Version:        25.1.0
Release:        0
Summary:        Fancy PyPI READMEs with Hatch
License:        MIT
URL:            https://github.com/hynek/hatch-fancy-pypi-readme
Source:         https://files.pythonhosted.org/packages/source/h/hatch_fancy_pypi_readme/hatch_fancy_pypi_readme-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
Requires:       alts
Provides:       python-hatch_fancy_pypi_readme = %{version}-%{release}
BuildArch:      noarch
%{?python_enable_dependency_generator}
%if %{with test}
# SECTION test
BuildRequires:  %{python_module hatch-fancy-pypi-readme >= %version}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
%python_subpackages

%description
hatch_fancy_pypi_readme is a Hatch metadata plugin for everyone who cares about
the first impression of their project's PyPI landing page. It allows you to
define your PyPI project description in terms of concatenated fragments that
are based on static strings, files, and most importantly: parts of files
defined using cut-off points or regular expressions.

Once you've assembled your readme, you can additionally run regular
expression-based substitutions over it. For instance to make relative links
absolute or to linkify users and issue numbers in your changelog.

Do you want your PyPI readme to be the project readme, but without badges,
followed by the license file, and the changelog section for only the last
release? You've come to the right place!

%prep
%setup -q -n hatch_fancy_pypi_readme-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/hatch-fancy-pypi-readme
%endif

%check
%if %{with test}
#test_end_to_end want's to have a hatchling wheel
%pytest --ignore tests/test_end_to_end.py
%endif

%pre
%python_libalternatives_reset_alternative hatch-fancy-pypi-readme

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/hatch-fancy-pypi-readme
%{python_sitelib}/hatch_fancy_pypi_readme
%{python_sitelib}/hatch_fancy_pypi_readme-%{version}*-info
%endif

%changelog
