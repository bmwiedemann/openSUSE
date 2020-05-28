#
# spec file for package python-colorcet
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-colorcet
Version:        2.0.2
Release:        0
Summary:        Collection of perceptually uniform colormaps
License:        CC-BY-4.0
Group:          Development/Languages/Python
URL:            https://github.com/bokeh/colorcet
Source:         https://files.pythonhosted.org/packages/source/c/colorcet/colorcet-%{version}.tar.gz
BuildRequires:  %{python_module param >= 1.7.0}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-param >= 1.7.0
Requires:       python-pyct >= 0.4.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/colorcet
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative colorcet

%postun
%python_uninstall_alternative colorcet

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/colorcet
%{python_sitelib}/*

%changelog
