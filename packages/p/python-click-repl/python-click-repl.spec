#
# spec file for package python-click-repl
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
Name:           python-click-repl
Version:        0.1.6
Release:        0
Summary:        REPL plugin for Click
License:        MIT
URL:            https://github.com/untitaker/click-repl
# No tests in PyPI archive
Source:         https://github.com/click-contrib/click-repl/archive/%{version}.tar.gz#/click-repl-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM click-repl-pr53-hyphens.patch -- Update tests to expect hyphens
Patch0:         https://github.com/click-contrib/click-repl/pull/53.patch#/click-repl-pr53-hyphens.patch
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module prompt_toolkit}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-prompt_toolkit
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
REPL plugin for Click

%prep
%autosetup -p1 -n click-repl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/click_repl
%{python_sitelib}/click_repl-%{version}*info

%changelog
