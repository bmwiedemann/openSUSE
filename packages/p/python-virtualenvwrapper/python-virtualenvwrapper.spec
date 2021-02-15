#
# spec file for package python-virtualenvwrapper
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
%bcond_with test
%global pythons python3
Name:           python-virtualenvwrapper
Version:        4.8.4
Release:        0
Summary:        Enhancements to virtualenv
License:        MIT
Group:          Development/Languages/Python
URL:            https://virtualenvwrapper.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/v/virtualenvwrapper/virtualenvwrapper-%{version}.tar.gz
Patch0:         virtualenvwrapper-4.8.4-python_version.patch
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-stevedore
Requires:       python-virtualenv
Requires:       python-virtualenv-clone
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module stevedore}
BuildRequires:  %{python_module virtualenv-clone}
BuildRequires:  %{python_module virtualenv}
%endif
%python_subpackages

%description
virtualenvwrapper is a set of extensions to Ian Bicking's virtualenv
tool.  The extensions include wrappers for creating and deleting virtual
environments and otherwise managing your development workflow, making it
easier to work on more than one project at a time without introducing
conflicts in their dependencies.

1.  Organizes all of your virtual environments in one place.
2.  Wrappers for creating, copying and deleting environments, including
    user-configurable hooks.
3.  Use a single command to switch between environments.
4.  Tab completion for commands that take a virtual environment as
    argument.
5.  User-configurable hooks for all operations.
6.  Plugin system for more creating sharable extensions.

%prep
%setup -q -n virtualenvwrapper-%{version}
sed -i -e '1i#!/bin/sh' virtualenvwrapper.sh
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/virtualenvwrapper.sh %{buildroot}%{_bindir}/virtualenvwrapper
mv %{buildroot}%{_bindir}/virtualenvwrapper_lazy.sh %{buildroot}%{_bindir}/virtualenvwrapper_lazy

# Prepare for update-alternatives usage
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for p in virtualenvwrapper virtualenvwrapper_lazy ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

#%%check
#python3.6 -m venv --system-site-packages --without-pip venvwrapper-3.6
#sh tests/run_tests $PWD/venvwrapper-3.6

%post
%python_install_alternative virtualenvwrapper virtualenvwrapper_lazy

%postun
%python_uninstall_alternative virtualenvwrapper

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.es.rst README.ja.rst README.txt
%python_alternative %{_bindir}/virtualenvwrapper
%python_alternative %{_bindir}/virtualenvwrapper_lazy
%{python_sitelib}/*

%changelog
