#
# spec file for package smtpping
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           smtpping
Version:        1.1.3
Release:        0
Summary:        A tool for measuring SMTP server delay, delay variation and throughput
License:        GPL-2.0
Group:          Productivity/Networking/Other
URL:            https://github.com/halon/smtpping
#Git-Clone:     https://github.com/halon/smtpping.git
Source:         https://github.com/halon/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A tool for measuring SMTP server delay, delay variation and throughput.

%prep
%setup -q

%build
%cmake \
    -DMAN_INSTALL_DIR="%{_mandir}"

%install
%cmake_install

%files
%doc LICENSE README.md
%{_bindir}/smtpping
%{_mandir}/man1/smtpping.1%{ext_man}

%changelog
