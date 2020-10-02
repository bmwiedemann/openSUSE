#
# spec file for package python-pybtex
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oname   pybtex
Name:           python-pybtex
Version:        0.22.2
Release:        0
Summary:        BibTeX-compatible Bibliography Processor in Python
License:        MIT
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://pybtex.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pybtex/pybtex-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.0.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module latexcodec}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-latexcodec
Requires:       python-pyparsing
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
# install man
for man in %{oname} %{oname}-convert %{oname}-format ; do
  install -Dpm 0644 docs/man1/${man}.1 %{buildroot}%{_mandir}/man1/${man}.1
done
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}-format.1
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}-convert.1
%python_clone -a %{buildroot}%{_mandir}/man1/%{oname}.1
%python_clone -a %{buildroot}%{_bindir}/%{oname}-format
%python_clone -a %{buildroot}%{_bindir}/%{oname}-convert
%python_clone -a %{buildroot}%{_bindir}/%{oname}

%post
%python_install_alternative %{oname}-format.1
%python_install_alternative %{oname}-convert.1
%python_install_alternative %{oname}.1
%python_install_alternative %{oname}-format
%python_install_alternative %{oname}-convert
%python_install_alternative %{oname}

%postun
%python_uninstall_alternative %{oname}-format.1
%python_uninstall_alternative %{oname}-convert.1
%python_uninstall_alternative %{oname}.1
%python_uninstall_alternative %{oname}-format
%python_uninstall_alternative %{oname}-convert
%python_uninstall_alternative %{oname}

%files %{python_files}
%python_alternative %{_mandir}/man1/%{oname}-format.1%{ext_man}
%python_alternative %{_mandir}/man1/%{oname}-convert.1%{ext_man}
%python_alternative %{_mandir}/man1/%{oname}.1%{ext_man}
%python_alternative %{_bindir}/%{oname}-format
%python_alternative %{_bindir}/%{oname}-convert
%python_alternative %{_bindir}/%{oname}
%{python_sitelib}/*

%changelog
