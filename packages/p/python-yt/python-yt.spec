#
# spec file for package python-yt
#
# Copyright (c) 2023 SUSE LLC
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-yt
Version:        4.1.3
Release:        0
Summary:        An analysis and visualization toolkit for volumetric data
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/yt-project/yt
Source0:        https://files.pythonhosted.org/packages/source/y/yt/yt-%{version}.tar.gz
Source100:      python-yt-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy-devel >= 1.10.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-ipython >= 1.0
Requires:       python-matplotlib >= 2.0.2
Requires:       python-more-itertools >= 8.4
Requires:       python-numpy >= 1.10.4
Requires:       python-setuptools >= 19.6
Requires:       python-sympy >= 1.2
Requires:       python-toml >= 0.10.2
Requires:       python-tqdm >= 3.4.0
Requires:       python-unyt >= 2.7.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-bottle
Recommends:     python-girder-client
# SECTION test requirements
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module girder-client}
BuildRequires:  %{python_module ipython >= 1.0}
BuildRequires:  %{python_module matplotlib >= 2.0.2}
BuildRequires:  %{python_module sympy >= 1.2}
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
export CFLAGS="%{optflags} -freport-bug"
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitearch}/yt-%{version}*-info
%{python_sitearch}/yt

%changelog
