#
# spec file for package python-enaml
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         X_display         ":98"
Name:           python-enaml
Version:        0.10.2
Release:        0
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause and LGPL-2.1
Summary:        Declarative DSL for building rich user interfaces in Python
Url:            https://github.com/nucleic/enaml
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/e/enaml/enaml-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module QtPy >= 1.3}
BuildRequires:  %{python_module atom >= 0.4.1}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module kiwisolver >= 1.0.0}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module setuptools}
BuildRequires:  xorg-x11-server
# /SECTION
Requires:       python-QtPy >= 1.3
Requires:       python-atom >= 0.4.1
Requires:       python-future
Requires:       python-kiwisolver >= 1.0.0
Requires:       python-ply >= 3.4
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/enaml-run

%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

export QT_HASH_SEED=0
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
py.test-%{$python_bin_suffix} tests
}

%post
%python_install_alternative enaml-run

%postun
%python_uninstall_alternative enaml-run

%files %{python_files}
%doc README.rst
%license COPYING.txt licenses/
%python_alternative %{_bindir}/enaml-run
%{python_sitearch}/*

%changelog
