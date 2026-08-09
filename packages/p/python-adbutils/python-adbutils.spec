#
# spec file for package python-adbutils
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-adbutils
Version:        2.12.0
Release:        0
Summary:        Pure Python Adb Library
License:        MIT
URL:            https://github.com/openatx/adbutils
Source:         https://files.pythonhosted.org/packages/source/a/adbutils/adbutils-%{version}.tar.gz
Patch1:         fix-shebang.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module deprecation >= 2.0.6}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module retry}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-deprecation >= 2.0.6
Requires:       python-Pillow
Requires:       python-requests
Requires:       python-retry
BuildArch:      noarch
%python_subpackages

%description
Pure Python Adb Library

%prep
%autosetup -p1 -n adbutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python3_fix_shebang

%check
%pytest

%files %{python_files}
%doc ChangeLog README.md
%license LICENSE AUTHORS
%{python_sitelib}/adbutils
%{python_sitelib}/adbutils-%{version}.dist-info

%changelog
