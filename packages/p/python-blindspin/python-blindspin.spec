#
# spec file for package python-blindspin
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
Name:           python-blindspin
Version:        2.0.1
Release:        0
Summary:        Braille Spinner for Click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kennethreitz/blindspin
Source:         https://github.com/not-kennethreitz/blindspin/archive/v%{version}.tar.gz#/blindspin-%{version}.tar.gz
BuildRequires:  %{python_module click-spinner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Recommends:     python-click-spinner
BuildArch:      noarch
%python_subpackages

%description
Braille Spinner for Click.

%prep
%setup -q -n blindspin-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
