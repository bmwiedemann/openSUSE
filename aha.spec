#
# spec file for package aha
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           aha
Version:        0.5.1
Release:        0
Summary:        ANSI color to HTML converter
License:        MPL-1.1 OR LGPL-2.1-or-later
Group:          System/Console
URL:            https://github.com/theZiz/aha/
Source:         https://github.com/theZiz/aha/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
aha (ANSI HTML Adapter) converts ANSI colors to HTML, e.g. if you
want to publish the output of ls --color=yes, git diff, ccal or htop
as static HTML somewhere.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%doc CHANGELOG README.md
%{_bindir}/aha
%{_mandir}/man1/aha.1%{?ext_man}

%changelog
