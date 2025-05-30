#
# spec file for package python-httpsig_cffi
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-httpsig_cffi
Version:        15.0.0
Release:        0
Summary:        Secure HTTP request signing using the HTTP Signature draft specification
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hawkowl/httpsig_cffi
Source:         https://files.pythonhosted.org/packages/source/h/httpsig_cffi/httpsig_cffi-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/hawkowl/httpsig_cffi/pull/2 Fix cryptography deprecation warnings and future warning in get_fingerprint
Patch0:         new-cryptography.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/httpsig_cffi
%{python_sitelib}/httpsig_cffi-%{version}*-info

%changelog
