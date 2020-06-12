#
# spec file for package mawk
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 Guido Berhoerster.
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


%define _upver 1.3.4
%define _datever 20200120
Name:           mawk
Version:        %{_upver}.%{_datever}
Release:        0
Summary:        Implementation of New/POSIX AWK
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            http://invisible-island.net/mawk/mawk.html
Source0:        ftp://ftp.invisible-island.net/mawk/mawk-%{_upver}-%{_datever}.tgz
Source1:        ftp://ftp.invisible-island.net/mawk/mawk-%{_upver}-%{_datever}.tgz.asc
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE -- bmwiedemann -- drop timestamp / for build-compare
Patch0:         reproducible.patch
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
mawk is an interpreter for the AWK Programming Language. It implements the AWK
language as defined in Aho, Kernighan and Weinberger, The AWK  Programming
Language, Addison-Wesley Publishing, 1988. Furthermore, it conforms to the
POSIX 1003.2 (draft 11.3) definition of the AWK language and additionally
provides a small number of extensions.

%prep
%setup -q -n mawk-%{_upver}-%{_datever}
%patch0 -p1
chmod 755 examples/*

%build
# without --enable-warnings several functions will not be marked with gcc's
# noreturn attribute and produce warnings when $RPM_OPT_FLAGS contains -Wall
%configure \
  --enable-warnings
make %{?_smp_mflags}

%install
%make_install

# compatibility symlink
install -d -m 755 %{buildroot}/bin
ln -s %{_bindir}/mawk %{buildroot}/bin/mawk
# create symlinks for update-alternatives
install -d -m 755 %{buildroot}%{_sysconfdir}/alternatives
ln -s %{_sysconfdir}/alternatives/awk %{buildroot}/bin/awk
ln -s %{_sysconfdir}/alternatives/usr-bin-awk %{buildroot}%{_bindir}/awk
ln -s %{_sysconfdir}/alternatives/awk.1%{?ext_man} %{buildroot}%{_mandir}/man1/awk.1%{?ext_man}

%check
make %{?_smp_mflags} check

%post
%{_sbindir}/update-alternatives \
  --install /bin/awk awk %{_bindir}/mawk 15 \
  --slave %{_bindir}/awk usr-bin-awk %{_bindir}/mawk \
  --slave %{_mandir}/man1/awk.1.gz awk.1%{?ext_man} %{_mandir}/man1/mawk.1%{?ext_man}

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove awk %{_bindir}/mawk
fi

%files
%license COPYING
%doc ACKNOWLEDGMENT CHANGES README examples/
/bin/mawk
%{_bindir}/mawk
%{_mandir}/man1/mawk.1%{?ext_man}
/bin/awk
%{_bindir}/awk
%{_mandir}/man1/awk.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/awk
%ghost %{_sysconfdir}/alternatives/usr-bin-awk
%ghost %{_sysconfdir}/alternatives/awk.1%{?ext_man}

%changelog
