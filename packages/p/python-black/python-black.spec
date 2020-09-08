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
Version:        20.8b1
Release:        0
Summary:        A code formatter written in, and written for Python
License:        MIT
URL:            https://github.com/psf/black
Source:         https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.3.2}
BuildRequires:  %{python_module aiohttp_cors}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs >= 18.1.0}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module click >= 7.1.2}
BuildRequires:  %{python_module mypy_extensions >= 0.4.3}
BuildRequires:  %{python_module pathspec >= 0.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex >= 2020.1.8}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml >= 0.10.1}
BuildRequires:  %{python_module typed-ast >= 1.4.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.3.2
Requires:       python-aiohttp_cors
Requires:       python-appdirs
Requires:       python-attrs >= 18.1.0
Requires:       python-click >= 7.1.2
Requires:       python-mypy_extensions >= 0.4.3
Requires:       python-pathspec >= 0.6
Requires:       python-regex >= 2020.1.8
Requires:       python-toml >= 0.10.1
Requires:       python-typed-ast >= 1.4.0
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
sed -i '1{/#!/d}' src/black_primer/cli.py src/black_primer/lib.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/black
%python_clone -a %{buildroot}%{_bindir}/blackd
%python_clone -a %{buildroot}%{_bindir}/black-primer
%{python_expand cp src/black_primer/primer.json %{buildroot}%{$python_sitelib}/black_primer/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# Copy one of the executable scripts into the PATH
mkdir ~/bin
cp $(ls %{buildroot}%{_bindir}/black-* | head -1) ~/bin/black
export PATH=$PATH:~/bin

# test_expression_diff - sometimes fails on async timing in OBS
skiptests="test_expression_diff"
# https://github.com/psf/black/issues/1109
if [ $(python3 -c 'import sys; print(sys.byteorder)') == 'big' ]; then
skiptests+=" or test_python2"
fi
%pytest -k "not ($skiptests)"

%post
%python_install_alternative black blackd black-primer

%postun
%python_uninstall_alternative black

%files %{python_files}
%doc README.md CHANGES.md docs/*.md docs/reference
%license LICENSE
%python_alternative %{_bindir}/black
%python_alternative %{_bindir}/blackd
%python_alternative %{_bindir}/black-primer
%{python_sitelib}/_black_version.py*
%{python_sitelib}/black_primer/
%{python_sitelib}/black/
%{python_sitelib}/blackd/
%{python_sitelib}/blib2to3/
%{python_sitelib}/black-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
