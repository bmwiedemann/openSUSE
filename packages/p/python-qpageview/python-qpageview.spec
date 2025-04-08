#
# spec file for package python-qpageview
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-qpageview
Version:        1.0.0
Release:        0
Summary:        Widget to display page-based documents for Qt5/PyQt5
License:        GPL-3.0-only
URL:            https://github.com/frescobaldi/qpageview
Source:         https://files.pythonhosted.org/packages/source/q/qpageview/qpageview-%{version}.tar.gz
BuildRequires:  %{python_module cups}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module qt6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-qt6
BuildArch:      noarch
%python_subpackages

%description
Widget to display page-based documents for Qt6/PyQt6

%prep
%setup -q -n qpageview-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/qpageview
%{python_sitelib}/qpageview-%{version}*-info

%changelog
