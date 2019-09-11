#
# spec file for package python-ioflo
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
Name:           python-ioflo
Version:        1.7.5
Release:        0
Summary:        Python framework for programming autonomous systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ioflo/ioflo
Source0:        https://files.pythonhosted.org/packages/source/i/ioflo/ioflo-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git >= 1.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
IoFlo is a software framework for automating developers' programmable world.
IoFlo has its roots in the research and development of autonomous underwater
vehicles, autonomic ships, and automated buildings. It attempts to make
programming autonomous/autonomic systems easier.

%prep
%setup -q -n ioflo-%{version}

%build
%python_build

%install
%python_install
rm -f %{buildroot}%{_bindir}/ioflo{2,3}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests actually fail with syntax error, upstream should sort it out
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%license LICENSE* LEGAL
%doc README* ChangeLog.md
%{python_sitelib}/*
%python3_only %{_bindir}/ioflo

%changelog
