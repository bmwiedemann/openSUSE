#
# spec file for package python-pyct
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-pyct
Version:        0.6.0
Release:        0
Summary:        Python package for common tasks for users
License:        BSD-3-Clause
URL:            https://github.com/pyviz/pyct
Source0:        https://files.pythonhosted.org/packages/source/p/pyct/pyct-%{version}.tar.gz
Source100:      python-pyct-rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-vcs >= 0.4.0}
BuildRequires:  %{python_module hatchling >= 1.25.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-param >= 1.7.0
Recommends:     python-PyYAML
Recommends:     python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module param >= 1.7.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A utility package that includes:

  1. pyct.cmd: Makes various commands available to other
     packages. (Currently no sophisticated plugin system, just a try
     import/except in the other packages.) The same commands are
     available from within python. Can either add new subcommands to
     an existing argparse based command if the module has an existing
     command, or create the entire command if the module has no
     existing command. Currently, there are commands for copying
     examples and fetching data. See

  2. pyct.build: Provides various commands to help package
     building, primarily as a convenience for project maintainers.

%prep
%setup -q -n pyct-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyct

%post
%python_install_alternative pyct

%postun
%python_uninstall_alternative pyct

%check
rm -rf build _build*
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/pyct
%{python_sitelib}/pyct
%{python_sitelib}/pyct-%{version}.dist-info

%changelog
