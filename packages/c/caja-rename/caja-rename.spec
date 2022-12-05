#
# spec file for package caja-rename
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


%define pythons python3
# Compatibility with *SUSE 15.
%if 0%{?suse_version} && 0%{?suse_version} < 1550
%define python_compileall \
%{python_expand for d in %{buildroot}%{$python_sitelib} %{buildroot}%{$python_sitearch}; do \
  if [ -d $d ]; then \
    find $d -name '*.pyc' -delete; \
    $python -m compileall $d; \
    $python -O -m compileall $d; \
  fi; \
done \
} \
%{nil}
%endif
%define _name   cajarename
Name:           caja-rename
Version:        22.10.31
Release:        0
Summary:        Batch renaming extension for Caja
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/tari01/caja-rename
Source0:        https://github.com/tari01/caja-rename/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module polib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
# For directory owning.
# Note that we cannot use python_module here. The package doesn't provide a
# python3-caja virtual.
BuildRequires:  python-caja
BuildRequires:  python-rpm-macros
Requires:       caja
Requires:       python-caja
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
An extension for the Caja file browser allowing users to rename
multiple files/folders in a single pass.

The application can change the case, insert, replace and delete
strings, as well as enumerate the selection. Any changes are
instantly visible in the preview list. The user interface strives
to be as simple as possible, without confusing advanced
operations.

%lang_package

%prep
%setup -q

# Don't use env to call python.
%{python_expand sed -i -e 's_^#!%{_bindir}/env python3$_#!%{__$python}_' 'data/usr/share/caja-python/extensions/caja-rename.py' }

# Remove hashbangs on scripts installed into sitelib.
find '%{_name}' -type 'f' -iname '*.py' -exec sed -i -e '0,/^\s*#!\s*\/.*$/d' '{}' '+'

# Also remove executable flags.
find '%{_name}' -type 'f' -iname '*.py' -exec chmod -x '{}' '+'
chmod -x 'COPYING' 'README.md'
find 'data/usr/share/%{_name}' -type 'f' -exec chmod -x '{}' '+'

%build
%python_build

%install
%python_install
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%find_lang %{_name}

%files
%license COPYING
%doc README.md
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-%{version}*-info
%{_datadir}/caja-python/extensions/%{name}.py
%{_datadir}/%{_name}/
%pycache_only %{python_sitelib}/%{_name}/__pycache__/*

%files lang -f %{_name}.lang

%changelog
