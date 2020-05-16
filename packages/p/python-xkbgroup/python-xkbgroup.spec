#
# spec file for package python-xkbgroup
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-xkbgroup
Version:        0.2.0
Release:        0
Summary:        Query and change XKB layout state
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hcpl/xkbgroup
Source:         https://files.pythonhosted.org/packages/source/x/xkbgroup/xkbgroup-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       xorg-x11-server
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python library to query and change XKB layout state.

%prep
%setup -q -n xkbgroup-%{version}
sed -i 's/from \.xkb/from xkbgroup.xkb/' xkbgroup/core.py
sed -i 's/from xkb/from xkbgroup.xkb/' xkbgroup/test.py
sed -i 's/nonlocal/global/' xkbgroup/test.py

# https://github.com/hcpl/xkbgroup/issues/13 - issues on 32bit
# with _XData32 and _XRead32 which are unlikely to be commonly used
# xkbgroup/xkb.py is generated using python-ctypeslib with
# h2xml.py -c -o xkb.xml X11/Xlib.h X11/Xlibint.h X11/XKBlib.h
# xml2py.py -k defst -o xkb.py -l X11 xkb.xml
# ctypelib depends on gccxml which is no longer provided on openSUSE
# Regenerating using ctypeslib2 may be an option.
# https://github.com/hcpl/xkbgroup/issues/14
# Remove the problematic entries manually on all platforms
# for consistency in any breakage caused.
sed -Ei '/_X(Data|Read)32/d' xkbgroup/xkb.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/xkbgroup
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run $python xkbgroup/core.py
# pause between pythons to allow X to stop
sleep 5
xvfb-run %{buildroot}%{_bindir}/xkbgroup-%{python_version} get all_data
sleep 5
# Seg faults:
# xvfb-run $python xkbgroup/test.py
}

%post
%python_install_alternative xkbgroup

%postun
%python_uninstall_alternative xkbgroup

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/xkbgroup
%{python_sitelib}/*

%changelog
