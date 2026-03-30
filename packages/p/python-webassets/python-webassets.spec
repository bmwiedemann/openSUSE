#
# spec file for package python-webassets
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


Name:           python-webassets
Version:        3.0.0
Release:        0
Summary:        Media asset management for Python, with glue code for various web frameworks
# rjsmin=Apache-2.0
# jspacker=LGPL-2.1
# cssrewrite=BSD-3-Clause
License:        Apache-2.0 AND BSD-2-Clause AND LGPL-2.1-only AND BSD-3-Clause
URL:            https://github.com/miracle2k/webassets/
Source:         https://files.pythonhosted.org/packages/source/w/webassets/webassets-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.2
Requires:       python-zope.dottedname >= 6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.1.4}
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module cssutils >= 2.11.1}
BuildRequires:  %{python_module libsass >= 0.23.0}
BuildRequires:  %{python_module ply >= 3.11}
BuildRequires:  %{python_module pytest >= 8.3.3}
BuildRequires:  %{python_module rcssmin >= 1.1.2}
BuildRequires:  %{python_module slimit >= 0.8.1}
BuildRequires:  sassc
# /SECTION
%python_subpackages

%description
Merges, minifies and compresses Javascript and CSS files, supporting a variety
of different filters, including YUI, jsmin, jspacker or CSS tidy. Also supports
URL rewriting in CSS files.

%prep
%autosetup -p1 -n webassets-%{version}

sed -i 's/#!.*//' src/webassets/filter/rjsmin/rjsmin.py

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/webassets
%{python_sitelib}/webassets-%{version}.dist-info

%changelog
