#
# spec file for package python-proton-client
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


%define skip_python2 1
Name:           python-proton-client
Version:        0.7.1
Release:        0
Summary:        Safely login with ProtonVPN credentials to connect to Proton
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonMail/proton-python-client
Source:         https://github.com/ProtonMail/proton-python-client/archive/refs/tags/%{version}.tar.gz#/proton-python-client-%{version}.tar.gz
Patch1:         urllib3-v2-migration.patch
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module gnupg}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libopenssl)
Requires:       python-bcrypt
Requires:       python-gnupg
Requires:       python-pyOpenSSL
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
This package, originally forked from python-srp module implements a simple
wrapper to Proton Technologies API, abstracting from the SRP authentication.

%prep
%autosetup -n proton-python-client-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip test_tlspinning.py as OBS has no network access
%pytest tests --ignore=tests/test_tlspinning.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_client-%{version}*-info

%changelog
