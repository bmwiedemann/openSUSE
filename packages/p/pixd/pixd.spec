#
# spec file for package pixd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pixd
Version:        1.0.0
Release:        0
Summary:        Colourful visualization tool for binary files
License:        MIT
Group:          Development/Tools/Debuggers
Url:            https://github.com/FireyFly/pixd.git
Source:         https://github.com/FireyFly/pixd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
pixd is a tool for visualizing binary data using a colour palette.
It is in a lot of ways akin to a hexdump tool, except using coloured
squares to represent each octet.

%prep
%setup -q

%build
make CFLAGS='%{optflags} -std=c99' %{?_smp_mflags}

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 pixd %{buildroot}%{_bindir}/pixd
install -m 0644 pixd.1 %{buildroot}%{_mandir}/man1/pixd.1

%files
%license LICENSE
%doc README.md
%{_bindir}/pixd
%{_mandir}/man1/pixd.1%{ext_man}

%changelog
