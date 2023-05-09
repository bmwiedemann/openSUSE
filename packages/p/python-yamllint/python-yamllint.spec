#
# spec file for package python-yamllint
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-yamllint
Version:        1.28.0
Release:        0
Summary:        A linter for YAML files
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/adrienverge/yamllint
Source:         https://files.pythonhosted.org/packages/source/y/yamllint/yamllint-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-pathspec >= 0.5.3
%if 0%{python_version_nodots} < 38
# boo#1151703, See below
Requires:       python-setuptools
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
# override gh#adrienverge/yamllint#401, boo#1151703 fixed by importlib.resources in python >= 3.8 and a recent setuptools
sed 's/  setuptools/  setuptools; python_version < "3.8"/' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/yamllint

%check
export LANG="en_US.UTF8"
# skip test_run_with_user_global_config_file, probably same reason as upstreams GHA skip: '$HOME not overridable'
export GITHUB_RUN_ID=1
%pyunittest -v

%post
%python_install_alternative yamllint

%postun
%python_uninstall_alternative yamllint

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/yamllint
%{python_sitelib}/yamllint
%{python_sitelib}/yamllint-%{version}*-info

%changelog
