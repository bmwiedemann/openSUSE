#
# spec file for package python-certbot-apache
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
Name:           python-certbot-apache
Version:        5.1.0
Release:        0
Summary:        Apache plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/letsencrypt/letsencrypt
Source:         https://files.pythonhosted.org/packages/source/c/certbot-apache/certbot_apache-%{version}.tar.gz
BuildRequires:  %{python_module augeas}
BuildRequires:  %{python_module certbot >= %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       apache2 >= 2.3
Requires:       python-acme >= %{version}
Requires:       python-augeas
Requires:       python-certbot >= %{version}
BuildArch:      noarch
%python_subpackages

%description
The Apache plugin for Certbot.

%prep
%setup -q -n certbot_apache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/certbot_apache
%{python_sitelib}/certbot_apache-%{version}*info

%changelog
