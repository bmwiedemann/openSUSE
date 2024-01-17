#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

Name:           python-%{pkg_name}
Version:        0.0.3
Release:        0
Summary:        Parse HID report descriptors
License:        MIT
URL:            https://github.com/FFY00/python-hid-parser
Source0:        https://files.pythonhosted.org/packages/48/af/6266119b18570fee7dc838c3389e37db3586a4e2003de709cf4ac24e395a/hid-parser-0.0.3.tar.gz
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
%setup -q -n %{pkg_name}-%{version}

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
