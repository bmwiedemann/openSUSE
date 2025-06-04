#
# spec file for package python-css-html-js-minify
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


%bcond_without libalternatives
%define pkg_version 2.5.5
Name:           python-css-html-js-minify
Version:        2.5.5.git.1523718195.8f72452
Release:        0
Summary:        CSS HTML JS Minifier
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/juancarlospaco/css-html-js-minify#css-html-js-minify
Source:         css-html-js-minify-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Async single-file cross-platform no-dependencies Minifier for the Web

%prep
%autosetup -p1 -n css-html-js-minify-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/css-html-js-minify
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative css-html-js-minify

# post and postun macro call is not needed with only libalternatives

%check
%pyunittest tests.test_html_minifier

%files %{python_files}
%doc README.md
%license LICENCE.lgpl.txt LICENSE.gpl.txt
%python_alternative %{_bindir}/css-html-js-minify
%{python_sitelib}/css[-_]html[-_]js[-_]minify
%{python_sitelib}/css[-_]html[-_]js[-_]minify-%{pkg_version}*-info

%changelog
