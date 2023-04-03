#
# spec file for package python-lazy-loader
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


Name:           python-lazy-loader
Version:        0.2
Release:        0
Summary:        Populate library namespace without incurring immediate import costs
License:        BSD-3-Clause
URL:            https://github.com/scientific-python/lazy_loader
Source:         https://files.pythonhosted.org/packages/source/l/lazy_loader/lazy_loader-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-lazy_loader = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
lazy_loader makes it easy to load subpackages and functions on demand.
  1. Allow subpackages to be made visible to users without incurring import costs.
  2. Allow external libraries to be imported only when used, improving import times.

%prep
%setup -q -n lazy_loader-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/lazy_loader
%{python_sitelib}/lazy_loader-%{version}.dist-info

%changelog
