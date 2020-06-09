#
# spec file for package python-black
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
Name:           python-black
Version:        19.10b0
Release:        0
Summary:        A code formatter written in, and written for Python
License:        MIT
URL:            https://github.com/ambv/black
Source:         https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
Patch0:         fix-tests.patch
BuildRequires:  %{python_module aiohttp >= 3.3.2}
# TODO: needed for blackd
#BuildRequires:  %{python_module aiohttp-cors}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs >= 18.1.0}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module click >= 6.5}
BuildRequires:  %{python_module mypy_extensions}
BuildRequires:  %{python_module pathspec}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml >= 0.9.4}
BuildRequires:  %{python_module typed-ast}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.3.2
# TODO: needed for blackd
#Requires:       python-aiohttp-cors
Requires:       python-appdirs
Requires:       python-attrs >= 18.1.0
Requires:       python-click >= 6.5
Requires:       python-mypy_extensions
Requires:       python-pathspec
Requires:       python-regex
Requires:       python-toml >= 0.9.4
Requires:       python-typed-ast
Requires:       python-typing_extensions
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Black is a code formatter written in Python, and reformats Python 2.x
and 3.x code.

Black reformats entire files in place. It is not configurable. It
does not take previous formatting into account. The coding style
enforced is a PEP-8 subset, adheres to PEP-257, and otherwise passes
the rules of the "pycodestyle" checker. Black skips over blocks that
start and end with "# fmt: off" and "# fmt: on", respectively. It
also recognizes YAPF's block comments to the same effect.

%prep
%setup -q -n black-%{version}
%patch0 -p1
rm -rf %{pypi_name}.egg-info

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/black
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# TODO: missing aiohttp-cors (not in distribution and tests failing)
rm %{buildroot}/%{_bindir}/blackd

%check
# test_expression_diff - sometimes fails on async timing in OBS
%pytest -k 'not test_expression_diff'

%post
%python_install_alternative black

%postun
%python_uninstall_alternative black

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/black
#%%python_alternative %%{_bindir}/blackd
%license LICENSE
%{python_sitelib}/*

%changelog
