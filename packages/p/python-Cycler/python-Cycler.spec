#
# spec file for package python-Cycler
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Cycler
Version:        0.10.0
Release:        0
Summary:        Composable style cycles
License:        BSD-3-Clause
URL:            https://github.com/matplotlib/cycler
Source:         https://files.pythonhosted.org/packages/source/c/cycler/cycler-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
When plotting more than one line it is common to want to be able to
cycle over one or more artist styles. For simple cases than can be
done with out too much trouble.

However, if you want to do something more complicated, the plotting
logic can quickly become very involved. To address this and allow
easy cycling over arbitrary kwargs the Cycler class, a composable
kwarg iterator, was developed.

%prep
%setup -q -n cycler-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
