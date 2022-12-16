#
# spec file for package python-enaml
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


Name:           python-enaml
Version:        0.15.2
Release:        0
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
Summary:        Declarative DSL for building rich user interfaces in Python
License:        BSD-3-Clause AND LGPL-2.1-only
URL:            https://github.com/nucleic/enaml
Source:         https://files.pythonhosted.org/packages/source/e/enaml/enaml-%{version}.tar.gz
BuildRequires:  %{python_module cppy >= 1.2.0}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-atom >= 0.8.0
Requires:       python-bytecode >= 0.13.0
Requires:       python-kiwisolver >= 1.2.0
Requires:       python-ply
# SECTION The Qt variants are optional variants in the python metadata, but probably either one is required and they all require QtPy
Requires:       python-QtPy >= 2.1.0
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
# pyside is python3 only, PyQt5 (-qt5) and PyQt6 are multiflavored
Requires:       (python-qt5 or python-PyQt6 >= 6.3.1 or python3-pyside2 or python3-pyside6 >= 6.2.3)
%else
Requires:       (python-qt5 or python-PyQt6 >= 6.3.1)
%endif
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module QtPy >= 2.1.0}
BuildRequires:  %{python_module atom >= 0.8.0}
BuildRequires:  %{python_module bytecode >= 0.13.0}
BuildRequires:  %{python_module kiwisolver >= 1.2.0}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  xauth
BuildRequires:  xorg-x11-fonts
# /SECTION
%python_subpackages

%description
Enaml is a programming language and framework for creating
professional quality user interfaces with minimal effort.
Enaml combines a domain specific declarative language with
a constraints based layout system to allow users to easily
define rich UIs with complex and flexible layouts. Enaml
applications can be run on any platform which supports
Python and Qt.

%prep
%setup -q -n enaml-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/enaml-compileall
%python_clone -a %{buildroot}%{_bindir}/enaml-run

%check
# use the builddir instead of buildroot in order to avoid
# packaging of unreproducible files generated during tests
# https://github.com/nucleic/enaml/issues/397
%python_expand cp -r %{buildroot}%{$python_sitearch} build/testlib
export PYTHONPATH=$PWD/build/testlib
# See the skipif mark of the tests: 'Skip on linux CI where setting up a windows manager is a nightmare'
donttest="test_focus_tracking or test_focus_traversal"
%pytest_arch tests -k "not ($donttest)"

%post
%python_install_alternative enaml-compileall enaml-run

%postun
%python_uninstall_alternative enaml-compileall

%files %{python_files}
%doc README.rst releasenotes.rst
%license LICENSE
%python_alternative %{_bindir}/enaml-compileall
%python_alternative %{_bindir}/enaml-run
%{python_sitearch}/enaml
%{python_sitearch}/enaml-%{version}*-info

%changelog
