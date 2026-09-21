#
# spec file for package python-pybtex
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define oname   pybtex
%bcond_without libalternatives
Name:           python-pybtex
Version:        0.26.1
Release:        0
Summary:        BibTeX-compatible Bibliography Processor in Python
License:        MIT
URL:            https://pybtex.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pybtex/pybtex-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.0.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module latexcodec}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML
Requires:       python-latexcodec
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
%autosetup -n %{oname}-%{version}
# make_charwidths.py is a build-time helper with a /usr/bin/env shebang
# (rpmlint E: env-script-interpreter); point it at the system python
sed -i '1s|^.*$|#!%{_bindir}/python3|' src/pybtex/charwidths/make_charwidths.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Upstream no longer ships prebuilt man pages (docs/generate_manpages.py
# needs the unpublished pybtex-doctools); regenerate them from --help
export PYTHONPATH=%{buildroot}%{python_sitelib}
for man in %{oname} %{oname}-convert %{oname}-format ; do
  help2man -N --version-string=%{version} --output=${man}.1 %{buildroot}%{_bindir}/${man}
  install -Dpm 0644 ${man}.1 %{buildroot}%{_mandir}/man1/${man}.1
done
unset PYTHONPATH
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}-format.1
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}-convert.1
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}.1
%python_clone -a %{buildroot}%{_bindir}/%{oname}-format
%python_clone -a %{buildroot}%{_bindir}/%{oname}-convert
%python_clone -a %{buildroot}%{_bindir}/%{oname}
%python_group_libalternatives %{oname}-format %{oname}-convert %{oname}

%check
%pytest

%pre
%python_libalternatives_reset_alternative %{oname}-format
%python_libalternatives_reset_alternative %{oname}-convert
%python_libalternatives_reset_alternative %{oname}

%files %{python_files}
%python_alternative %{_mandir}/man1/%{oname}-format.1%{ext_man}
%python_alternative %{_mandir}/man1/%{oname}-convert.1%{ext_man}
%python_alternative %{_mandir}/man1/%{oname}.1%{ext_man}
%python_alternative %{_bindir}/%{oname}-format
%python_alternative %{_bindir}/%{oname}-convert
%python_alternative %{_bindir}/%{oname}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info

%changelog
