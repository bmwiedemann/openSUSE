#
# spec file for package python-cauldron-notebook
#
# Copyright (c) 2024 SUSE LLC
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


%define         skip_python39 1
Name:           python-cauldron-notebook
Version:        1.0.9
Release:        0
Summary:        Scientific Analysis Environment
License:        MIT
URL:            https://github.com/sernst/cauldron
Source:         https://github.com/sernst/cauldron/archive/v%{version}.tar.gz#/cauldron-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-Jinja2
Requires:       python-Markdown
Requires:       python-beautifulsoup4
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-pygments
Requires:       python-requests
Requires:       python-waitress
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-bokeh
Recommends:     python-matplotlib
Recommends:     python-plotly
Recommends:     python-seaborn
Provides:       python-cauldron_notebook = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module seaborn}
BuildRequires:  %{python_module waitress}
# /SECTION
%python_subpackages

%description
Interactive computing for complex data processing,
modeling and analysis in Python.

%prep
%setup -q -n cauldron-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cauldron
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests only work on git repo
# %%check
# %%pytest

%post
%python_install_alternative cauldron

%postun
%python_uninstall_alternative cauldron

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/cauldron
%{python_sitelib}/cauldron
%{python_sitelib}/cauldron_notebook-%{version}.dist-info

%changelog
