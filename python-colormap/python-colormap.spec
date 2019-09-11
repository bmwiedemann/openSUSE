#
# spec file for package python-colormap
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-colormap
Version:        1.0.2
Release:        0
Summary:        Utilities to manipulate matplotlib colormaps and color codecs
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/cokelaer/colormap
Source:         https://files.pythonhosted.org/packages/source/c/colormap/colormap-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module easydev}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose-cov}
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-easydev
Requires:       python-matplotlib
BuildArch:      noarch

%python_subpackages

%description
The colormap package provides utilities to convert colors between
RGB, HEX, HLS, HUV and a class to build colormaps for matplotlib. All
matplotlib colormaps and some R colormaps are available altogether. The
plot_colormap method is able to pick up a colormaps and
the test_colormap can be used to visually test a new colormap.

%prep
%setup -q -n colormap-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
