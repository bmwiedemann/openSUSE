#
# spec file for package python-webassets
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  python2
Name:           python-webassets
Version:        2.0
Release:        0
Summary:        Media asset management for Python, with glue code for various web frameworks
# rjsmin=Apache-2.0
# jspacker=LGPL-2.1
# cssrewrite=BSD-3-Clause
# six.py=MIT
License:        Apache-2.0 AND BSD-2-Clause AND LGPL-2.1-only AND BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/miracle2k/webassets/
Source:         https://files.pythonhosted.org/packages/source/w/webassets/webassets-%{version}.tar.gz
# PATCH-FIX-UPSTREAM webassets-py39-threading.patch -- gh#miracle2k/webassets#529
Patch0:         https://github.com/miracle2k/webassets/pull/529.patch#/webassets-py39-threading.patch
# PATCH-FIX-UPSTREAM remove-nose -- gh#miracle2k/webassets#539
Patch1:         remove-nose.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
# jsmin and rjsmin fail if imported: different utf8 filters
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cssutils}
BuildRequires:  %{python_module glob2}
BuildRequires:  %{python_module lesscpy}
BuildRequires:  %{python_module rcssmin}
BuildRequires:  %{python_module slimit}
BuildRequires:  sassc
%if %{with python2}
BuildRequires:  python2-mock
%endif
# /SECTION
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Merges, minifies and compresses Javascript and CSS files, supporting a variety
of different filters, including YUI, jsmin, jspacker or CSS tidy. Also supports
URL rewriting in CSS files.

%prep
%autosetup -p1 -n webassets-%{version}
sed -i 's/#!.*//' src/webassets/filter/rjsmin/rjsmin.py
# fix py2 only syntax
sed -i -e 's:e.message:e.args[0]:g' tests/test_filters.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/webassets
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%pytest -ra

%post
%python_install_alternative webassets

%postun
%python_uninstall_alternative webassets

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.rst
%python_alternative %{_bindir}/webassets
%{python_sitelib}/*

%changelog
