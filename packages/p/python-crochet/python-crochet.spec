#
# spec file for package python-crochet
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
Name:           python-crochet
Version:        1.12.0
Release:        0
Summary:        Use Twisted from any applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/itamarst/crochet
Source:         https://files.pythonhosted.org/packages/source/c/crochet/crochet-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 16.0
Requires:       python-wrapt
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted >= 16.0}
BuildRequires:  %{python_module wrapt}
# /SECTION
%python_subpackages

%description
Crochet is an MIT-licensed library that makes it easier for blocking or
threaded applications like Flask or Django to use the Twisted networking
framework.

%prep
%setup -q -n crochet-%{version}
# Two tests fail on i586 only https://github.com/itamarst/crochet/issues/125
# Disable only these two globally
sed -Ei 's/(test_control_c_is_possible|test_reactor_stop_unblocks)/_\1/' crochet/tests/test_api.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
