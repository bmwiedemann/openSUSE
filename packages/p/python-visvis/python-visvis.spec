#
# spec file for package python-visvis
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


%{?sle15_python_module_pythons}
Name:           python-visvis
Version:        1.14.0
Release:        0
Summary:        An object oriented approach to visualization of 1D to 4D data
License:        BSD-3-Clause
URL:            https://github.com/almarklein/visvis
Source:         https://files.pythonhosted.org/packages/source/v/visvis/visvis-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#almarklein/visvis#128
Patch0:         use-importlib.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-opengl
Requires:       python-qt5
Recommends:     python-Pillow
Recommends:     python-imageio
Recommends:     python-scikit-image
Recommends:     python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module scikit-image}
# /SECTION
%python_subpackages

%description
Visvis is a Python library for visualization of 1D to 4D data in an
object oriented way. Essentially, visvis is an object oriented layer
of Python on top of OpenGl. A Matlab/Matplotlib-like interface in the
form of a set of functions allows creation of objects (e.g. plot(),
imshow(), volshow(), surf()).

%prep
%autosetup -p1 -n visvis-%{version}
find * -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license license.txt
%{python_sitelib}/visvis
%{python_sitelib}/visvis-%{version}.dist-info

%changelog
