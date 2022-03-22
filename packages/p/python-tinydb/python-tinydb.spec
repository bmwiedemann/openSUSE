#
# spec file for package python-tinydb
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-tinydb
Version:        4.7.0
Release:        0
Summary:        A document-oriented database
License:        MIT
Group:          Productivity/Databases/Servers
URL:            https://github.com/msiemens/tinydb
Source:         https://files.pythonhosted.org/packages/source/t/tinydb/tinydb-%{version}.tar.gz
# https://github.com/msiemens/tinydb/issues/324
Source1:        https://github.com/msiemens/tinydb/archive/refs/tags/v%{version}.tar.gz#/tinydb-%{version}-gh.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
#BuildRequires:  %%{python_module typing-extensions >= 3.10 if %%python-base < 3.7}
%if 0%{suse_version} < 1550
# For submission to 15.4, which still has not the boolean rpm requirements support in prjconf
BuildRequires:  %{python_module typing-extensions >= 3.10}
%endif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 37
Requires:       python-typing-extensions >= 3.10
%endif
BuildArch:      noarch
%python_subpackages

%description
TinyDB is a document oriented database written in
pure Python and has no external dependencies.
The target are small apps that would be “blown away” by a SQL-DB or an
external database server.

%prep
%setup -q -n tinydb-%{version}
chmod a-x LICENSE
dos2unix LICENSE
# only extract tests, use the sdist for the rest. We could use poetry-core and the github archive only if it wasn't for SLE/Leap
tar -zx -C .. -f %{SOURCE1} tinydb-%{version}/tests

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tinydb
%{python_sitelib}/tinydb-%{version}*-info

%changelog
