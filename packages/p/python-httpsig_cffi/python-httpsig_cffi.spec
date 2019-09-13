#
# spec file for package python-httpsig_cffi
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
Name:           python-httpsig_cffi
Version:        15.0.0
Release:        0
Summary:        Secure HTTP request signing using the HTTP Signature draft specification
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hawkowl/httpsig_cffi
Source:         https://files.pythonhosted.org/packages/source/h/httpsig_cffi/httpsig_cffi-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Secure HTTP request signing using the HTTP Signature draft specification

%prep
%setup -q -n httpsig_cffi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
