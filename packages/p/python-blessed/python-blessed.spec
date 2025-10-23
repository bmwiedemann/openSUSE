#
# spec file for package python-blessed
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-blessed
Version:        1.22.0
Release:        0
Summary:        Wrapper around terminal styling, screen positioning, and keyboard input
License:        MIT
URL:            https://github.com/jquast/blessed
Source:         https://files.pythonhosted.org/packages/source/b/blessed/blessed-%{version}.tar.gz
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth >= 0.1.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-curses
Requires:       python-wcwidth >= 0.1.4
BuildArch:      noarch
%python_subpackages

%description
Blessed is a thin, practical wrapper around terminal capabilities in Python.

Brief Overview
--------------

*Blessed* is a more simplified wrapper around curses, providing :

* Styles, color, and maybe a little positioning without necessarily
  clearing the whole screen first.
* Works great with standard Python string formatting.
* Provides up-to-the-moment terminal height and width, so you can respond to
  terminal size changes.
* Avoids making a mess if the output gets piped to a non-terminal:
  outputs to any file-like object such as *StringIO*, files, or pipes.
* Uses the `terminfo(5)`_ database so it works with any terminal type
  and supports any terminal capability: No more C-like calls to tigetstr_
  and tparm_.
* Keeps a minimum of internal state, so you can feel free to mix and match with
  calls to curses or whatever other terminal libraries you like.
* Provides plenty of context managers to safely express terminal modes,
  automatically restoring the terminal to a safe state on exit.
* Act intelligently when somebody redirects your output to a file, omitting
  all of the terminal sequences such as styling, colors, or positioning.
* Dead-simple keyboard handling: safely decoding unicode input in your
  system's preferred locale and supports application/arrow keys.
* Allows the printable length of strings containing sequences to be
  determined.

Blessed **does not** provide...

* Windows command prompt support.  A PDCurses_ build of python for windows
  provides only partial support at this time -- there are plans to merge with
  the ansi module in concert with colorama to resolve this.

%prep
%autosetup -p1 -n blessed-%{version}
# disable cons25 tests as they fail in OBS
sed -i -e 's:cons25 ::' tests/accessories.py
# do not pull extra deps that are not needed
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export TEST_QUICK=1
%pytest tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/blessed
%{python_sitelib}/blessed-%{version}*-info

%changelog
