#
# spec file for package python-aioitertools
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-aioitertools
Version:        0.7.0
Release:        0
Summary:        itertools and builtins for AsyncIO and mixed iterables
License:        MIT
Group:          Development/Languages/Python
URL:            https://aioitertools.omnilib.dev
Source:         https://files.pythonhosted.org/packages/source/a/aioitertools/aioitertools-%{version}.tar.gz
BuildRequires:  %{python_module asyncio}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 3.7
BuildArch:      noarch
%python_subpackages

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type iterables.

%prep
%setup -q -n aioitertools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/*

%changelog
