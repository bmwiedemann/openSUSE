#
# spec file for package python-browsers
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Georg Pfuetzenreuter <mail+rpm@georg-pfuetzenreuter.net>
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define appname browsers
Name:           python-%{appname}%{psuffix}
Version:        0.6.0
Release:        0
Summary:        Library for detecting and launching browsers
License:        MIT
URL:            https://github.com/roniemartinez/browsers
Source0:        https://github.com/roniemartinez/browsers/archive/refs/tags/%{version}.tar.gz
# - test with Chromium instead of unavailable proprietary Chrome
# - adjust Firefox .desktop entry name
# - add Firefox to launch test
Patch0:         test.patch
# - adjust Chromium .desktop file name
Patch1:         chromium.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-pyxdg
Provides:       python3-pybrowsers
BuildArch:      noarch
# Browsers like Chromium are not built for other architectures
ExclusiveArch:  aarch64 riscv64 x86_64
%if %{with test}
BuildRequires:  %{python_module browsers}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  MozillaFirefox
BuildRequires:  chromium
# Firefox needs /etc/os-release
BuildRequires:  distribution-release
%endif
%python_subpackages

%description
Python library for detecting and launching browsers

%prep
%autosetup -p1 -n %{appname}-%{version}
sed -i '/pywin32/d' pyproject.toml

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{appname}
%endif

%if %{with test}
%check
%python_expand $python -m poetry config --local virtualenvs.in-project true && $python -m poetry run pytest
rm -r /home/abuild/.config
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/%{appname}
%{python_sitelib}/py%{appname}-%{version}.dist-info
%{python_sitelib}/%{appname}/*.py
%pycache_only %{python_sitelib}/%{appname}/__pycache__
%endif

%changelog
