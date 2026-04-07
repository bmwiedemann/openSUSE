#
# spec file for package python-hid-parser
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


%{?sle15_python_module_pythons}
Name:           python-hid-parser
Version:        0.1.0
Release:        0
Summary:        Parse HID report descriptors
License:        MIT
URL:            https://github.com/FFY00/python-hid-parser
Source0:        https://files.pythonhosted.org/packages/source/h/hid-parser/hid_parser-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# TEST
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 4.4.0 if %python-base < 3.13}
# /TEST
BuildRequires:  fdupes
Requires:       (python-typing-extensions >= 4.4.0 if python-base < 3.13)
BuildArch:      noarch
Conflicts:      solaar < 1.1.7
%python_subpackages

%description
Typed pure Python library to parse HID report descriptors

%prep
%autosetup -n hid_parser-%{version}

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
