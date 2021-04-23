#
# spec file for package python-empy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-empy
Version:        3.3.4
Release:        0
License:        LGPL-2.1-or-later
Summary:        A templating system for Python
Url:            http://www.alcyone.com/software/empy
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/e/empy/empy-%{version}.tar.gz
Source1:        https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
EmPy is a system for embedding Python expressions and statements
in template text; it takes an EmPy source file, processes it, and
produces output.  This is accomplished via expansions, which are
special signals to the EmPy system and are set off by a special
prefix (by default the at sign, '@').  EmPy can expand arbitrary
Python expressions and statements in this way, as well as a
variety of special forms.  Textual data not explicitly delimited
in this way is sent unaffected to the output, allowing Python to
be used in effect as a markup language.  Also supported are "hook"
callbacks, recording and playback via diversions, and dynamic,
chainable filters.  The system is highly configurable via command
line options and embedded commands.

%prep
%setup -q -n empy-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license lgpl-2.1.txt
%doc README
%{python_sitelib}/*

%changelog
