#
# spec file for package python-black
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-black
Version:        25.11.0
Release:        0
Summary:        A code formatter written in, and written for Python
License:        MIT
URL:            https://github.com/psf/black
Source:         https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.3.2}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module click >= 8.0.0}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling >= 1.8.0}
BuildRequires:  %{python_module mypy_extensions >= 0.4.3}
BuildRequires:  %{python_module packaging >= 22.0}
BuildRequires:  %{python_module pathspec >= 0.9.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytokens >= 0.1.10}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-aiohttp >= 3.10.0
Requires:       python-click >= 8.0.0
Requires:       python-mypy_extensions >= 0.4.3
Requires:       python-packaging
Requires:       python-pathspec >= 0.9.0
Requires:       python-platformdirs >= 2
Requires:       python-pytokens >= 0.1.10

%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
mkdir -p ~/bin
cp $(ls %{buildroot}%{_bindir}/black-* | head -1) ~/bin/black
export PATH=$PATH:~/bin

# test_expression_diff - sometimes fails on async timing in OBS
# test_bpo_2142_workaround fails on arm
skiptests="test_expression_diff or test_bpo_2142_workaround"
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative black

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
