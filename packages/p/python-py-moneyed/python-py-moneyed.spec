#
# spec file for package python-py-moneyed
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-py-moneyed
Version:        3.0
Release:        0
Summary:        Python currency and money classes
License:        BSD-3-Clause
URL:            https://github.com/limist/py-moneyed
Source:         https://github.com/py-moneyed/py-moneyed/archive/refs/tags/v%{version}.tar.gz#/py-moneyed-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 2.8.0
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mypy >= 0.812}
BuildRequires:  %{python_module Babel >= 2.8.0}
BuildRequires:  %{python_module pytest >= 2.3.0}
BuildRequires:  %{python_module pytest >= 2.3.0}
BuildRequires:  %{python_module tox >= 1.6.0}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3}
# /SECTION
%python_subpackages

%description
Provides Currency and Money classes for use in your Python code.

%prep
%autosetup -p1 -n py-moneyed-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/moneyed
%{python_sitelib}/py_moneyed-%{version}*-info

%changelog
