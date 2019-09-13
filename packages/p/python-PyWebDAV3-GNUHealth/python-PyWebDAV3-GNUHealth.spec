#
# spec file for package python-PyWebDAV3-GNUHealth
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         oldpython python
%define         skip_python2 1
%bcond_without  test
Name:           python-PyWebDAV3-GNUHealth
Version:        0.10.3
Release:        0
%define ltmsver 0.13
Summary:        WebDAV library for Python - GNU Health port
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Servers
Url:            http://health.gnu.org
Source0:        https://files.pythonhosted.org/packages/source/P/PyWebDAV3-GNUHealth/PyWebDAV3-GNUHealth-%{version}.tar.gz
Source1:        http://www.webdav.org/neon/litmus/litmus-%{ltmsver}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
Conflicts:      python-PyWebDAV3
%ifpython2
Obsoletes:      %{oldpython}-PyWebDAV < %{version}
Provides:       %{oldpython}-PyWebDAV = %{version}
%endif
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
This is a Python WebDAV implementation (level 1 and 2) that
features a library for integrating WebDAV server capabilities
into applications.

An example on how to use the library is included. This server
can be run as daemon.

Port from Andrew Leech PyWebDAV3 library to Support GNU Health.

%prep
%setup -q -n PyWebDAV3-GNUHealth-%{version}
cp %{SOURCE1} test/

%build
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/pywebdav/server/server.py
sed -i "s|^#!/usr/bin/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/pywebdav/server/server.py
%fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pywebdav/server/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pywebdav/server/
%fdupes %{buildroot}%{$python_sitelib}/pywebdav/server/
}

%python_clone -a %{buildroot}%{_bindir}/davserver

%if %{with test}
%check
%python_expand py.test-%{$python_bin_suffix}
%endif

%post
%python_install_alternative davserver

%postun
%python_uninstall_alternative davserver

%files %{python_files}
%defattr(-,root,root,-)
%doc README doc/Changes doc/LICENSE doc/TODO
%python_alternative %{_bindir}/davserver
%{python_sitelib}/*

%changelog
