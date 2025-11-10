#
# spec file for package python-automaton
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-automaton
Version:        3.2.0
Release:        0
Summary:        Friendly state machines for python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/automaton
Source0:        https://files.pythonhosted.org/packages/source/a/automaton/automaton-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Friendly state machines for python.

%package -n python-automaton-doc
Summary:        Documentation for the Automaton Library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-automaton-doc
Documentation for the Automaton library.

%prep
%autosetup -p1 -n automaton-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/automaton
%{python_sitelib}/automaton-%{version}.dist-info

%files -n python-automaton-doc
%license LICENSE
%doc doc/build/html

%changelog
