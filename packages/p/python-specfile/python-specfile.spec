#
# spec file for package python-specfile
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


Name:           python-specfile
Version:        0.29.0
Release:        0
Summary:        A library for parsing and manipulating RPM spec files
License:        MIT
URL:            https://github.com/packit/specfile
Source:         https://files.pythonhosted.org/packages/source/s/specfile/specfile-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rpm
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rpm}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
A library for parsing and manipulating RPM spec files.

%prep
%autosetup -p1 -n specfile-%{version}
# we use our own package for "rpm" module (see Requires)
sed -i '/rpm-py-installer/d' setup.cfg

%build
%pyproject_wheel

%check
# Following tests fail:
# * test_update_tag
# * test_macros_reinit
%pytest -k "not (test_update_tag or test_macros_reinit or test_parse_texlive_spec)"

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/specfile
%{python_sitelib}/specfile-%{version}*-info

%changelog
