#
# spec file for package python-piexif
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-piexif
Version:        1.1.3
Release:        0
Summary:        To simplify exif manipulations with python. Writing, reading, and more
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/hMatoba/Piexif
Source:         https://files.pythonhosted.org/packages/source/p/piexif/piexif-%{version}.zip
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  unzip
BuildRequires:  fdupes
## needed for tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Pillow}
BuildArch:      noarch
%python_subpackages

%description
%summary.

%prep
%autosetup -p1 -n piexif-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="load"
%pytest -k "not $donttest"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/piexif
%{python_sitelib}/piexif-%{version}.dist-info

%changelog
