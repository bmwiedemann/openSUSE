#
# spec file for package python-pybtex
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Guido Berhoerster.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oname   pybtex
Name:           python-pybtex
Version:        0.21
Release:        0
Summary:        BibTeX-compatible Bibliography Processor in Python
License:        MIT
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://pybtex.org/
Source0:        https://pypi.python.org/packages/82/59/d46b4a84faacd7c419cfc9a442b7940d6d625d127b83d83666e2a8b203d8/pybtex-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.0.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module latexcodec}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-latexcodec
Requires:       python-pyparsing
BuildArch:      noarch
%python_subpackages

%description
Pybtex is a BibTeX-compatible bibliography processor written in Python which
can produce formatted bibliographies in different, customizable formats. It
supports both native BibTeX style files and styles written in Python and
accepts BibTeX, BibTeXML, and a custom YAML-based bibligraphy input format and
can output LaTeX, HTML, and plain text.

Furthermore, Pybtex provides an interface for Python applications which need to
process the above formats.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# install man
for man in %{oname} %{oname}-convert %{oname}-format ; do
  install -Dpm 0644 docs/man1/${man}.1 %{buildroot}%{_mandir}/man1/${man}.1
done

%files %{python_files}
%python3_only %{_bindir}/%{oname}*
%python3_only %{_mandir}/man1/%{oname}.1%{ext_man}
%python3_only %{_mandir}/man1/%{oname}-convert.1%{ext_man}
%python3_only %{_mandir}/man1/%{oname}-format.1%{ext_man}
%{python_sitelib}/*

%changelog
