#
# spec file for package python-pathvalidate
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pathvalidate
Version:        2.2.2
Release:        0
Summary:        Python library to sanitize/validate a string such as filenames
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/pathvalidate
Source:         https://files.pythonhosted.org/packages/source/p/pathvalidate/pathvalidate-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module allpairspy}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 38.3.0}
# /SECTION
Requires:       python-setuptools >= 38.3.0
BuildArch:      noarch
%python_subpackages

%description
pathvalidate is a Python library to sanitize/validate a string such as
filenames/file-paths/etc.

%prep
%setup -q -n pathvalidate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pathvalidate*

%changelog
