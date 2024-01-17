#
# spec file for package python-PyWebDAV3
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
%define         oldpython python
%define ltmsver 0.13
Name:           python-PyWebDAV3
Version:        0.9.14
Release:        0
Summary:        WebDAV library including a standalone server for python2 and python3
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/andrewleech/PyWebDAV3
Source0:        https://files.pythonhosted.org/packages/source/P/PyWebDAV3/PyWebDAV3-%{version}.tar.gz
# Only used in %%check for testing purposes
Source1:        http://www.webdav.org/neon/litmus/litmus-%{ltmsver}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-PyWebDAV < %{version}
Provides:       %{oldpython}-PyWebDAV = %{version}
%endif
%python_subpackages

%description
WebDAV library for python2 and python3.

Consists of a server that is ready to run Serve and the DAV package
that provides WebDAV server functionality.

This package does not provide client functionality.

%prep
%setup -q -n PyWebDAV3-%{version}
cp %{SOURCE1} test/

%build
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/pywebdav/server/server.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/pywebdav/server/server.py
%fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pywebdav/server/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pywebdav/server/
%fdupes %{buildroot}%{$python_sitelib}/pywebdav/server/
}

%python_clone -a %{buildroot}%{_bindir}/davserver

%check
%pytest

%post
%python_install_alternative davserver

%postun
%python_uninstall_alternative davserver

%files %{python_files}
%license doc/LICENSE
%doc README doc/Changes doc/TODO
%python_alternative %{_bindir}/davserver
%{python_sitelib}/*

%changelog
