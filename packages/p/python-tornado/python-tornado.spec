#
# spec file for package python-tornado
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_without python2
%{?sle15_python_module_pythons}
%global mbflavor @BUILD_FLAVOR@%{nil}
%if "%{mbflavor}" == "python2" && 0%{with python2}
# TW Factory defines _without_python2 and skips all python3 flavors if skip_python3 is defined
%define skip_python3 1
%define tornadoN tornado5
%define flavorbuild 1
%endif
%if "%{mbflavor}" == "python3"
# All distributions should have one or more python3 flavors
%define skip_python2 1
%define tornadoN tornado6
%define flavorbuild 1
%endif
%if ! 0%{?flavorbuild}
ExclusiveArch:  DoNotBuild
%endif

# query the default provider and assume that all installed python flavors have the same version
%if %{defined sle15_python_module_pythons}
%define Nversion %(rpm -q --qf '%%{version}' --whatprovides %{pythons}-%{tornadoN})
%else
%define Nversion %(rpm -q --qf '%%{version}' --whatprovides %{mbflavor}-%{tornadoN})
%endif

Name:           python-tornado
Version:        %{Nversion}
Release:        0
Summary:        A Python web framework and asynchronous networking library
License:        Apache-2.0
URL:            https://www.tornadoweb.org
Source0:        README.SUSE
BuildRequires:  %{python_module %{tornadoN}}
BuildRequires:  python-rpm-macros
Requires:       python-%{tornadoN} = %{Nversion}
BuildArch:      noarch
%python_subpackages

%description
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O, Tornado
can scale to tens of thousands of open connections, making it ideal for long
polling, WebSockets, and other applications that require a long-lived
connection to each user.

%prep
%setup -q -T -c
cp %{SOURCE0} .

%build
:

%install
:

%files %{python_files}
%doc README.SUSE

%changelog
