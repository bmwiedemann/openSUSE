#
# spec file for package python-TermRecord
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
Name:           python-TermRecord
Version:        1.2.5
Release:        0
Summary:        A terminal session recorder with HTML output
License:        MIT
URL:            https://github.com/theonewolf/TermRecord
Source:         https://files.pythonhosted.org/packages/source/T/TermRecord/TermRecord-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Jinja2 >= 2.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.6}
# /SECTION
%python_subpackages

%description
TermRecord is a program that wraps the `script` command. It automagically
detects the terminal size, records the session, and stores the output as
either JSON, embeddable JavaScript, or a static HTML file.  The HTML is
self-contained, embedding all necessary dependencies in one file so that
it can be shipped to anyone that has a browser. Fonts are embedded, too.

%prep
%setup -q -n TermRecord-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/TermRecord

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative TermRecord

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/TermRecord
%{python_sitelib}/[Tt]erm[Rr]ecord
%{python_sitelib}/[Tt]erm[Rr]ecord-%{version}*-info

%changelog
