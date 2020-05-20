#
# spec file for package python-tap.py
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
%define skip_python2 1
Name:           python-tap.py
Version:        3.0
Release:        0
Summary:        Test Anything Protocol (TAP) tools
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-tap/tappy
Source:         https://files.pythonhosted.org/packages/source/t/tap.py/tap.py-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-PyYAML
Recommends:     python-more-itertools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Test Anything Protocol (TAP) tools.

%prep
%setup -q -n tap.py-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/tap
%python_clone -a %{buildroot}%{_bindir}/tappy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative tap
%python_install_alternative tappy

%postun
%python_uninstall_alternative tap
%python_uninstall_alternative tappy

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE
%python_alternative %{_bindir}/tappy
%python_alternative %{_bindir}/tap
%{python_sitelib}/*

%changelog
