#
# spec file for package hexd
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


Name:           hexd
Version:        1.0.0
Release:        0
Summary:        Colourful, human-friendly hexdump tool
License:        MIT
Group:          Development/Tools/Debuggers
Url:            https://github.com/FireyFly/hexd.git
Source:         https://github.com/FireyFly/hexd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
hexd prints a human-readable hexdump of the specified files, or
standard input if omitted. Its main distinguishing feature is
the use of colours to visually indicate which range of values
an octet belongs to, aiding in spotting patterns in binary data.

%prep
%setup -q

%build
make CFLAGS='%{optflags} -std=c99' %{?_smp_mflags}

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 hexd %{buildroot}%{_bindir}/hexd
install -m 0644 hexd.1 %{buildroot}%{_mandir}/man1/hexd.1

%files
%doc README.md
%license LICENSE
%{_bindir}/hexd
%{_mandir}/man1/hexd.1%{ext_man}

%changelog
