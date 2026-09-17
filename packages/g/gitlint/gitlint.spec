#
# spec file for package gitlint
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pythons %{primary_python}
Name:           gitlint
Version:        0.19.1
Release:        0
Summary:        Git commit message linter checking
License:        MIT
URL:            https://github.com/jorisroovers/%{name}
Source:         https://pypi.io/packages/source/g/%{name}-core/%{name}_core-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-arrow >= 1
Requires:       python-click >= 8
Requires:       python-sh >= 1.13.0
BuildArch:      noarch
%python_subpackages

%description
Great for use as a commit-msg git hook or as part of your gating script in
a CI/CD pipeline (e.g. jenkins). Many of the gitlint validations are based
on well-known community standards, others are based on checks that we've
found useful throughout the years. Gitlint has sane defaults, but you can
also easily customize it to your own liking.

%prep
%setup -q -n %{name}_core-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_prefix}

%files %{python_files}
%license LICENSE
%{_bindir}/gitlint
%{python_sitelib}/gitlint
%{python_sitelib}/gitlint_core-%{version}*-info

%changelog
