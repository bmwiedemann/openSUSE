#
# spec file for package python-empy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-empy
Version:        4.0
Release:        0
Summary:        A templating system for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://www.alcyone.com/software/empy
Source:         https://files.pythonhosted.org/packages/source/e/empy/empy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
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

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/em.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative em.py

%postun
%python_uninstall_alternative em.py

%files %{python_files}
%license LICENSE.md
%doc README.md
%python_alternative %{_bindir}/em.py
%{python_sitelib}/em*.py
%pycache_only %{python_sitelib}/__pycache__/em*
%{python_sitelib}/empy-%{version}*-info

%changelog
