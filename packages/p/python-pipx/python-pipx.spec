#
# spec file for package python-pipx
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
Name:           python-pipx
Version:        0.14.0.0
Release:        0
Summary:        Install and run Python applications in isolated environments
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pipxproject/pipx
Source:         https://github.com/pipxproject/pipx/archive/%{version}.tar.gz#/pipx-%{version}.tar.gz
# PATCH-FIX-OPENSUSE test_alternative_names.patch mcepl@suse.com
# Make tests pass even with using alternatives
Patch0:         test_alternative_names.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module argcomplete >= 1.9.4}
BuildRequires:  %{python_module userpath}
# /SECTION
BuildRequires:  fdupes
Requires:       python-argcomplete >= 1.9.4
Requires:       python-setuptools
Requires:       python-userpath
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Install and run Python applications in isolated environments.

%prep
%setup -q -n pipx-%{version}
%autopatch -p1

sed -i '1{/^#!/d}' pipx/main.py pipx/venv_metadata_inspector.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pipx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Incompatible with nox https://github.com/pipxproject/pipx/blob/047a0be/noxfile.py#L7
# Most tests need internet https://github.com/pipxproject/pipx/issues/248
export PATH=$PATH:%{buildroot}%{_bindir}
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m venv --system-site-packages testenv
source testenv/bin/activate
$python -m pytest -vv -k 'test_basic_commands or test_pipx_help_contains_text'
}

%post
%python_install_alternative pipx

%postun
%python_uninstall_alternative pipx

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pipx
%{python_sitelib}/*

%changelog
