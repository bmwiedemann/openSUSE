#
# spec file for package python-setuptools-git-versioning
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
Name:           python-setuptools-git-versioning
Version:        1.13.5
Release:        0
Summary:        Use git repo data for building a version number according PEP-440
License:        MIT
URL:            https://setuptools-git-versioning.readthedocs.io
# SourceDist:    https://github.com/dolfinus/setuptools-git-versioning
# the sdist on PyPI does not have the tests, we needs full git metadata for bootstrap, run osc service runall to update
Source:         setuptools-git-versioning-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-packaging
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-setuptools_git_versioning = %{version}-%{release}
BuildArch:      noarch
%if 0%{python_version_nodots} < 311
Requires:       python-toml >= 0.10.2
%endif
# SECTION test
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Use git repo data (latest tag, current commit hash, etc) for building a
version number according PEP440.

  - Can be installed & configured through both `setup.py` and :PEP518's `pyproject.toml`
  - Does not require to change source code of the project
  - Tag-, file-, and callback-based versioning schemas are supported
  - Templates for *tag*, *dev* and *dirty* versions are separated
  - Templates support a lot of substitutions including git and environment information

%prep
%setup -q -n setuptools-git-versioning-%{version}
# avoid dirty version
echo '_build*' >> .git/info/exclude
echo _current_flavor >> .git/info/exclude

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/setuptools-git-versioning
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# cannot test isolated: no wheels for setuptools, wheel, coverage. Modify after wheel build
sed -i  '/assert get_version(repo, isolated=True)/d' tests/test_integration/test_config.py
# test tries to get a wheel wheel in isolated build env
donttest="test_substitution_env"
%pytest -k "not ($donttest)" -n auto

%post
%python_install_alternative setuptools-git-versioning

%postun
%python_uninstall_alternative setuptools-git-versioning

%files %{python_files}
%python_alternative %{_bindir}/setuptools-git-versioning
%{python_sitelib}/setuptools_git_versioning.py*
%{python_sitelib}/setuptools_git_versioning-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/setuptools_git_versioning*.pyc

%changelog
