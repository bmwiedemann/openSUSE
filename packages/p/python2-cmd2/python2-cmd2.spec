#
# spec file for package python2-cmd2
#
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python2-cmd2
Version:        0.8.9
Release:        0
Summary:        Extra features for standard library's cmd module
License:        MIT
Group:          Development/Languages/Python
URL:            http://packages.python.org/cmd2/
Source:         https://files.pythonhosted.org/packages/source/c/cmd2/cmd2-%{version}.tar.gz
BuildRequires:  python-contextlib2
BuildRequires:  python-enum34
BuildRequires:  python-mock
BuildRequires:  python-pyperclip
BuildRequires:  python-pytest-xdist
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
BuildRequires:  python-subprocess32
BuildRequires:  python-wcwidth
Requires:       python2-contextlib2
Requires:       python2-enum34
Requires:       python2-pyparsing >= 2.0.1
Requires:       python2-pyperclip
Requires:       python2-six
Requires:       python2-subprocess32
Requires:       python2-wcwidth
Provides:       python-cmd2 = %{version}-%{release}
Obsoletes:      python-cmd2 < %{version}-%{release}
BuildArch:      noarch

%description
Enhancements for standard library's cmd module.

Drop-in replacement adds several features for command-prompt tools:

    * Searchable command history (commands: "hi", "li", "run")
    * Load commands from file, save to file, edit commands in file
    * Multi-line commands
    * Case-insensitive commands
    * Special-character shortcut commands (beyond cmd's "@" and "!")
    * Settable environment parameters
    * Parsing commands with flags
    * > (filename), >> (filename) redirect output to file
    * < (filename) gets input from file
    * bare >, >>, < redirect to/from paste buffer
    * accepts abbreviated commands when unambiguous
    * `py` enters interactive Python console
    * test apps against sample session transcript (see example/example.py)

%prep
%setup -q -n cmd2-%{version}

%build
%py2_build

%install
%py2_install

%check
python2 setup.py test

%files
%license LICENSE
%doc CHANGELOG.md CODEOWNERS README.md
%{python2_sitelib}/*

%changelog
