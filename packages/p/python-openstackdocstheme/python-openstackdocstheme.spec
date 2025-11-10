#
# spec file for package python-openstackdocstheme
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


%global pythons %{primary_python}
Name:           python-openstackdocstheme
Version:        3.5.0
Release:        0
Summary:        OpenStack Docs Theme
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/openstackdocstheme
Source0:        https://files.pythonhosted.org/packages/source/o/openstackdocstheme/openstackdocstheme-%{version}.tar.gz
BuildRequires:  %{python_module dulwich >= 0.15.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildRequires:  python3-Sphinx
Requires:       python-Sphinx
Requires:       python-dulwich >= 0.15.0
BuildArch:      noarch
%python_subpackages

%description
Theme and extension support for Sphinx documentation that is published
to docs.openstack.org. Intended for use by OpenStack projects.

%prep
%autosetup -p1 -n openstackdocstheme-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
PYTHONPATH=. sphinx-build -a -E -j auto -d doc/build/doctrees -b html doc/source doc/build/htm

%files %{python_files}
%license LICENSE
%doc README.rst
%{_bindir}/docstheme-build-pdf
%{_bindir}/docstheme-build-translated.sh
%{_bindir}/docstheme-lang-display-name.py
%{python_sitelib}/openstackdocstheme
%{python_sitelib}/openstackdocstheme-%{version}.dist-info

%changelog
