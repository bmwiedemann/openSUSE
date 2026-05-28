#
# spec file for package python-pyshark
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2022, Martin Hauke <mardnh@gmx.de>
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
Name:           python-pyshark
Version:        0.6
Release:        0
Summary:        A Python wrapper for tshark output parsing
License:        MIT
URL:            https://github.com/KimiNewt/pyshark
#Git-Clone:     https://github.com/KimiNewt/pyshark.git
Source:         https://github.com/KimiNewt/pyshark/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_tshark.patch -- based on PR 744
Patch0:         fix_tshark.patch
# PATCH-FIX-UPSTREAM gh#KimiNewt/pyshark#755
Patch1:         support-python-314.patch
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  wireshark
Requires:       python-appdirs
Requires:       python-lxml
Requires:       python-packaging
Requires:       python-termcolor
Requires:       wireshark
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for tshark, allowing python packet parsing using
wireshark dissectors.

%prep
%autosetup -p1 -n pyshark-%{version}/src
dos2unix ../README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test "inmem_capture" needs to be fixed upstream, do not run it for now
rm -f ../tests/capture/test_inmem_capture.py ../tests/capture/test_live_capture.py
# test_iterate_empty_psml_capture broken with Python 3.14 forkserver
# test_get_tshark_path missing config
%pytest ../tests -k 'not (test_iterate_empty_psml_capture or test_get_tshark_path)'

%files %{python_files}
%license ../LICENSE.txt
%doc ../README.md
%{python_sitelib}/pyshark
%{python_sitelib}/pyshark-%{version}.dist-info

%changelog
