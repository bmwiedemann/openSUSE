#
# spec file for package python-black
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
Name:           python-black
Version:        24.8.0
Release:        0
Summary:        A code formatter written in, and written for Python
License:        MIT
URL:            https://github.com/psf/black
Source:         https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.3.2}
BuildRequires:  %{python_module aiohttp_cors}
BuildRequires:  %{python_module attrs >= 18.1.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module click >= 8.0.0}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling >= 1.8.0}
BuildRequires:  %{python_module mypy_extensions >= 0.4.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pathspec >= 0.9.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli >= 1.1.0}
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module typing_extensions >= 3.10.0.0 if %python-base < 3.11}
%endif
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.3.2
Requires:       python-aiohttp_cors
Requires:       python-attrs >= 18.1.0
Requires:       python-click >= 8.0.0
Requires:       python-mypy_extensions >= 0.4.3
Requires:       python-packaging
Requires:       python-pathspec >= 0.9.0
Requires:       python-platformdirs >= 2
Requires:       python-tomli >= 1.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?python_version_nodots} < 311
Requires:       python-typing_extensions >= 3.10.0.0
%endif
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
%autosetup -p1 -n black-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/black
%python_clone -a %{buildroot}%{_bindir}/blackd
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
# Copy one of the executable scripts into the PATH
mkdir ~/bin
cp $(ls %{buildroot}%{_bindir}/black-* | head -1) ~/bin/black
export PATH=$PATH:~/bin

# test_expression_diff - sometimes fails on async timing in OBS
# test_bpo_2142_workaround fails on arm
skiptests="test_expression_diff or test_bpo_2142_workaround"
%pytest -k "not ($skiptests)"

%post
%python_install_alternative black blackd

%postun
%python_uninstall_alternative black

%files %{python_files}
%doc README.md CHANGES.md docs/*.md
%license LICENSE
%python_alternative %{_bindir}/black
%python_alternative %{_bindir}/blackd
%{python_sitelib}/_black_version.py*
%{python_sitelib}/black/
%{python_sitelib}/blackd/
%{python_sitelib}/blib2to3/
%{python_sitelib}/black-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
