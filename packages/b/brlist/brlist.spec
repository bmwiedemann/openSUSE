#
# spec file for package brlist
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
Name:           brlist
Version:        0.1
Release:        0
Summary:        Tool for listing linux bridges with their member interfaces
License:        GPL-3.0-or-later
URL:            https://github.com/asdil12/%{name}
Source0:        https://github.com/asdil12/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  iproute2
Requires:       iproute2
Requires:       python3
BuildArch:      noarch

%description
This is a tool to list linux bridges with their member interfaces.
As there is no good replacement for `brctl` in the iproute2 aera,
this tool aims to provide a similar user-friendly output.

%prep
%setup -q

%build

%install
install -m 755 -D -v %{name}.py %{buildroot}%{_bindir}/%{name}
%{python3_fix_shebang}

%check
./%{name}.py

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
