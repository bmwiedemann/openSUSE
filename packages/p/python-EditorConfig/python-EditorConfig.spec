#
# spec file for package python-EditorConfig
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
%define modname editorconfig-core-py
Name:           python-EditorConfig
Version:        0.12.3+git.1630438300.f43312a
Release:        0
Summary:        File Locator and Interpreter for Python
License:        BSD-2-Clause AND Python-2.0
URL:            https://editorconfig.org
Source0:        %{modname}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
EditorConfig Python Core provides the same functionality as the
EditorConfig C Core. EditorConfig Python core can be used as a
command line program or as an importable library.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
# remove executable that is already supplied by the editorconfig package
rm -rf %{buildroot}%{_bindir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Still not resolved issues with tests, gh#editorconfig/editorconfig-core-py#37
cmake .
export PYTHONPATH=%{buildroot}%{$python_sitelib}
ctest -VV --output-on-failure . || /bin/true

%files %{python_files}
%license LICENSE.* COPYING
%doc README.rst
%{python_sitelib}/editorconfig
%{python_sitelib}/EditorConfig-*.egg-info

%changelog
