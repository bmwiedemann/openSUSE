#
# spec file for package python-demosh
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-demosh
Version:        0.5.0
Release:        0
Summary:        Run code in Markdown files or shell scripts very interactively
License:        Apache-2.0
URL:            https://github.com/BuoyantIO/demosh
Source:         https://github.com/BuoyantIO/demosh/archive/v%{version}.tar.gz#/demosh-%{version}.tar.gz
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-curses
BuildArch:      noarch
%python_subpackages

%description
tl;dr: demosh can run shell scripts or Markdown files in a very interactive
way, showing commentary in between running commands, and waiting for you to hit
RETURN to proceed before running commands. It was created as a tool for doing
live demos of relatively complex things. See testing.md and testing.sh for
examples.

%prep
%autosetup -n demosh-%{version}
# Remove shebangs
sed -i '/#!.*env python/d' demosh/*.py
chmod 0644 demosh/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/
%python_clone -a %{buildroot}%{_bindir}/demosh

%check
# Test that the command works
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
%{buildroot}%{_bindir}/demosh-%{$python_version} --version
}

%post
%python_install_alternative demosh

%postun
%python_uninstall_alternative demosh

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/demosh
%{python_sitelib}/demosh
%{python_sitelib}/demosh-%{version}*-info

%changelog
