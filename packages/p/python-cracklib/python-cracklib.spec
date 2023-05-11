#
# spec file for package python-cracklib
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


Name:           python-cracklib
Version:        2.9.6
Release:        0
Summary:        A CPython extension module wrapping the libcrack library
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/cracklib/cracklib
Source:         https://files.pythonhosted.org/packages/source/c/cracklib/cracklib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cracklib-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This CPython extension provides Python bindings for cracklib. It
contains a pythonic interface to cracklib's functions and some Python
convenience functions.

%prep
%setup -q -n cracklib-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%{python_sitearch}/*

%changelog
