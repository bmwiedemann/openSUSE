#
# spec file for package python-hatch
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hatch
Version:        0.23.0
Release:        0
Summary:        A modern project, package, and virtual env manager
License:        MIT OR Apache-2.0
URL:            https://github.com/ofek/hatch
Source:         https://files.pythonhosted.org/packages/source/h/hatch/hatch-%{version}.tar.gz
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module devel > 3.5}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip >= 9.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semver >= 2.7.8}
BuildRequires:  %{python_module setuptools >= 36.0.0}
BuildRequires:  %{python_module sortedcontainers >= 1.5.7}
BuildRequires:  %{python_module toml >= 0.9.3}
BuildRequires:  %{python_module twine >= 1.9.1}
BuildRequires:  %{python_module userpath >= 1.3.0}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel >= 0.27.0}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-appdirs
Requires:       python-atomicwrites
Requires:       python-click
Requires:       python-colorama
Requires:       python-coverage
Requires:       python-pexpect
Requires:       python-pip >= 9.0.1
Requires:       python-pytest
Requires:       python-semver >= 2.7.8
Requires:       python-setuptools >= 36.0.0
Requires:       python-sortedcontainers
Requires:       python-toml >= 0.9.3
Requires:       python-twine >= 1.9.1
Requires:       python-userpath >= 1.3.0
Requires:       python-virtualenv
Requires:       python-wheel >= 0.27.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Hatch is a productivity tool designed to make your workflow easier and more
efficient, while also reducing the number of other tools you need to know.
It aims to make the 90% use cases as pleasant as possible.

%prep
%setup -q -n hatch-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/hatch
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PATH=$PATH:%{buildroot}%{_bindir}
# test_list_success_1 randomly timeouts in OBS
%pytest -k 'not test_list_success_1'

%post
%python_install_alternative hatch

%postun
%python_uninstall_alternative hatch

%files %{python_files}
%doc README.rst
%license LICENSE-APACHE LICENSE-MIT
%python_alternative %{_bindir}/hatch
%{python_sitelib}/*

%changelog
