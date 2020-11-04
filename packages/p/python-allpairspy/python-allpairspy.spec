#
# spec file for package python-allpairspy
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-allpairspy
Version:        2.5.0
Release:        0
License:        MIT
Summary:        Pairwise test combinations generator
Url:            https://github.com/thombashi/allpairspy
Group:          Development/Languages/Python
Source:         https://github.com/thombashi/allpairspy/archive/v%{version}.tar.gz#/allpairspy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six >= 1.10.0
Suggests:       python-twine
Suggests:       python-wheel
Suggests:       python-releasecmd >= 0.0.18
Suggests:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Pairwise test combinations generator.

%prep
%setup -q -n allpairspy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/allpairspy*

%changelog
