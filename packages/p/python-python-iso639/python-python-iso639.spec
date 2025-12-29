#
# spec file for package python-python-iso639
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


%{?sle15_python_module_pythons}
Name:           python-python-iso639
Version:        2025.11.16
Release:        0
Summary:        ISO 639 language codes, names, and other associated information
License:        Apache-2.0
URL:            https://github.com/jacksonllee/iso639
Source:         %{url}/archive/v%{version}.tar.gz#/python_iso639-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 65.3.0}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-iso639 is a Python package for ISO 639 language codes, names, and other
associated information.

Current features:

 * A representation of languages mapped across ISO 639-1, 639-2, and 639-3.
 * Functionality to "guess" what a language is for a given unknown language
   code or name.

%prep
%autosetup -p1 -n iso639-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/iso639
%{python_sitelib}/python_iso639-%{version}.dist-info

%changelog
