#
# spec file for package python-lfdfiles
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
%global skip_python311 1
Name:           python-lfdfiles
Version:        2026.6.24
Release:        0
Summary:        Laboratory for Fluorescence Dynamics (LFD) file formats
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/lfdfiles
Source:         https://github.com/cgohlke/lfdfiles/archive/v%{version}.tar.gz#/lfdfiles-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module czifile >= 2019.7.2}
BuildRequires:  %{python_module matplotlib >= 3.2.0}
BuildRequires:  %{python_module netpbmfile >= 2020.9.18}
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module oiffile >= 2020.9.18}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2020.9.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-czifile >= 2019.7.2
Requires:       python-matplotlib >= 3.2.0
Requires:       python-netpbmfile >= 2020.9.18
Requires:       python-numpy >= 1.15
Requires:       python-oiffile >= 2020.9.18
Requires:       python-tifffile >= 2020.9.3
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Lfdfiles is a Python library and console script for reading, writing,
converting, and viewing many of the proprietary file formats used to store
experimental data at the Laboratory for Fluorescence Dynamics.

%prep
%setup -q -n lfdfiles-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//g' README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lfdfiles

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%pre
%python_reset_alternative lfdfiles

%post
%python_install_alternative lfdfiles

%postun
%python_uninstall_alternative lfdfiles

%check
true

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/lfdfiles
%{python_sitelib}/lfdfiles
%{python_sitelib}/lfdfiles-%{version}.dist-info

%changelog
