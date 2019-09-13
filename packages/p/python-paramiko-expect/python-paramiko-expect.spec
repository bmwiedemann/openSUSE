#
# spec file for package python-paramiko-expect
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-paramiko-expect
Version:        0.2.8
Release:        0
Summary:        An expect-like extension for the Paramiko SSH library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/fgimian/paramiko-expect
Source:         https://files.pythonhosted.org/packages/source/p/paramiko-expect/paramiko-expect-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/fgimian/paramiko-expect/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-paramiko >= 1.10.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module contextlib2}
BuildRequires:  %{python_module paramiko >= 1.10.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-mock
# /SECTION
%python_subpackages

%description
Paramiko Expect provides an expect-like extension for the Paramiko SSH library
which allows scripts to fully interact with hosts via a true SSH
connection.

The class is constructed with an SSH Client object (this will likely be
extended to support a transport in future for more flexibility).

%prep
%setup -q -n paramiko-expect-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Needs running ssh server with properly set keys
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
