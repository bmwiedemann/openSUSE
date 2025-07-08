#
# spec file for package python-html2text
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
%define upname html2text
%{?sle15_python_module_pythons}
Name:           python-%{upname}
Version:        2025.4.15
Release:        0
Summary:        Python script for turning HTML into Markdown text
License:        GPL-3.0-only
URL:            https://github.com/Alir3z4/html2text/
Source:         https://files.pythonhosted.org/packages/source/h/%{upname}/%{upname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Provides:       html2text = %{version}-%{release}
Obsoletes:      html2text < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
html2text is a Python script that converts a page of HTML into
Markdown (a text-to-HTML format).

%prep
%setup -q -n %{upname}-%{version}
# remove useless shebang
sed -i '/^#!/d' %{upname}/__init__.py

# remove executable bits from egg files
rm -r *.egg-info/

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/%{upname}

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative html2text

# post and postun macro call is not needed with only libalternatives

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md AUTHORS.rst ChangeLog.rst
%python_alternative %{_bindir}/%{upname}
%{python_sitelib}/html2text
%{python_sitelib}/html2text-%{version}.dist-info

%changelog
