#
# spec file for package python-uc-micro-py
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
Name:           python-uc-micro-py
Version:        1.0.1
Release:        0
Summary:        Micro subset of unicode data files for linkify-it-py projects
License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
Source:         https://github.com/tsutsu3/uc.micro-py/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Micro subset of unicode data files for linkify-it-py projects.

%prep
%setup -q -n uc.micro-py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/uc_micro
%{python_sitelib}/uc_micro_py-%{version}*.egg-info

%changelog
