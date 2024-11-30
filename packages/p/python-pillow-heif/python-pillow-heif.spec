#
# spec file for package python-pillow-heif
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


Name:           python-pillow-heif
Version:        0.21.0
Release:        0
Summary:        Python interface for libheif library
License:        BSD-3-Clause
URL:            https://github.com/bigcat88/pillow_heif
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 9.5.0}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.8}
BuildRequires:  %{python_module sphinx-issues}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module sphinxcontrib-copybutton}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(aom) >= 3.3.0
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libheif) >= 1.18.2
Requires:       python-Pillow >= 9.5.0
Suggests:       python-pillow-heif-doc
%python_subpackages

%description
Python interface for libheif library

%prep
%autosetup -p1 -n pillow_heif-%{version}

%build
%pyproject_wheel

#docs
pushd docs
%make_build html
popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
rm docs/_build/html/.buildinfo
%fdupes docs/_build/html

%files %{python_files}
%doc docs/_build/html
%{python_sitearch}/pillow_heif
%{python_sitearch}/pillow_heif-%{version}.dist-info
%{python_sitearch}/_pillow_heif.cpython-*.so

%changelog
