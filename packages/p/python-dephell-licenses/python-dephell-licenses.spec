#
# spec file for package python-dephell-licenses
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-dephell-licenses
Version:        0.1.6
Release:        0
Summary:        Dephell library to get info about OSS licenses
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dephell/dephell_licenses
Source:         https://files.pythonhosted.org/packages/source/d/dephell-licenses/dephell-licenses-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Dephell library to get info about OSS licenses.

%prep
%setup -q -n dephell-licenses-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_make_text - online test
%pytest -k 'not test_make_text'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
