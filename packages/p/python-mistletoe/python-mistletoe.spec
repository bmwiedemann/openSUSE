#
# spec file for package python-mistletoe
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-mistletoe
Version:        1.5.0
Release:        0
Summary:        A Markdown parser in pure Python
License:        MIT
URL:            https://github.com/miyuchina/mistletoe
Source:         https://github.com/miyuchina/mistletoe/archive/refs/tags/v%{version}.tar.gz#/mistletoe-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Pygments
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A Markdown parser in pure Python, designed to be fast,
spec-compliant and fully customizable.

%prep
%autosetup -p1 -n mistletoe-%{version}
sed -i 's,/usr/bin/env python,,' mistletoe/contrib/md2jira.py
find . -type f -print0 | xargs -0 dos2unix --

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mistletoe
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative mistletoe

%post
%python_install_alternative mistletoe

%postun
%python_uninstall_alternative mistletoe

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mistletoe
%{python_sitelib}/mistletoe
%{python_sitelib}/mistletoe-%{version}.dist-info

%changelog
