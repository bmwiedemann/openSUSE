#
# spec file for package gitlint
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


Name:           gitlint
Version:        0.13.1
Release:        0
Summary:        Git commit message linter checking
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jorisroovers/%{name}
Source:         https://pypi.io/packages/source/g/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE relax-requirements.patch -- relax requirements to work with openSUSE
Patch0:         relax-requirements.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-arrow >= 0.10.0
Requires:       python-click >= 6.7
Requires:       python-sh >= 1.12.14
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Great for use as a commit-msg git hook or as part of your gating script in
a CI/CD pipeline (e.g. jenkins). Many of the gitlint validations are based
on well-known community standards, others are based on checks that we've
found useful throughout the years. Gitlint has sane defaults, but you can
also easily customize it to your own liking.

%prep
%setup -q
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/%{name}
%fdupes %{buildroot}%{_prefix}

%post
%python_install_alternative gitlint

%postun
%python_uninstall_alternative gitlint

%files %{python_files}
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/gitlint

%changelog
