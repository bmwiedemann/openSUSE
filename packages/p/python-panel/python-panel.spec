#
# spec file for package python-panel
#
# Copyright (c) 2021 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
%define modname panel
Name:           python-panel%{psuffix}
Version:        0.10.2
Release:        0
Summary:        A high level app and dashboarding solution for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://panel.holoviz.org
Source:         https://files.pythonhosted.org/packages/source/p/panel/panel-%{version}.tar.gz
Source99:       python-panel-rpmlintrc
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module bokeh >= 2.2.2}
BuildRequires:  %{python_module param >= 1.9.3}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 0.7.4}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module holoviews}
BuildRequires:  %{python_module ipympl}
BuildRequires:  %{python_module ipython >= 7.0}
BuildRequires:  %{python_module nbsmoke >= 0.2.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module streamz}
BuildRequires:  %{python_module twine}
# Tests segfault
# BuildRequires:  %%{python_module vtk}
%endif
Requires:       python-Markdown
Requires:       python-bokeh >= 2.2.2
Requires:       python-param >= 1.9.3
Requires:       python-pyct >= 0.4.4
Requires:       python-pyviz-comms >= 0.7.4
Requires:       python-requests
Requires:       python-tqdm
Requires(post):   update-alternatives
Requires(postun): update-alternatives
Recommends:     python-plotly
Recommends:     python-Pillow
Recommends:     python-matplotlib
Recommends:     python-notebook >= 5.4
Recommends:     python-holoviews >= 1.13.2
BuildArch:      noarch
%python_subpackages

%description
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

%prep
%setup -q -n panel-%{version}
# Do not try to rebuild the bundled npm stuff. We don't have network. Just use the shipped bundle.
sed -i '/def _build_paneljs/ a \    return' setup.py

%build
%python_build

%if ! %{with test}
%install
%python_install

%{python_expand  # FIX HASHBANG AND LINK EXAMPLES INTO PACKAGE DOCS
mkdir examples-%{$python_bin_suffix}
ln -s %{$python_sitelib}/%{modname}/examples examples-%{$python_bin_suffix}/examples
sed -i "1{s|#!/usr/bin/env python|#!%{__$python}|}" \
  %{buildroot}%{$python_sitelib}/%{modname}/examples/apps/django2/manage.py \
  %{buildroot}%{$python_sitelib}/%{modname}/examples/apps/django_multi_apps/manage.py
}

%python_clone -a %{buildroot}%{_bindir}/panel

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# DISABLE TESTS REQUIRING NETWORK ACCESS
%pytest -rs -k 'not (test_loading_a_image_from_url or test_image_alt_text or test_image_link_url or test_vtk_pane_from_url or test_vtkjs_pane)'
%endif

%post
%python_install_alternative panel

%postun
%python_uninstall_alternative panel

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%doc examples-%{python_bin_suffix}/examples
%docdir %{python_sitelib}/%{modname}/examples
%python_alternative %{_bindir}/panel
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/
%endif

%changelog
