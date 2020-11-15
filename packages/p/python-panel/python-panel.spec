#
# spec file for package python-panel
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


# Dependencies (e.g. bokeh) no longer support python2
%define skip_python2 1
%define modname panel
Name:           python-panel
Version:        0.10.1
Release:        0
Summary:        A high level app and dashboarding solution for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://panel.holoviz.org
Source:         https://files.pythonhosted.org/packages/source/p/panel/panel-%{version}.tar.gz
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module bokeh >= 2.0.0}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module param >= 1.9.3}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 0.7.4}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nbsmoke >= 0.2.0}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-Markdown
Requires:       python-bokeh >= 2.0.0
Requires:       python-param >= 1.9.3
Requires:       python-pyct >= 0.4.4
Requires:       python-pyviz-comms >= 0.7.4
Requires:       python-scipy
Requires:       python-tqdm
Recommends:     python-matplotlib
BuildArch:      noarch
%python_subpackages

%description
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

%prep
%setup -q -n panel-%{version}
# env-based hashbangs
%python_expand sed -i "1{s|#!/usr/bin/env python|#!%{_bindir}/$python|}" \
  examples/apps/django2/manage.py \
  examples/apps/django_multi_apps/manage.py

%build
%python_build

%install
%python_install

# MOVE EXAMPLES TO DOC DIR
mkdir -p %{buildroot}%{_docdir}/%{modname}
%python_expand mv %{buildroot}%{$python_sitelib}/%{modname}/examples %{buildroot}/%{_docdir}/%{modname}/

# UNNECESSARY HIDDEN FILE
%python_expand rm %{buildroot}%{$python_sitelib}/%{modname}/.version

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_docdir}/%{modname}/

%check
# DISABLE TESTS REQUIRING NETWORK ACCESS
%pytest -k 'not (test_loading_a_image_from_url or test_image_alt_text or test_image_link_url or test_vtk_pane_from_url or test_vtkjs_pane)'

%files %{python_files}
%license LICENSE.txt
%doc README.md
%doc %{_docdir}/%{modname}/
%python3_only %{_bindir}/panel
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
