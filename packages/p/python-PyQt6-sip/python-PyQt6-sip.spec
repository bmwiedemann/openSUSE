#
# spec file for package python-PyQt6-sip
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
Name:           python-PyQt6-sip
Version:        13.6.0
Release:        0
Summary:        The sip module support for PyQt6
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        https://files.pythonhosted.org/packages/source/P/PyQt6-sip/PyQt6_sip-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The sip extension module provides support for the PyQt6 package.

SIP is a tool for automatically generating Python bindings for
C and C++ libraries. SIP was originally developed in 1998 for
PyQt - the Python bindings for the Qt GUI toolkit - but is
suitable for generating bindings for any C or C++ library. SIP
can also be used write self contained extension modules, i.e.
without a library to be wrapped.

%prep
%autosetup -p1 -n PyQt6_sip-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python_sitearch}/PyQt6
%{python_sitearch}/PyQt6/sip*
%{python_sitearch}/PyQt6_sip-%{version}.dist-info

%changelog
