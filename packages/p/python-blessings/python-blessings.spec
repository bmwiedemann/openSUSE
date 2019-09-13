#
# spec file for package python-blessings
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-blessings
Version:        1.7
Release:        0
Summary:        A thin, practical wrapper around terminal capabilities in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/erikrose/blessings
Source:         https://files.pythonhosted.org/packages/source/b/blessings/blessings-%{version}.tar.gz
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
Requires:       python-curses
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Curses-like terminal wrapper with a display based on compositing 2d
arrays of text.

%prep
%setup -q -n blessings-%{version}

%build
%python_build

%install
%python_install

%check
# Can't be run because it expects real term where it can play with colours
#%%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
