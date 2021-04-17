#
# spec file for package bump2version
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


# Flavor to build for
%define pythons python3
Name:           bump2version
Version:        1.0.1
Release:        0
Summary:        Version-bump software with a single command
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/c4urself/bump2version
# using GH URL instead of PyPI as the PyPI tarball contains already-prebuilt files
Source:         %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures >= 6.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      bumpversion <= 0.6.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch

%python_subpackages

%description
A command line tool handling the release process of software by updating all
version strings in the source code by the correct increment. Also creates
commits and tags. Version formats are configurable' works without any VCS, but
can read tag information from and writes commits and tags to Git and Mercurial
if available; handles text files, so it's not specific to any programming
language.

This package obsoletes bumpversion.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bump2version
%python_clone -a %{buildroot}%{_bindir}/bumpversion
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_usage_string_fork: bumpversion is not in PATH
%pytest -k 'not test_usage_string_fork'

%post
%{python_install_alternative bump2version bumpversion}

%postun
%python_uninstall_alternative bump2version

%files %{python_files}
%doc README.md
%license LICENSE.rst
%python_alternative %{_bindir}/bump2version
%python_alternative %{_bindir}/bumpversion
%{python_sitelib}/*

%changelog
