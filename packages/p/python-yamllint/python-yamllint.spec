#
# spec file for package python-yamllint
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
Name:           python-yamllint
Version:        1.24.2
Release:        0
Summary:        A linter for YAML files
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/adrienverge/yamllint
Source:         https://files.pythonhosted.org/packages/source/y/yamllint/yamllint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-pathspec >= 0.5.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pathspec >= 0.5.3}
# /SECTION
%python_subpackages

%description
A linter for YAML files.

YAMLlint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%prep
%setup -q -n yamllint-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/yamllint

%check
export LANG="en_US.UTF8"
%python_exec -m unittest discover -v

%post
%python_install_alternative yamllint

%postun
%python_uninstall_alternative yamllint

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/yamllint
%{python_sitelib}/*

%changelog
