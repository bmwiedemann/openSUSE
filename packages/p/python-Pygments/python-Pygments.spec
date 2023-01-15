#
# spec file for package python-Pygments
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


#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-Pygments
Version:        2.14.0
Release:        0
Summary:        A syntax highlighting package written in Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://pygments.org
Source:         https://files.pythonhosted.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcag-contrast-ratio}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
# Preferred for plugin loading, see https://pygments.org/docs/plugins/
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
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
%autosetup -n Pygments-%{version} -p1

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

%check
# skip test that requires wcag-contrast-ratio Python package
%pytest

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
%{python_sitelib}/Pygments-%{version}*-info

%changelog
