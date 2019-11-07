#
# spec file for package arj
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           arj
Version:        3.10.22
Release:        0
Summary:        Archiver for .arj files
License:        GPL-2.0-or-later
URL:            http://arj.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# unarj.* from Debian
Source1:        unarj.sh
Source2:        unarj.1
Patch0:         arj_3.10.22-6.diff.gz
Patch1:         arj-3.10.22-missing-protos.patch
Patch2:         arj-3.10.22-custom-printf.patch
# Filed into upstream bugtracker as https://sourceforge.net/tracker/?func=detail&aid=2853421&group_id=49820&atid=457566
Patch3:         arj-3.10.22-quotes.patch
# PATCH-FIX-OPENSUSE -- make build reproducible
Patch4:         arj-3.10.22-reproducible.patch
BuildRequires:  autoconf

%description
An implementation of an .arj archiving program. It preserves compatibility and
retains the feature set of original ARJ archiver as provided by ARJ Software,
Inc.
This open implementation is produced by the namesake, but otherwise
unaffiliated, ARJ Software Russia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

for i in debian/patches/00*.patch; do
  patch -p1 < $i
done

%build
pushd gnu
  autoconf
  %configure
popd

# Disable binary strippings
make %{?_smp_mflags} ADD_LDFLAGS=""

%install
%make_install

install -Dpm 644 resource/rearj.cfg.example %{buildroot}%{_sysconfdir}/rearj.cfg
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/unarj
install -pm 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/unarj.1

# remove the register remainders of arj's sharewares time
rm -f %{buildroot}%{_bindir}/arj-register
rm -f %{buildroot}%{_mandir}/man1/arj-register.1*

%files
%doc ChangeLog* doc/COPYING doc/rev_hist.txt
%config(noreplace) %{_sysconfdir}/rearj.cfg
%{_bindir}/arj
%{_bindir}/arjdisp
%{_bindir}/rearj
%{_bindir}/unarj
%dir %{_libdir}/arj
%{_libdir}/arj/arjcrypt.so
%{_mandir}/man1/arj.1%{ext_man}
%{_mandir}/man1/arjdisp.1%{ext_man}
%{_mandir}/man1/rearj.1%{ext_man}
%{_mandir}/man1/unarj.1%{ext_man}

%changelog
