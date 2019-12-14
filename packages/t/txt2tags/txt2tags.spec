#
# spec file for package txt2tags
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013,2019 Christoph Junghans <junghans@votca.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           txt2tags
Version:        3.3
Release:        0
Summary:        Converts text files to HTML, XHTML, sgml, LaTeX, man and others
License:        GPL-2.0
Group:          Productivity/Text/Convertors
Url:            http://txt2tags.sourceforge.net
Source:         https://github.com/jendrikseipp/txt2tags/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/txt2tags/txt2tags/commit/49b0808
Patch0:         reproducible.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Obsoletes:      txt2tags < %{version}
Provides:       txt2tags = %{version}
Requires:       %{python_module setuptools}

Requires(post):    update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
Txt2tags is a generic text converter. From a simple text file with minimal
markup, it generates documents on the following formats: HTML, XHTML, sgml,
LaTeX, Lout, man, Magic Point (mgp), MoinMoin and Adobe PageMaker. Supports
heading, font beautifiers, verbatim, quote, link, lists, table and image.
There are GUI, Web and cmdline interfaces. It's a single Python script and
no external commands or libraries are needed.
 
%prep
%setup -q
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/txt2tags
sed -i '1s/env python/python3/' %{buildroot}%{python3_sitelib}/txt2tags.py
chmod +x %{buildroot}%{python3_sitelib}/txt2tags.py
%ifpython2
sed -i '1s/env python/python2/' %{buildroot}%{python2_sitelib}/txt2tags.py
chmod +x %{buildroot}%{python2_sitelib}/txt2tags.py
%endif

%post
%python_install_alternative txt2tags

%postun
%python_uninstall_alternative txt2tags

%files %python_files
%doc CHANGELOG.md README.md
%license COPYING
%python_alternative %{_bindir}/txt2tags
%{python_sitelib}/txt2tags*
%pycache_only %{python_sitelib}/__pycache__

%changelog
