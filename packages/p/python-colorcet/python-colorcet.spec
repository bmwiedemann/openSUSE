#
# spec file for package python-colorcet
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-colorcet
Version:        3.1.0
Release:        0
Summary:        Collection of perceptually uniform colormaps
License:        CC-BY-4.0
URL:            https://github.com/bokeh/colorcet
Source:         https://files.pythonhosted.org/packages/source/c/colorcet/colorcet-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm >= 6}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
colorcet is a collection of perceptually uniform colormaps
for use with Python plotting programs like bokeh, matplotlib,
holoviews, and datashader.

%prep
%setup -q -n colorcet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/colorcet
%{python_sitelib}/colorcet-%{version}.dist-info

%changelog
