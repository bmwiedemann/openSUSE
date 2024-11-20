#
# spec file for package python-hid-parser
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


%define pkg_name hid-parser
%{?sle15_python_module_pythons}
Name:           python-%{pkg_name}
Version:        0.0.3
Release:        0
Summary:        Parse HID report descriptors
License:        MIT
URL:            https://github.com/FFY00/python-hid-parser
Source0:        https://files.pythonhosted.org/packages/source/h/hid-parser/hid-parser-%{version}.tar.gz
Patch1:         pytest-catch-warnings.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# TEST
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module hypothesis}
# /TEST
BuildRequires:  fdupes
BuildArch:      noarch
Conflicts:      solaar < 1.1.7
%python_subpackages

%description
Typed pure Python library to parse HID report descriptors

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/hid_parser
%{python_sitelib}/hid_parser-%{version}.dist-info

%changelog
