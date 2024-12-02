#
# spec file for package python-pyasyncore
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


# Requires Python 3.11 or above
%define skip_python310 1
Name:           python-pyasyncore
Version:        1.0.4
Release:        0
Summary:        Make asyncore available for Python 3.12 onwards
License:        PSF-2.0
URL:            https://github.com/simonrob/pyasyncore
Source:         https://github.com/simonrob/pyasyncore/archive/refs/tags/v%{version}.tar.gz#/pyasyncore-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Make asyncore available for Python 3.12 onwards

%prep
%autosetup -p1 -n pyasyncore-%{version}
chmod -x LICENSE README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/asyncore
%{python_sitelib}/pyasyncore-%{version}.dist-info

%changelog
