#
# spec file for package jp
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

Name:           jp
Version:        1.1.12
Release:        0
Summary:        JSON/CSV data plotting program for the terminal
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/sgreben/jp
#Git-Clone:     https://github.com/sgreben/jp.git
Source:         https://github.com/sgreben/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  golang(API) >= 1.9
BuildRequires:  golang-packaging
BuildRequires:  fdupes
Conflicts:      python2-jmespath
Conflicts:      python3-jmespath
%{go_provides}

%description
This program generates terminal plots from JSON (or CSV) data. Bar charts,
line charts, scatter plots, histograms and heatmaps are supported.

%prep
%setup -q

%build
%{goprep} github.com/sgreben/jp
%{gobuild} ...

%install
%{goinstall}
%{gosrc}
%{gofilelist}
%fdupes -s %{buildroot}

%files -f file.lst
%doc README.md
%license LICENSE
%{_bindir}/jp

%changelog
