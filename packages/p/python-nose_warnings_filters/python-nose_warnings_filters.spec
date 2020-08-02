#
# spec file for package python-nose_warnings_filters
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
%bcond_without test
Name:           python-nose_warnings_filters
Version:        0.1.5
Release:        0
Summary:        Nose plugin to inject warning filters during nosetest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Carreau/nose_warnings_filters
Source:         https://files.pythonhosted.org/packages/source/n/nose_warnings_filters/nose_warnings_filters-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Carreau/nose_warnings_filters/0.1.1/LICENSE
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nose
BuildArch:      noarch
%python_subpackages

%description
This python-nose plugin works by putting the same arguments as
`warnings.filterwarnings` into `setup.cfg` at the root of a project,
separated each argument by pipes `|`, one filter per line. Whitespace
are stripped.

nose can be told to load a differently named configuration files
with `nosetests -c`.

%prep
%setup -q -n nose_warnings_filters-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
