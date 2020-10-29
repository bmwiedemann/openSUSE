#
# spec file for package python-urwid
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
Name:           python-urwid
Version:        2.1.1
Release:        0
Summary:        A full-featured console (xterm et al.) user interface library
License:        LGPL-2.1-or-later
URL:            http://urwid.org
Source:         https://files.pythonhosted.org/packages/source/u/urwid/urwid-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-curses
%python_subpackages

%description
Urwid is a console user interface library.  It includes many features
useful for text console application developers including:
- Applications resize quickly and smoothly
- Automatic, programmable text alignment and wrapping
- Simple markup for setting text attributes within blocks of text
- Powerful list box with programmable content for scrolling all widget types
- Your choice of event loops: Twisted, Glib or built-in select-based loop
- Pre-built widgets include edit boxes, buttons, check boxes and radio buttons
- Display modules include raw, curses, and experimental LCD and web displays
- Support for UTF-8, simple 8-bit and CJK encodings
- 256 and 88 color mode support
- Python 3.2 support

%prep
%setup -q -n "urwid-%{version}"
# remove unwanted shebang
find urwid -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# this test won't work on OBS
rm -f urwid/tests/test_vterm.py
%python_exec setup.py -q test

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/urwid/
%{python_sitearch}/urwid-%{version}-py%{python_version}.egg-info

%changelog
