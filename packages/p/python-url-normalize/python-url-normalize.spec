#
# spec file for package python-url-normalize
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

%{?sle15_python_module_pythons}
Name:           python-url-normalize
Version:        2.2.1
Release:        0
Summary:        URL normalization for Python
License:        MIT
URL:            https://github.com/niksite/url-normalize
Source:         https://github.com/niksite/url-normalize/archive/refs/tags/v%{version}.tar.gz#/url-normalize-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module idna >= 3.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-url_normalize = %{version}-%{release}
Requires:       python-idna >= 3.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
URL normalization for Python.

%prep
%autosetup -p1 -n url-normalize-%{version}
# Do not require pytest-ruff
sed -i '/^  "--ruff",$/d' pyproject.toml
# Do not fail over coverage issues
sed -i '/^  "--cov-fail-under=100",$/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/url-normalize

%check
%pytest

%post
%python_install_alternative url-normalize

%postun
%python_uninstall_alternative url-normalize

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/url-normalize
%{python_sitelib}/url_normalize
%{python_sitelib}/url_normalize-%{version}.dist-info

%changelog
