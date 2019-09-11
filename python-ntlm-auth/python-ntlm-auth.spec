#
# spec file for package python-ntlm-auth
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
Name:           python-ntlm-auth
Version:        1.3.0
Release:        0
Summary:        NTLM low-level Python library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jborean93/ntlm-auth
Source:         https://github.com/jborean93/ntlm-auth/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-ordereddict
Recommends:     python-cryptography
BuildArch:      noarch
%python_subpackages

%description
This library handles the low-level details of NTLM authentication for
use in authenticating with a service that uses NTLM. It will create
and parse the 3 different message types in the order required and
produce a base64 encoded value that can be attached to the HTTP
header.

%prep
%setup -q -n ntlm-auth-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version}

%files %{python_files}
%license LICENSE
%doc CHANGES.md README.md
%{python_sitelib}/*

%changelog
