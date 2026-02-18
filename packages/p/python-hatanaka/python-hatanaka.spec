#
# spec file for package python-hatanaka
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

# affects the python macros even if not used in the spec file
%bcond_without libalternatives

%{?sle15_python_module_pythons}
%define pyname hatanaka
Name:           python-%{pyname}
Version:        2.8.1
Release:        0
Summary:        Effortless compression / decompression of RINEX files in Python
License:        BSD-3-Clause
URL:            https://github.com/valgur/%{pyname}
Source:         https://github.com/valgur/%{pyname}/archive/refs/tags/v%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module importlib_resources}
BuildRequires:  %{python_module ncompress}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{python_module importlib_resources}
Requires:       %{python_module ncompress}
Requires:       alts
%python_subpackages

%description
Effortless compression / decompression of RINEX files in Python and on the command line.

Supports all compression formats allowed by the RINEX 2, 3 and 4 standards:
* Hatanaka compression for Observation Data Files,
* LZW (.Z), gzip (.gz), bzip2 (.bz2) and .zip.

%prep
%autosetup -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/crx2rnx
%python_clone -a %{buildroot}%{_bindir}/rinex-compress
%python_clone -a %{buildroot}%{_bindir}/rinex-decompress
%python_clone -a %{buildroot}%{_bindir}/rnx2crx

%check
export LANG=en_US.UTF-8
%pytest -rs --tb=short

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{pyname}
%{python_sitearch}/%{pyname}-%{version}.dist-info
%python_alternative %{_bindir}/crx2rnx
%python_alternative %{_bindir}/rinex-compress
%python_alternative %{_bindir}/rinex-decompress
%python_alternative %{_bindir}/rnx2crx

%changelog
