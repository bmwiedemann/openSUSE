#
# spec file for package python-PyWebDAV3-GNUHealth
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
%bcond_without  test
Name:           python-PyWebDAV3-GNUHealth
Version:        0.13.0
Release:        0
%define ltmsver 0.15
Summary:        WebDAV library for Python - GNU Health port
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Servers
URL:            https://health.gnu.org
Source0:        https://files.pythonhosted.org/packages/source/P/PyWebDAV3-GNUHealth/pywebdav3_gnuhealth-%{version}.tar.gz
Source1:        https://notroj.github.io/litmus/litmus-%{ltmsver}.tar.gz

# TODO: send this upstream (where?)
Patch0:         pywebdav-server-configparser.patch
Patch1:         litmus_version.patch

BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  libxml2-devel
%endif
Conflicts:      python-PyWebDAV3
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives

%python_subpackages

%description
This is a Python WebDAV implementation (level 1 and 2) that
features a library for integrating WebDAV server capabilities
into applications.

An example on how to use the library is included. This server
can be run as daemon.

Port from Andrew Leech PyWebDAV3 library to Support GNU Health.

%prep
%autosetup -p1 -n pywebdav3_gnuhealth-%{version}

cp %{SOURCE1} test/

%build
%pyproject_wheel

%install
%pyproject_install

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
%pytest
%endif

%post
%python_install_alternative davserver

%postun
%python_uninstall_alternative davserver

%files %{python_files}
%license doc/LICENSE
%doc README.rst doc/Changes doc/TODO
%python_alternative %{_bindir}/davserver
%{python_sitelib}/pywebdav
%{python_sitelib}/[Pp]y[Ww]eb[Dd][Aa][Vv]3_[Gg][Nn][Uu][Hh]ealth-%{version}.dist-info

%changelog
