#
# spec file for package python-Pygments
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Pygments
Version:        2.7.2
Release:        0
Summary:        A syntax highlighting package written in Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://pygments.org
Source:         https://files.pythonhosted.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
# We need pytest just because of its test runner, it seems even
# python3 stdlib unittest runner doesn't work
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pygments = %{version}
Obsoletes:      python-pygments < %{version}
BuildArch:      noarch
%python_subpackages

%description
Pygments is a generic syntax highlighter for general use in all kinds of software
such as forum systems, wikis or other applications that need to prettify
source code. Highlights are:

 * a wide range of common languages and markup formats is supported
 * support for new languages and formats can be added
 * a number of output formats, presently HTML, LaTeX, RTF, SVG, all image
   formats that PIL supports and ANSI sequences
 * it is usable as a command-line tool and as a library
 * highlights Brainfuck

%prep
%setup -q -n Pygments-%{version}

# Remove non-oss licensed files, see bnc# 760344
rm tests/examplefiles/firefox.mak tests/examplefiles/example.webidl

# Remove unnecessary executable bit
find . -type f -print0 | xargs -0 chmod -x

%build
%python_build

%install
%python_install
install -Dm0644 doc/pygmentize.1 %{buildroot}%{_mandir}/man1/pygmentize.1
%python_clone -a %{buildroot}%{_bindir}/pygmentize
%python_clone -a %{buildroot}%{_mandir}/man1/pygmentize.1
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%fdupes %{buildroot}%{$python_sitelib}
}

%prepare_alternative pygmentize

%post
%{python_install_alternative pygmentize pygmentize.1}

%postun
%python_uninstall_alternative pygmentize

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES
%python_alternative %{_bindir}/pygmentize
%python_alternative %{_mandir}/man1/pygmentize.1%{ext_man}
%{python_sitelib}/pygments/
%{python_sitelib}/Pygments-%{version}-py%{python_version}.egg-info/

%changelog
