#
# spec file for package python-webassets
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-webassets
Version:        0.12.1
Release:        0
Summary:        Media asset management for Python, with glue code for various web frameworks
# rjsmin=Apache-2.0
# jspacker=LGPL-2.1
# cssrewrite=BSD-3-Clause
# six.py=MIT
License:        BSD-2-Clause AND Apache-2.0 AND LGPL-2.1-only AND BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            http://github.com/miracle2k/webassets/
Source:         https://files.pythonhosted.org/packages/source/w/webassets/webassets-%{version}.tar.gz
Patch0:         tests.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Merges, minifies and compresses Javascript and CSS files, supporting a variety
of different filters, including YUI, jsmin, jspacker or CSS tidy. Also supports
URL rewriting in CSS files.

%prep
%setup -q -n webassets-%{version}
%patch0 -p1
sed -i 's/#!.*//' src/webassets/filter/rjsmin/rjsmin.py
# fix py2 only syntax
sed -i -e 's:e.message:e.args[0]:g' tests/test_filters.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{pytest}

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.rst
%python3_only %{_bindir}/webassets
%{python_sitelib}/*

%changelog
