#
# spec file for package python-bokcolmaps
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
%define         skip_python2 1
Name:           python-bokcolmaps
Version:        1.0.0
Release:        0
Summary:        Colourmap plots based on the Bokeh visualisation library
License:        MIT
URL:            https://bitbucket.org/sea_dev/bokcolmaps
Source:         https://files.pythonhosted.org/packages/source/b/bokcolmaps/bokcolmaps-%{version}.tar.gz
# Will hopefully be included in next release, see https://bitbucket.org/sea_dev/bokcolmaps/pull-requests/1/include-license-in-sdists/diff
Source10:       https://bitbucket.org/sea_dev/bokcolmaps/raw/0a6f3852821bc033779a8f9392d984ea304f3ef7/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 0.12.13
Requires:       python-numpy >= 1.13
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module bokeh >= 0.12.13}
BuildRequires:  %{python_module numpy >= 1.13}
# /SECTION
%python_subpackages

%description
Colourmap plots based on the Bokeh visualisation library

%prep
%setup -q -n bokcolmaps-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/bokcolmaps/jet.txt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -B -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
