#
# spec file for package python-Trololio
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


Name:           python-Trololio
Version:        1.0
Release:        0
Summary:        Trollius and asyncio compatibility library
License:        MIT
URL:            https://github.com/ThinkChaos/Trololio
Source:         https://files.pythonhosted.org/packages/source/T/Trololio/Trololio-%{version}.zip
# License file from source repository
Source1:        https://raw.githubusercontent.com/ThinkChaos/Trololio/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%ifpython2
Requires:       python2-trollius
%endif
%python_subpackages

%description
Trololio provides a compatibility layer for Trollius and asyncio (aka Tulip).
It addresses the differences listed in Trollius and Tulip:

* Allows the use of Trollius' syntax with asyncio.
* Provides missing objects and aliases for the others.
* Synchronizes debug environnement variables.

%prep
%setup -q -n Trololio-%{version}

# Install license into source tree
cp %{SOURCE1} LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/trololio.py
%{python_sitelib}/[Tt]rololio-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/trololio*
%doc README.rst
%license LICENSE

%changelog
