#
# spec file for package python2-cairocffi
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
%define         skip_python3 1
Name:           python2-cairocffi
Version:        0.9.0
Release:        0
Summary:        Python cairo bindings based on cffi
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/SimonSapin/cairocffi
Source:         https://files.pythonhosted.org/packages/source/c/cairocffi/cairocffi-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xcffib >= 0.3.2}
BuildRequires:  cairo
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf
BuildRequires:  python-rpm-macros
Requires:       cairo
Requires:       python
Requires:       python-cffi >= 0.6
Requires:       python-xcffib >= 0.3.2
BuildArch:      noarch
%python_subpackages

%description
cairocffi is a CFFI-based drop-in replacement for Pycairo,
a set of Python bindings and object-oriented API for cairo.
Cairo is a 2D vector graphics library with support for multiple backends
including image buffers, PNG, PostScript, PDF, and SVG file output.

%package pixbuf
Summary:        Python cairo bindings based on cffi - pixbuf image loader
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       gdk-pixbuf

%description pixbuf
cairocffi is a CFFI-based drop-in replacement for Pycairo,
a set of Python bindings and object-oriented API for cairo.
Cairo is a 2D vector graphics library with support for multiple backends
including image buffers, PNG, PostScript, PDF, and SVG file output.

This package provides the optional gdk-pixbuf image loader module.

%prep
%setup -q -n cairocffi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch} 

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/cairocffi-%{version}-py*.egg-info
%{python_sitelib}/cairocffi/
%exclude %{python_sitelib}/cairocffi/test_pixbuf.py*
%exclude %{python_sitelib}/cairocffi/pixbuf.py*

%files %{python_files pixbuf}
%{python_sitelib}/cairocffi/pixbuf.py*
%{python_sitelib}/cairocffi/test_pixbuf.py*

%changelog
