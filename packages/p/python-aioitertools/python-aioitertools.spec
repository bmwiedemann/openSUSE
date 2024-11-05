#
# spec file for package python-aioitertools
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-aioitertools
Version:        0.12.0
Release:        0
Summary:        Itertools and builtins for AsyncIO and mixed iterables
License:        MIT
Group:          Development/Languages/Python
URL:            https://aioitertools.omnilib.dev
Source:         https://github.com/omnilib/aioitertools/archive/v%{version}.tar.gz#/aioitertools-%{version}.tar.gz
BuildRequires:  %{python_module asyncio}
BuildRequires:  %{python_module flit-core > 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 310
Requires:       python-typing_extensions >= 4.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type iterables.

%prep
%autosetup -p1 -n aioitertools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/aioitertools
%{python_sitelib}/aioitertools-%{version}*-info

%changelog
