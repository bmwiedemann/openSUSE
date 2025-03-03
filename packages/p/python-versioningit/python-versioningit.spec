#
# spec file for package python-versioningit
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-versioningit
Version:        3.1.2
Release:        0
Summary:        Versioning It with your Version In Git
License:        MIT
URL:            https://github.com/jwodder/versioningit
Source:         https://files.pythonhosted.org/packages/source/v/versioningit/versioningit-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.10}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli >= 1.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
Requires:       python-tomli >= 1.2
%if %{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 3.6
%endif
Suggests:       python-dataclasses
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
Python Setuptools plugin for automatically determining your package's version
based on your version control repository's tags. Unlike others, it allows easy
customization of the version format and even lets you easily override the
separate functions used for version extraction & calculation.

%prep
%setup -q -n versioningit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/versioningit

%check
%pytest test -k 'not test_editable_mode or not test_end2end'

%pre
%python_libalternatives_reset_alternative versioningit

%post
%python_install_alternative versioningit

%postun
%python_uninstall_alternative versioningit

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python_alternative %{_bindir}/versioningit
%{python_sitelib}/versioningit
%{python_sitelib}/versioningit-%{version}*-info

%changelog
