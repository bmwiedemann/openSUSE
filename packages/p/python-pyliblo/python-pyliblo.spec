# spec file for package python-pyliblo
#
# Copyright (c) 2019 Fabio Pesari
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:          python-pyliblo
Version:       0.10.0
Release:       0
Summary:       Python bindings for the liblo Open Sound Control (OSC) library
License:       LGPL-2.1+
Group:         Development/Languages/Python
URL:           http://das.nasophon.de/pyliblo/
Source0:       pyliblo-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: %{python_module devel}
BuildRequires: %{python_module Cython}
BuildRequires: liblo-devel

%description
pyliblo is a Python wrapper for the liblo OSC library. 
It supports almost the complete functionality of liblo, 
allowing you to send and receive OSC messages using a nice and simple Python API. 

%package -n pyliblo-tools
Summary:        Tools for python-pyliblo
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{python_module pyliblo} = %{version}

%description -n pyliblo-tools
This package contains command-line tools from python-pyliblo.

%package doc
Summary:        Documentation for python-pyliblo
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
This package contains HTML documentation, including tutorials and API
reference for python-pyliblo.


%python_subpackages

%prep
%setup -q -n pyliblo-%{version}
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README NEWS
%license COPYING
%{python_sitearch}/liblo*
%{python_sitearch}/pyliblo-*.egg-info

%files %{python_files doc}
%doc doc/
%doc examples/

%files -n pyliblo-tools
%{_bindir}/dump_osc
%{_bindir}/send_osc
%_mandir/*/*

%changelog