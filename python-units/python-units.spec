#
# spec file for package python-units
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-units
Version:        0.07
Release:        0
Summary:        Python support for quantities with units
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://bitbucket.org/adonohue/units/
Source:         https://files.pythonhosted.org/packages/source/u/units/units-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Provides support for quantities and units, which strictly disallow
invalid operations between incompatible quantities. For example, one
cannot add 2 metres to 5 seconds, because this doesn't make sense.

%prep
%setup -q -n units-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rf _build.* build
%{python_expand rm -rf _build.* build
py.test-%{$python_bin_suffix}
}

%files %{python_files}
%doc README
%license units/LICENSE
%{python_sitelib}/*

%changelog
