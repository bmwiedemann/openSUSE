#
# spec file for package python-ioflo
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
Name:           python-ioflo
Version:        2.0.0
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
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
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
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/ioflo

%check
%pytest

%post
%python_install_alternative ioflo

%postun
%python_uninstall_alternative ioflo

%files %{python_files}
%license LICENSE* LEGAL
%doc README* ChangeLog.md
%{python_sitelib}/*
%python_alternative %{_bindir}/ioflo
%{_bindir}/ioflo3

%changelog
