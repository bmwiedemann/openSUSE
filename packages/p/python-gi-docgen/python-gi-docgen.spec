#
# spec file for package python-gi-docgen
#
# Copyright (c) 2022 SUSE LLC
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


%define pythons python3
Name:           python-gi-docgen
Version:        2022.2
Release:        0
Summary:        Documentation tool for GObject-based libraries
License:        Apache-2.0 AND GPL-3.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/ebassi/gi-docgen
Source:         https://files.pythonhosted.org/packages/source/g/gi-docgen/gi-docgen-%{version}.tar.gz

BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module typogrify}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Jinja2
Requires:       python-Markdown > 3.2.0
Requires:       python-MarkupSafe
Requires:       python-Pygments
Requires:       python-toml
Requires:       python-typogrify
Suggests:       python-coverage
Suggests:       python-green
Obsoletes:      python38-gi-docgen < %{version}
BuildArch:      noarch
%python_subpackages

%description
Documentation tool for GObject-based libraries

%prep
%autosetup -n gi-docgen-%{version} -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gi-docgen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gi-docgen

%postun
%python_uninstall_alternative gi-docgen

%files %{python_files}
%doc README.md
%license LICENSES LICENSES/Apache-2.0.txt LICENSES/GPL-3.0-or-later.txt
%python_alternative %{_bindir}/gi-docgen
%{python_sitelib}/*
%{_mandir}/man1/gi-docgen.1%{?ext_man}
%{_datadir}/pkgconfig/gi-docgen.pc

%changelog
