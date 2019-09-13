#
# spec file for package tj
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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

Name:           tj
Version:        7.0.0
Release:        0
Summary:        Timestamp input
License:        MIT
Group:          System/Base
URL:            https://github.com/sgreben/tj
#Git-Clone:     https://github.com/sgreben/tj.git
Source:         https://github.com/sgreben/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  golang(API) >= 1.9
BuildRequires:  golang-packaging
%{go_provides}

%description
tj adds a timestamp to the beginning of each line of input.
It supports several time-formats and can also colorize the output.
Users could also define custom output formats via templates.

%prep
%setup -q

%build
%{goprep} github.com/sgreben/tj
%{gobuild} ...

%install
%{goinstall}
%{gosrc}
%{gofilelist}

%files -f file.lst
%doc README.md
%{_bindir}/tj

%changelog
