#
# spec file for package python-stem
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
%define skip_python2 1
Name:           python-stem
Version:        1.7.1
Release:        0
Summary:        Python controller library for Tor
License:        LGPL-3.0-only
URL:            https://stem.torproject.org/
Source:         https://files.pythonhosted.org/packages/source/s/stem/stem-%{version}.tar.gz
Patch0:         python38.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Stem is a Python controller library that allows applications
to interact with Tor (https://www.torproject.org/).

%prep
%setup -q -n stem-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec run_tests.py -u

%files %{python_files}
%license LICENSE
%python3_only %{_bindir}/tor-prompt
%{python_sitelib}/*

%changelog
