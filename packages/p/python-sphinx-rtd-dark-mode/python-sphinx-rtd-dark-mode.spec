#
# spec file for package python-sphinx-rtd-dark-mode
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


Name:           python-sphinx-rtd-dark-mode
Version:        1.3.0
Release:        0
Summary:        Dark mode for the Sphinx Read the Docs theme
License:        MIT
URL:            https://github.com/MrDogeBro/sphinx_rtd_dark_mode
Source:         https://github.com/MrDogeBro/sphinx_rtd_dark_mode/archive/refs/tags/v%{version}.tar.gz#/sphinx_rtd_dark_mode-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-sphinx_rtd_theme
Provides:       python-sphinx_rtd_dark_mode = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Dark mode for the Sphinx Read the Docs theme.

%prep
%autosetup -p1 -n sphinx_rtd_dark_mode-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/build.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/sphinx_rtd_dark_mode
%{python_sitelib}/sphinx_rtd_dark_mode-%{version}.dist-info

%changelog
