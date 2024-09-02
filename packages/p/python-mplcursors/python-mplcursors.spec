#
# spec file for package python-mplcursors
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


Name:           python-mplcursors
Version:        0.5.3
Release:        0
Summary:        Interactive data selection cursors for Matplotlib
License:        Zlib
URL:            https://github.com/anntzer/mplcursors
Source:         https://files.pythonhosted.org/packages/source/m/mplcursors/mplcursors-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mplcursors-10b553e-mpl3.9-pytest8.patch https://github.com/anntzer/mplcursors/commit/10b553e
Patch0:         mplcursors-10b553e-mpl3.9-pytest8.patch
# PATCH-FIX-UPSTREAM mplcursors-1d9461c-np2.patch https://github.com/anntzer/mplcursors/commit/1d9461c
Patch1:         mplcursors-1d9461c-np2.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.1
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
Requires:       (python-matplotlib >= 3.1 without python-matplotlib = 3.7.1)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.1 without %python-matplotlib = 3.7.1}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
mplcursors provides interactive data selection cursors for Matplotlib.

%prep
%setup -q -n mplcursors-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/mplcursors
%{python_sitelib}/mplcursors.pth
%{python_sitelib}/mplcursors-%{version}*-info

%changelog
