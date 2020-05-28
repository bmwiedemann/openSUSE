#
# spec file for package python-demjson
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
%bcond_without tests
Name:           python-demjson
Version:        2.2.4
Release:        0
Summary:        Encoder, decoder, and lint/validator for JSON compliant with RFC 4627
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://deron.meranda.us/python/demjson/
Source:         https://files.pythonhosted.org/packages/source/d/demjson/demjson-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This module provides classes and functions for encoding or decoding data
represented in the language-neutral JSON format (which is often used as a
simpler substitute for XML in Ajax web applications).  This implementation tries
to be as compliant to the JSON specification (RFC 4627) as possible, while
still providing many optional extensions to allow less restrictive JavaScript
syntax.  It includes complete Unicode support, including UTF-32, BOM, and
surrogate pair processing.  It can also support JavaScript's
NaN and Infinity numeric types as well as it's 'undefined' type.
It also includes a lint-like JSON syntax validator which tests JSON text
for strict compliance to the standard.

%prep
%setup -q -n demjson-%{version}
sed -i "1d" demjson.py # Fix non-executable script

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jsonlint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}3
%check
%python_expand cp test/test_demjson.py test/test_demjson_%{$python_bin_suffix}.py
%if %{have_python3}
2to3 -nw test/test_demjson_%{python3_bin_suffix}.py
%endif
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test/test_demjson_%{$python_bin_suffix}.py
}
%endif

%post
%python_install_alternative jsonlint

%postun
%python_uninstall_alternative jsonlint

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%doc docs/
%python_alternative %{_bindir}/jsonlint
%{python_sitelib}/*

%changelog
