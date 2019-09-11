#
# spec file for package python-lml
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
Name:           python-lml
Version:        0.0.9
Release:        0
Summary:        A lazy plugin management system for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/chfw/lml
Source:         https://files.pythonhosted.org/packages/source/l/lml/lml-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
LML is "Load me later". lml seamlessly finds the lml-based
plugins from the current Python environment but loads plugins on
demand. It supports plugins that have external dependencies,
especially bulky and/or memory hungry ones. lml provides the plugin
management system only and the plugin interface is for the developer
to do.

Plugins loaded by lml may be installed packages or standalone
Python modules in a supplied directory.

%prep
%setup -q -n lml-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests --with-doctest --doctest-extension=.rst README.rst tests docs/source lml

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst docs/source
%{python_sitelib}/*

%changelog
