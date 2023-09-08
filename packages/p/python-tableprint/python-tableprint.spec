#
# spec file for package python-tableprint
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           python-tableprint
Version:        0.9.1
Release:        0
Summary:        Pretty console printing of tabular data
License:        MIT
URL:            https://github.com/nirum/tableprint
Source:         https://github.com/nirum/tableprint/archive/v%{version}.tar.gz#/tableprint-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#nirum/tableprint#24
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wcwidth
BuildArch:      noarch
%python_subpackages

%description
Formatted console printing of tabular data.
tableprint lets you easily print formatted tables of data.
Unlike other modules, you can print single rows of data at a time
(useful for printing ongoing computation results).

%prep
%autosetup -p1 -n tableprint-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license License.md
%doc README.md
%{python_sitelib}/tableprint
%{python_sitelib}/tableprint-%{version}.dist-info

%changelog
