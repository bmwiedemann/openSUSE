#
# spec file for package python-pymediainfo
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


%define skip_python2 1
Name:           python-pymediainfo
Version:        7.0.1
Release:        0
Summary:        Python wrapper for the mediainfo library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sbraz/pymediainfo
Source0:        https://files.pythonhosted.org/packages/source/p/pymediainfo/pymediainfo-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module importlib-metadata if %python-version < 3.8}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  libmediainfo0
Requires:       libmediainfo0
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module is a Python wrapper for the mediainfo library.

%prep
%autosetup -p1 -n pymediainfo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pymediainfo
%{python_sitelib}/pymediainfo-%{version}.dist-info

%changelog
