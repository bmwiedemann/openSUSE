#
# spec file for package python-click-extra
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


%define module_name click-extra
%{?sle15_python_module_pythons}
Name:           python-click-extra
Version:        4.14.1
Release:        0
Summary:        Drop-in replacement for Click to make user-friendly and colorful CLI
License:        GPL-2.0-or-later
URL:            https://github.com/kdeldycke/click-extra
Source:         https://github.com/kdeldycke/click-extra/archive/v%{version}.tar.gz#/%{module_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION Build dependencies
# https://github.com/kdeldycke/click-extra/blob/v4.8.3/pyproject.toml#L67
BuildRequires:  %{python_module PyYAML >= 6.0.0}
BuildRequires:  %{python_module boltons >= 25.0.0}
BuildRequires:  %{python_module click >= 8.1.8}
BuildRequires:  %{python_module cloup >= 3.0.5}
BuildRequires:  %{python_module extra-platforms >= 2.0.0}
BuildRequires:  %{python_module mergedeep >= 1.3.4}
BuildRequires:  %{python_module requests >= 2.32.3}
BuildRequires:  %{python_module tabulate >= 0.9}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python-base < 3.11}
BuildRequires:  %{python_module wcmatch >= 10.0}
BuildRequires:  %{python_module xmltodict >= 0.14.2}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pygments >= 2.14}
BuildRequires:  %{python_module pygments-ansi-color >= 0.3.0}
# https://github.com/kdeldycke/click-extra/blob/v4.8.3/pyproject.toml#L117
BuildRequires:  %{python_module pytest >= 8}
BuildRequires:  %{python_module pytest-httpserver >= 1.0.6}
BuildRequires:  %{python_module pytest-randomly >= 3.16.0}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# https://github.com/kdeldycke/click-extra/blob/v4.8.3/pyproject.toml#L67
Requires:       python-PyYAML >= 6.0.0
Requires:       python-boltons >= 25.0.0
Requires:       python-click >= 8.1.4
Requires:       python-cloup >= 3.0.5
Requires:       python-extra-platforms >= 2.0.0
Requires:       python-mergedeep >= 1.3.4
Requires:       python-requests >= 2.32.3
Requires:       python-tabulate >= 0.9
Requires:       python-wcmatch >= 10.0
Requires:       python-xmltodict >= 0.14.2
Requires:       (python-tomli >= 2.0.1 if python-base < 3.11)
# https://github.com/kdeldycke/click-extra/blob/v4.8.3/pyproject.toml#L94
Suggests:       python-pygments >= 2.14
Suggests:       python-pygments-ansi-color >= 0.3.0
BuildArch:      noarch
%python_subpackages

%description
🌈 Drop-in replacement for Click to make user-friendly and colorful CLI

%prep
%autosetup -p1 -n %{module_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove coverage configuration
sed -i '/--cov.*",/d' pyproject.toml
# ignore test that requires network connectivity
%pytest -k 'not (test_ansi_lexers_candidates)'

%files %{python_files}
%{python_sitelib}/click_extra
%{python_sitelib}/click_extra-%{version}.dist-info

%changelog
