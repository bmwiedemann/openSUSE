#
# spec file for package webrepl
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


%define use_python python3
%define pythons %{use_python}

Name:           webrepl
Version:        20221108.1e09d9a
Release:        0
Summary:        Tool similar to ssh/scp for MicroPython devices running WebREPL
License:        MIT
URL:            https://github.com/micropython/webrepl
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  python-rpm-macros

%description
WebREPL client, for accessing a MicroPython REPL (interactive prompt)
as well as transfering files over WebSockets.

%prep
%setup -q

%build

%install
install -m 755 -D -v webrepl_cli.py %{buildroot}%{_bindir}/%{name}
%python3_fix_shebang

%check
# There are no tests available even upstream

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
