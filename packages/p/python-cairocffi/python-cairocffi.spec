#
# spec file for package python-cairocffi
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-cairocffi
Version:        1.4.0
Release:        0
Summary:        Python cairo bindings based on cffi
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/cairocffi
Source:         https://files.pythonhosted.org/packages/source/c/cairocffi/cairocffi-%{version}.tar.gz
# https://github.com/Kozea/cairocffi/issues/208
Source1:        https://raw.githubusercontent.com/Kozea/cairocffi/master/LICENSE
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module cffi >= 1.1.0}
# we don't want pikepdf in Ring1 stagings
#BuildRequires:  %{python_module pikepdf}
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  %{python_module xcffib >= 0.3.2}
BuildRequires:  cairo
Requires:       cairo
Requires:       python-cffi >= 1.1.0
Requires:       python-xcffib >= 0.3.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
# /SECTION
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
%autosetup -n cairocffi-%{version} -p1
cp %{SOURCE1} .
# disable development tools for unit tests. Remove deprecated pytest-runner
sed -i -e 's/pytest-runner$/pytest/' \
       -e '/pytest-flake8$/ d' \
       -e '/pytest-isort$/ d' \
       -e '/pytest-cov$/ d' \
       -e '/^addopts.*flake8.*isort$/ d' setup.cfg

mkdir tests
mv cairocffi/test_*.py tests/
sed -i 's/^from \. /from cairocffi /' tests/*.py
sed -i 's/^from \./from cairocffi./' tests/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd tests/
# test_cairo.py needs pikepdf, remove it
rm test_cairo.py
# Switch off test_xcb_window (gh#Kozea/cairocffi#203)
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" xvfb-run --server-args="-screen 0 1280x1024x16" $python -m pytest -k "not test_xcb_window" *.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/cairocffi-%{version}*-info
%{python_sitelib}/cairocffi
%exclude %{python_sitelib}/cairocffi/pixbuf.py*
%ifpycache
%exclude %{python_sitelib}/cairocffi/__pycache__/pixbuf.*
%endif

%files %{python_files pixbuf}
%{python_sitelib}/cairocffi/pixbuf.py*
%ifpycache
%{python_sitelib}/cairocffi/__pycache__/pixbuf.*
%endif

%changelog
