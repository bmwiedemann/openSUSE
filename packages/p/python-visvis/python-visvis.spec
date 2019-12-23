#
# spec file for package python-visvis
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
Name:           python-visvis
Version:        1.12.2
Release:        0
Summary:        An object oriented approach to visualization of 1D to 4D data
License:        BSD-3-Clause
URL:            https://github.com/almarklein/visvis
Source:         https://files.pythonhosted.org/packages/source/v/visvis/visvis-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n visvis-%{version}
find * -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license license.txt
%{python_sitelib}/*

%changelog
