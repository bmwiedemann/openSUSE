#
# spec file for package python-python-rpm-spec
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-rpm-spec
Version:        0.8
Release:        0
Summary:        Python module for parsing RPM spec files
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/bkircher/python-rpm-spec
Source0:        https://files.pythonhosted.org/packages/source/p/python-rpm-spec/python-rpm-spec-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-pyrpm
BuildArch:      noarch
%python_subpackages

%description
python-rpm-spec is a Python module for parsing RPM spec files. RPMs are build
from a package's sources along with a spec file. The spec file controls how the
RPM is built. This module allows you to parse spec files and gives you simple
access to various bits of information that is contained in the spec file.

%prep
%setup -q -n python-rpm-spec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand py.test-%{$python_bin_suffix} -vv tests

%files %{python_files}
%doc CHANGELOG* README*
%license LICENSE*
%{python_sitelib}/*

%changelog
