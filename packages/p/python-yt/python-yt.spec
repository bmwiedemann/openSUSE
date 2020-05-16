#
# spec file for package python-yt
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
%define         skip_python2 1
Name:           python-yt
Version:        3.5.1
Release:        0
Summary:        An analysis and visualization toolkit for volumetric data
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/yt-project/yt
Source0:        https://files.pythonhosted.org/packages/source/y/yt/yt-%{version}.tar.gz
Source100:      python-yt-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy-devel >= 1.10.4}
BuildRequires:  %{python_module setuptools >= 19.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 1.5.3
Requires:       python-numpy >= 1.10.4
Requires:       python-setuptools >= 19.6
Requires:       python-sympy >= 1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-bottle
Recommends:     python-girder-client
Recommends:     python-jupyter_ipython >= 1.0
# SECTION test requirements
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module girder-client}
BuildRequires:  %{python_module jupyter_ipython >= 1.0}
BuildRequires:  %{python_module matplotlib >= 1.5.3}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module sympy >= 1.0}
# /SECTION
%python_subpackages

%description
YT is an python package for analyzing and visualizing volumetric
data.  YT supports structured, variable-resolution meshes,
unstructured meshes, and discrete or sampled data such as particles.

%prep
%setup -q -n yt-%{version}
sed -i -e '/^#!\//, 1d' yt/utilities/lodgeit.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/yt
%python_clone -a %{buildroot}%{_bindir}/iyt
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative yt
%python_install_alternative iyt

%postun
%python_uninstall_alternative yt
%python_uninstall_alternative iyt

%files %{python_files}
%doc README.md
%license COPYING.txt
%python_alternative %{_bindir}/iyt
%python_alternative %{_bindir}/yt
%{python_sitearch}/*

%changelog
