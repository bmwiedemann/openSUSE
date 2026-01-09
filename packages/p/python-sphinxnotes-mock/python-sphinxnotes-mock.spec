#
# spec file for package python-sphinxnotes-mock
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         skip_python311 1
%define         _modname sphinxnotes_mock
Name:           python-sphinxnotes-mock
Version:        1.1
Release:        0
Summary:        Sphinx extension for masking unsupported directives and roles
License:        BSD-3-Clause
URL:            https://github.com/sphinx-notes/mock
Source:         https://files.pythonhosted.org/packages/source/s/sphinxnotes-mock/sphinxnotes_mock-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 7.0}
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 46.1.0}
BuildRequires:  %{python_module setuptools_scm >= 5}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension for masking unsupported directives and roles.

%prep
%autosetup -p1 -n %{_modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/sphinxnotes
%{python_sitelib}/%{_modname}-%{version}.dist-info

%changelog
