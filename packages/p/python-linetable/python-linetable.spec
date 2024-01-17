#
# spec file for package python-linetable
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-linetable
Version:        0.0.3
Release:        0
Summary:        library to manage Python Locations Table (co_linetable)
License:        MIT
URL:            https://github.com/amol-/linetable
Source:         https://files.pythonhosted.org/packages/source/l/linetable/linetable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
library to manage Python Locations Table (co_linetable)

%prep
%setup -q -n linetable-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
