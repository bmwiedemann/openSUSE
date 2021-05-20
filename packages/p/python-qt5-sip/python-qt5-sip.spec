#
# spec file for package python-qt5-sip
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-qt5-sip
Version:        12.9.0
Release:        0
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
Summary:        The sip module support for PyQt5
URL:            https://www.riverbankcomputing.com/software/sip/
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/P/PyQt5-sip/PyQt5_sip-%{version}.tar.gz
Source1:        https://www.riverbankcomputing.com/hg/sip/raw-file/tip/LICENSE
Source2:        https://www.riverbankcomputing.com/hg/sip/raw-file/tip/LICENSE-GPL2
Source3:        https://www.riverbankcomputing.com/hg/sip/raw-file/tip/LICENSE-GPL3
BuildRequires:  %pythons > 3.5
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools >= 30.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
The sip extension module provides support for the PyQt5 package.

SIP is a tool that makes it very easy to create Python bindings for
C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create
bindings for any C or C++ library. For example, it is also used to
create wxPython, the Python bindings for the wxWidget toolkit.

%prep
%setup -q -n PyQt5_sip-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/sip*
%{python_sitearch}/PyQt5_sip-%{version}*info

%changelog
