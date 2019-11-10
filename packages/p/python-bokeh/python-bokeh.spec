#
# spec file for package python-bokeh
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
# Tests fail due to missing git data,
# and building the JS from source doesn't work
%bcond_with     tests
Name:           python-bokeh
Version:        1.4.0
Release:        0
Summary:        Statistical interactive HTML plots for Python
License:        BSD-3-Clause
URL:            https://github.com/bokeh/bokeh/
Source:         https://files.pythonhosted.org/packages/source/b/bokeh/bokeh-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.7}
BuildRequires:  %{python_module Pillow >= 4.0}
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module numpy >= 1.7.1}
BuildRequires:  %{python_module packaging >= 16.8}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module requests >= 1.2.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5.2}
BuildRequires:  %{python_module tornado >= 4.3}
BuildRequires:  fdupes
BuildRequires:  python-futures >= 3.0.3
BuildRequires:  python-rpm-macros
BuildConflicts: python-buildservice-tweak
Requires:       python-Jinja2 >= 2.7
Requires:       python-Pillow >= 4.0
Requires:       python-PyYAML >= 3.10
Requires:       python-numpy >= 1.7.1
Requires:       python-packaging >= 16.8
Requires:       python-python-dateutil >= 2.1
Requires:       python-requests >= 1.2.3
Requires:       python-six >= 1.5.2
Requires:       python-tornado >= 4.3
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-icalendar
Recommends:     python-networkx
Recommends:     python-pscript
Recommends:     python-vincent
BuildArch:      noarch
%if %{with tests}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module boto}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module jupyter_nbconvert}
BuildRequires:  %{python_module jupyter_nbformat}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pscript}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  chromedriver
%endif
%ifpython2
Requires:       python-futures >= 3.0.3
%endif
%python_subpackages

%description
Bokeh is a Python interactive visualization library that targets web
browsers for presentation. It provides concise construction of
graphics in the style of D3.js, and favors delivering this capability
with interactivity over large or streaming datasets.

%prep
%setup -q -n bokeh-%{version}
sed -i 's/\r$//' examples/app/apply_theme.py
sed -i 's/\r$//' examples/reference/models/Dash.py
sed -i 's/\r$//' examples/app/apply_theme.py
sed -i 's/\r$//' examples/reference/models/Dash.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/bokeh

# Remove hidden files
%python_expand mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-bokeh
%python_expand cp -r examples %{buildroot}%{_docdir}/%{$python_prefix}-bokeh/
%python_expand rm -rf examples %{buildroot}%{_docdir}/%{$python_prefix}-bokeh/examples/*/.ipynb_checkpoints
%python_expand rm -rf examples %{buildroot}%{_docdir}/%{$python_prefix}-bokeh/examples/*/*/.ipynb_checkpoints
%python_expand %fdupes %{buildroot}%{_docdir}/%{$python_prefix}-bokeh/

# Remove test and script files
%python_expand rm -rf %{buildroot}%{$python_sitelib}/scripts/
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/

%if %{with tests}
%check
rm -rf build _build.*
%{python_expand rm -rf build _build.*
py.test-%{$python_bin_suffix} -s -m js -rs
py.test-%{$python_bin_suffix} -m 'not (examples or js or integration)' --cov=bokeh --cov-config=bokeh/.coveragerc -rs
py.test-%{$python_bin_suffix} -m integration -rs -v
}
%endif

%post
%python_install_alternative bokeh

%preun
%python_uninstall_alternative bokeh

%files %{python_files}
%license LICENSE.txt
%{_docdir}/%{python_prefix}-bokeh
%python_alternative %{_bindir}/bokeh
%{python_sitelib}/bokeh/
%{python_sitelib}/bokeh-%{version}-py*.egg-info

%changelog
