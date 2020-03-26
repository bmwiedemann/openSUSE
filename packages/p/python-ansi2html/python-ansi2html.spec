#
# spec file for package python-ansi2html
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
Name:           python-ansi2html
Version:        1.5.2
Release:        0
Summary:        Python module to convert text with ANSI color codes to HTML or LaTeX
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ralphbean/ansi2html/
Source:         https://github.com/ralphbean/ansi2html/archive/%{version}.tar.gz
# https://github.com/ralphbean/ansi2html/pull/103
Patch0:         remove_nose.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A module to convert text with ANSI color codes to HTML or to LaTeX.

%prep
%setup -q -n ansi2html-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/ansi2html

%check
%python_exec -m unittest discover -s tests/ -v

%post
%python_install_alternative ansi2html

%postun
%python_uninstall_alternative ansi2html

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%python_alternative %{_bindir}/ansi2html
%{python_sitelib}/*

%changelog
