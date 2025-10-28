#
# spec file for package python-Pygments
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-Pygments%{psuffix}
Version:        2.19.2
Release:        0
Summary:        A syntax highlighting package written in Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://pygments.org
Source:         https://files.pythonhosted.org/packages/source/p/pygments/pygments-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-wcag-contrast-ratio.patch gh#pygments/pygments!2564 mcepl@suse.com
# Don't make wcag-contrast-ratio mandatory for testing
Patch0:         skip-wcag-contrast-ratio.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module pytest >= 7}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
#!BuildIgnore:  ca-certificates:p11-kit
#!BuildIgnore:  ca-certificates:p11-kit-tools
Provides:       python-pygments = %{version}
Obsoletes:      python-pygments < %{version}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%autosetup -n pygments-%{version} -p1
# Remove unneeded executable bit
chmod -x pygments/formatters/_mapping.py pygments/lexers/gsql.py

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
install -Dm0644 doc/pygmentize.1 %{buildroot}%{_mandir}/man1/pygmentize.1
%python_clone -a %{buildroot}%{_bindir}/pygmentize
%python_clone -a %{buildroot}%{_mandir}/man1/pygmentize.1
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
# skip test_guess_lexer_modula2 as we have to remove it's depent artifacts
# in exmplefiles because of potential licensing concerns
# See https://github.com/pygments/pygments/issues/2872
# skip random input tests as they get stuck (missing entropy?)
# test_lexer_classes breaks with pytest 8.4.
%pytest -k "not (test_guess_lexer_modula2 or test_random_input or test_lexer_classes)"
%endif

%if !%{with test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pygmentize

%post
%{python_install_alternative pygmentize pygmentize.1}

%postun
%python_uninstall_alternative pygmentize

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES
%python_alternative %{_bindir}/pygmentize
%python_alternative %{_mandir}/man1/pygmentize.1%{ext_man}
%{python_sitelib}/pygments
%{python_sitelib}/pygments-%{version}*-info
%endif

%changelog
