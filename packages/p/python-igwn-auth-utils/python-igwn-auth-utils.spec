#
# spec file for package python-igwn-auth-utils
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%global srcname igwn-auth-utils
Name:           python-igwn-auth-utils
Version:        0.4.0
Release:        0
Summary:        Auth Utils for International Gravitational-Wave Observatory Network (IGWN)
License:        BSD-3-Clause
URL:            https://git.ligo.org/computing/igwn-auth-utils
Source:         https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.3
Requires:       python-requests >= 2.14
Requires:       python-safe-netrc >= 1.0.0
Requires:       python-scitokens >= 1.7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.3}
BuildRequires:  %{python_module pytest >= 3.9.1}
BuildRequires:  %{python_module requests >= 2.14}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module safe-netrc >= 1.0.0}
BuildRequires:  %{python_module scitokens >= 1.7.0}
# /SECTION
# The [requests] extra was a subpackage but is included into the main requirements since 0.3
Provides:       python-igwn-auth-utils-requests = %{version}-%{release}
Obsoletes:      python-igwn-auth-utils-requests <= 0.3
%python_subpackages

%description
Python library functions to simplify using International Gravitational-Wave
Observatory Network (IGWN) authorisation credentials.

This project is primarily aimed at discovering X.509 credentials and
SciTokens for use with HTTP(S) requests to IGWN-operated services.

%prep
%setup -q -n %{srcname}-%{version}
sed -i 's/--color=yes//' pyproject.toml
sed -i '/"error",/ a \        "ignore:pkg_resources is deprecated as an API:DeprecationWarning",' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/igwn_auth_utils
%{python_sitelib}/igwn_auth_utils-%{version}*-info

%changelog
