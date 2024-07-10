#
# spec file for package python-click-didyoumean
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


%{?sle15_python_module_pythons}
Name:           python-click-didyoumean
Version:        0.3.1
Release:        0
Summary:        Plugin to enable git-like did-you-mean feature in python-click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/timofurrer/click-didyoumean
Source:         https://github.com/click-contrib/click-didyoumean/archive/v%{version}.tar.gz#/click-didyoumean-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package enables a git-like did-you-mean feature in click.

%prep
%setup -q -n click-didyoumean-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/click_didyoumean
%{python_sitelib}/click_didyoumean-%{version}.dist-info

%changelog
