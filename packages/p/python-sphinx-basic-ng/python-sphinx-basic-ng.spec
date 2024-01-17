#
# spec file for package python-sphinx-basic-ng
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


Name:           python-sphinx-basic-ng
Version:        1.0.0.beta2
Release:        0
Summary:        A modern skeleton for Sphinx themes
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-basic-ng
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-basic-ng/sphinx_basic_ng-1.0.0b2.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 4.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 4.0
BuildArch:      noarch
%python_subpackages

%description
A modern skeleton for Sphinx themes.

%prep
%autosetup -p1 -n sphinx_basic_ng-1.0.0b2

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/sphinx_basic_ng
%{python_sitelib}/sphinx_basic_ng-*.dist-info

%changelog
