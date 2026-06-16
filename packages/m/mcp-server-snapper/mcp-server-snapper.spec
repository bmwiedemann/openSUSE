#
# spec file for package mcp-server-snapper
#
# Copyright (c) 2026 SUSE LLC
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

Name:           mcp-server-snapper
Version:        0.2.0
Release:        0
Summary:        MCP Server for Snapper
License:        MIT
URL:            https://github.com/aschnell/mcp-server-snapper
Source:         %{name}-%{version}.tar.xz
Patch0:         sle15sp7.patch
BuildArch:      noarch
BuildRequires:  python3-base
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
%if 0%{?suse_version} < 1600
%{sle15_python_module_pythons}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module mcp}
%else
BuildRequires:  python3-dbus-python
BuildRequires:  python3-mcp
%endif
Requires:       %{python_for_executables}-dbus-python
Requires:       %{python_for_executables}-mcp
Requires:       %{python_for_executables}-pydantic

%description
An MCP server for Snapper.

%prep
%setup -q

%if 0%{?suse_version} < 1600
%patch -P 0 -p1
%endif

%build

%check
cd testsuite && MCPSERVER=../src/mcp-server-snapper ./tools.py

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 src/mcp-server-snapper %{buildroot}%{_bindir}/mcp-server-snapper
install -d -m 0755 %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite
install -m 0755 testsuite/*.py %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite/

%files
%license LICENSE
%doc README.md
%{_bindir}/mcp-server-snapper

%package testsuite
Summary:        Testsuite for package %{name}
BuildArch:      noarch
Requires:       %{name}

%description testsuite
Testsuite for package %{name}

Note: This package is for testing purposes only. It is intended for
use by quality assurance and requires a dedicated testing environment.

Do not install on a production system!

%files testsuite
%{_prefix}/lib/mcp-server-snapper/
%{_prefix}/lib/mcp-server-snapper/testsuite/

%changelog
