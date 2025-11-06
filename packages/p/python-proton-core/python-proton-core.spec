#
# spec file for package python-proton-core
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-proton-core
Version:        0.7.0
Release:        0
Summary:        Proton VPN core library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/python-proton-core
Source:         https://github.com/ProtonVPN/python-proton-core/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module gnupg}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pyotp}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(libopenssl)
Requires:       python-aiohttp
Requires:       python-bcrypt
Requires:       python-gnupg
Requires:       python-importlib-metadata
Requires:       python-pyOpenSSL
Requires:       python-requests
Conflicts:      python-proton-client
BuildArch:      noarch
%python_subpackages

%description
This package contains core logic used by the other Proton components.

%prep
%autosetup -p1 -n python-proton-core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip some tests as OBS has no network access
%pytest tests --ignore=tests/test_alternativerouting.py --ignore=tests/test_autotransport.py --ignore=tests/test_protonsso.py --ignore=tests/test_session.py --ignore=tests/test_tlsverification.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_core-%{version}*-info

%changelog
