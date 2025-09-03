#
# spec file for package python-acme
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


%{?sle15_python_module_pythons}
%define libname acme
Name:           python-%{libname}
Version:        5.0.0
Release:        0
Summary:        Python library for the ACME protocol
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        https://files.pythonhosted.org/packages/source/a/%{libname}/%{libname}-%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 43.0.0}
BuildRequires:  %{python_module josepy >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 25.0.0}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 43.0.0
Requires:       python-josepy >= 2.0.0
Requires:       python-pyOpenSSL >= 25.0.0
Requires:       python-pyRFC3339
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
%if %{?suse_version} < 1500
BuildRequires:  %{python_module devel}
%endif
%python_subpackages

%description
Python library implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the certbot project. Formerly Let's Encrypt project.

%prep
%setup -q -n %{libname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{libname}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%pycache_only %{python_sitelib}/%{libname}/__pycache__
%{python_sitelib}/%{libname}
%{python_sitelib}/%{libname}-%{version}.dist-info

%changelog
