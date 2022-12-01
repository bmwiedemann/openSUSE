#
# spec file for package yank
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yank
Version:        1.3.0
Release:        0
Summary:        Tool for selecting and copying text from stdin without a mouse
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/mptre/yank
Source0:        https://github.com/mptre/yank/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
Requires:       bash

%description
Read input from stdin and display a selection interface that allows a field
to be selected and copied to the clipboard. Fields are either recognized by
a regular expression using the -g option or by splitting the input on a
delimiter sequence using the -d option.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=/usr

%files
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{ext_man}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
