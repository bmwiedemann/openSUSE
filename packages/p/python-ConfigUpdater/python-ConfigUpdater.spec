#
# spec file for package python-ConfigUpdater
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
Name:           python-ConfigUpdater
Version:        3.1.1
Release:        0
Summary:        Parser like ConfigParser but for updating configuration files
License:        MIT
URL:            https://github.com/pyscaffold/configupdater
Source:         https://files.pythonhosted.org/packages/source/C/ConfigUpdater/ConfigUpdater-3.1.1.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  fdupes
Provides:       python-configupdater = %{version}-%{release}
%if %python_version_nodots < 38
Requires:       python-importlib-metadata
%endif

BuildArch:      noarch
%python_subpackages

%description
The sole purpose of this program is to easily update an INI config file
with no changes to the original file except the intended ones. This means
comments, the ordering of sections and key/value-pairs as wells as their
cases are kept as in the original file. Thus ConfigUpdater provides
complementary functionality to Python's ConfigParser which is primarily
meant for reading config files and writing new ones.

%prep
%setup -q -n ConfigUpdater-%{version}
sed -i '/--cov/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/configupdater
%{python_sitelib}/ConfigUpdater-%{version}*-info

%changelog

