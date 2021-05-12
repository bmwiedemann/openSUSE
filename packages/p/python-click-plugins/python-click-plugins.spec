#
# spec file for package python-click-plugins
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{?sle_version} == 150300
# tests fail on python2 on Leap 15.3 and SLE 15 SP3
%define skip_python2 1
%endif
Name:           python-click-plugins
Version:        1.1.1
Release:        0
Summary:        Click extension to register CLI commands via setuptools entry-points
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/click-contrib/click-plugins
Source:         https://files.pythonhosted.org/packages/source/c/click-plugins/click-plugins-%{version}.tar.gz
BuildRequires:  %{python_module click >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 3.0
BuildArch:      noarch
%python_subpackages

%description
Use a decorator to get setuptools entry points that allows others
to use your commandline utility as a home for their related sub-commands.
You get to choose where these sub-commands or sub-groups can be registered
but the plugin developer gets to choose they ARE registered.
You could have all plugins register alongside the core commands,
in a special sub-group, across multiple sub-groups, or some combination.

%prep
%setup -q -n click-plugins-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc AUTHORS.txt CHANGES.md README.rst
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%%license LICENSE.txt
%else
%license LICENSE.txt
%endif
%{python_sitelib}/*

%changelog
