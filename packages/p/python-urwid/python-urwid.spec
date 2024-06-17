#
# spec file for package python-urwid
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
Name:           python-urwid
Version:        2.6.13
Release:        0
Summary:        A full-featured console (xterm et al.) user interface library
License:        LGPL-2.1-or-later
URL:            https://github.com/urwid/urwid
Source:         https://files.pythonhosted.org/packages/source/u/urwid/urwid-%{version}.tar.gz
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-curses
Requires:       python-typing_extensions
Requires:       python-wcwidth
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
%autosetup -p1 -n "urwid-%{version}"
# remove unwanted shebang
find urwid -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/urwid
%{python_sitelib}/urwid-%{version}.dist-info

%changelog
