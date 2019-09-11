#
# spec file for package python-wiring
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
%{!?license: %global license %doc}
%bcond_without test
Name:           python-wiring
Version:        0.4.0
Release:        0
Summary:        Architectural foundation for Python applications
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/msiedlarek/wiring
Source:         https://files.pythonhosted.org/packages/source/w/wiring/wiring-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Recommends:     python-venusian
BuildArch:      noarch
%python_subpackages

%description
Wiring provides architectural foundation for Python applications, featuring:
* dependency injection
* interface definition and validation
* modular component configuration
* small, extremely pedantic codebase

Full documentation is available at http://wiring.readthedocs.org

%prep
%setup -q -n wiring-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{python_sitelib}/wiring/

%files %{python_files}
%doc README.rst
%%license LICENSE
%{python_sitelib}/*

%changelog
