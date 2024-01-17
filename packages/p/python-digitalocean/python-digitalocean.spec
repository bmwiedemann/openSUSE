#
# spec file for package python-digitalocean
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


%{?sle15_python_module_pythons}
Name:           python-digitalocean
Version:        1.17.0
Release:        0
Summary:        Python module for Digital Ocean droplets
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/koalalorenzo/python-digitalocean/
Source:         https://github.com/koalalorenzo/python-digitalocean/archive/v%{version}.tar.gz
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.2.1}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 < 2.0.6}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-jsonpickle
Requires:       python-pytest
Requires:       python-requests >= 2.2.1
Requires:       python-responses
# urllib3 2.0.6 strips Cookies header, which changes the behavior of requests, which in turn breaks the Firewall tests
Requires:       python-urllib3 < 2.0.6
BuildArch:      noarch
%python_subpackages

%description
Python module to manage Digital Ocean droplets.

%prep
%autosetup -p1 -n python-digitalocean-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/digitalocean
%{python_sitelib}/python_digitalocean-%{version}*-info

%changelog
