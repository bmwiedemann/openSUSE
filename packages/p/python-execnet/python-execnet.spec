#
# spec file for package python-execnet
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


Name:           python-execnet
Version:        1.9.0
Release:        0
Summary:        Rapid multi-Python deployment
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/pytest-dev/execnet
Source0:        https://files.pythonhosted.org/packages/source/e/execnet/execnet-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
execnet provides a share-nothing model with
channel-send/receive communication for distributing
execution across many Python interpreters across version,
platform and network barriers. It has a minimal and fast
API targetting the following uses:

 * distribute tasks to (many) local or remote CPUs
 * write and deploy hybrid multi-process applications
 * write scripts to administer multiple environments

%prep
%setup -q -n execnet-%{version}
sed -i "1d" execnet/script/shell.py execnet/script/socketserver.py

%build
%python_build
# fix non-executable-script error
sed -i "1d" execnet/script/shell.py execnet/script/socketserver.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -r s -k"not test_gateway" testing

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/execnet
%{python_sitelib}/execnet-%{version}-py%{python_version}.egg-info

%changelog
