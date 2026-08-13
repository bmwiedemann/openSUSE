#
# spec file for package python-proton-keyring-linux
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         _modname proton_keyring_linux
%{?sle15_python_module_pythons}
Name:           python-proton-keyring-linux
Version:        0.2.3
Release:        0
Summary:        Proton keyring Linux library
License:        GPL-3.0-or-later
URL:            https://github.com/ProtonVPN/python-proton-keyring-linux
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module SecretStorage}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-core}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-keyring
Requires:       python-proton-core
Obsoletes:      python-proton-keyring-linux-secretservice <= 0.1.0
Provides:       python-proton-keyring-linux-secretservice = %{version}
BuildArch:      noarch
%python_subpackages

%description
%{summary}.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/proton/keyring_linux/

%check
%pytest

%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/proton
%{python_sitelib}/proton/keyring_linux
%{python_sitelib}/%{_modname}-%{version}.dist-info

%changelog
