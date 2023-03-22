#
# spec file for package python-hsluv
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


Name:           python-hsluv
Version:        5.0.3
Release:        0
Summary:        Human-friendly HSL
License:        MIT
URL:            https://www.hsluv.org
Source:         https://files.pythonhosted.org/packages/source/h/hsluv/hsluv-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Human-friendly HSL

%prep
%autosetup -p1 -n hsluv-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%pycache_only %{python_sitelib}/__pycache__/hsluv*.pyc
%{python_sitelib}/hsluv.py
%{python_sitelib}/hsluv-%{version}*-info

%changelog
