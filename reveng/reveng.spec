#
# spec file for package reveng
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           reveng
Version:        2.0.0
Release:        0
Summary:        An arbitrary-precision CRC calculator and algorithm finder
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://reveng.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:         reveng-dont-strip.patch
Patch1:         reveng-obey-cflags.patch
Patch2:         reveng-presets_x86_64.patch
Patch3:         reveng-presets_i386.patch

%description
CRC RevEng is an arbitrary-precision CRC calculator and
algorithm finder. It calculates CRCs using any of the 72 preset
algorithms, or a user-specified algorithm to any width. It calculates
reversed CRCs to give the bit pattern that produces a desired forward
CRC. CRC RevEng also reverse-engineers any CRC algorithm from
sufficient correctly formatted message-CRC pairs and optional known
parameters. It comprises input interpretation options.
It is compliant with Ross Williams' Rocksoft model of parametrised CRC
algorithms.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%ifarch x86_64
%patch2 -p1
%endif
%ifarch %ix86
%patch3 -p1
%endif

%build
%ifarch %{ix86} x86_64
export CFLAGS="%{optflags}"
make %{?_smp_mflags}
%else
gcc %{optflags} -Wall -ansi -c bmpbit.c cli.c model.c poly.c preset.c reveng.c
gcc %{optflags} -o reveng bmpbit.o cli.o model.o poly.o preset.o reveng.o
%endif

%install
install -Dpm 0755 reveng %{buildroot}/%{_bindir}/reveng

%files
%license COPYING
%doc CHANGES README
%{_bindir}/reveng

%changelog
