#
# spec file for package python-poetry
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-poetry
Version:        1.1.12
Release:        0
Summary:        Python dependency management and packaging
License:        MIT
Group:          Development/Languages/Python
URL:            https://python-poetry.org/
# PyPI sdist doesnt contain tests
Source:         https://github.com/python-poetry/poetry/archive/%{version}.tar.gz#/poetry-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/python-poetry/poetry/pull/3255#issuecomment-713442094 -- remove external http call requirement for lock --no-update
Patch0:         poetry-1645-1.1.patch
# PATCH-FIX-UPSTREAM https://github.com/python-poetry/poetry/commit/9591e88492508d4dba260952d53266a0032c04c7
Patch1:         use-new-name-of-MockFixture.patch
# PATCH-FIX-UPSTREAM https://github.com/python-poetry/poetry/pull/4749 -- make compatible with packaging >= 21
Patch2:         poetry-4749-1.1.patch
BuildRequires:  %{python_module CacheControl >= 0.12.9}
BuildRequires:  %{python_module cachy >= 0.3.0}
BuildRequires:  %{python_module cleo >= 0.8.1}
BuildRequires:  %{python_module clikit >= 0.6.2}
BuildRequires:  %{python_module html5lib >= 1.0}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.6}
BuildRequires:  %{python_module keyring >= 21.2.0}
# cachecontrol[filecache]
BuildRequires:  %{python_module lockfile >= 0.9}
BuildRequires:  %{python_module packaging >= 20.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkginfo >= 1.5}
BuildRequires:  %{python_module poetry-core >= 1.0.7}
BuildRequires:  %{python_module requests >= 2.18}
BuildRequires:  %{python_module requests-toolbelt >= 0.9.1}
BuildRequires:  %{python_module shellingham >= 1.1}
BuildRequires:  %{python_module tomlkit >= 0.7.0}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-CacheControl >= 0.12.9
Requires:       python-cachy >= 0.3.0
Requires:       python-cleo >= 0.8.0
Requires:       python-clikit >= 0.6.2
Requires:       python-html5lib >= 1.0
Requires:       python-keyring >= 21.2.0
# cachecontrol[filecache]
Requires:       python-lockfile >= 0.9
Requires:       python-pkginfo >= 1.5
Requires:       python-packaging >= 20.4
Requires:       python-pexpect >= 4.7.0
Requires:       python-poetry-core >= 1.0.7
Requires:       python-requests >= 2.18
Requires:       python-requests-toolbelt >= 0.9.1
Requires:       python-shellingham >= 1.1
Requires:       python-tomlkit >= 0.7.0
Requires:       python-virtualenv >= 20.0.26
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     git-core
Recommends:     python-devel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httpretty >= 1.0.3}
BuildRequires:  %{python_module pytest-mock >= 3.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Python dependency management and packaging made easy.

%prep
%autosetup -p1 -n poetry-%{version}
rm poetry/_vendor/.gitignore
rmdir poetry/_vendor
find poetry -name '*.py' -executable -print0 | xargs -0 chmod a-x

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/poetry
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# discussion of this section: gh#python-poetry/poetry#1645
%{python_expand # a virtualenv is necessary
virtualenv-%{$python_bin_suffix} --system-site-packages testenv-%{$python_bin_suffix}
source testenv-%{$python_bin_suffix}/bin/activate
export PYTHONPATH="%{buildroot}%{$python_sitelib}"
export PYTHONDONTWRITEBYTECODE=1
# pytest needs to be called from the virtualenv python interpreter
python -m pytest -v tests
deactivate
}

%post
%python_install_alternative poetry

%postun
%python_uninstall_alternative poetry

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/poetry
%{python_sitelib}/poetry-%{version}*-info
%python_alternative %{_bindir}/poetry

%changelog
