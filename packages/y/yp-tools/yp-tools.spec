#
# spec file for package yp-tools
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yp-tools
Version:        4.2.3
Release:        0
Summary:        Network Information Service (YP) client utilities
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Networking/NIS
URL:            https://github.com/thkukuk/yp-tools
Source:         yp-tools-%{version}.tar.bz2
Source1:        match_printcap
Source2:        yp-tools.conf
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnsl) >= 1.0.4
BuildRequires:  pkgconfig(libtirpc) >= 1.0.1

%description
This packages contains some useful tools for accessing NIS maps or to
test NIS configurations.

%prep
%setup -q

%build
# Work around use of bad cast
CFLAGS="%{optflags} -Wno-error=cast-align"
%configure --disable-static --with-pic --enable-call-passwd \
	--disable-domainname
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/yp
mv %{buildroot}%{_localstatedir}/yp/nicknames %{buildroot}%{_datadir}/yp/
install -D -m 755 %{SOURCE1} %{buildroot}%{_libexecdir}/yp/match_printcap
install -D -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/yp-tools.conf
%find_lang %{name}
%fdupes %{buildroot}/%{_prefix}

%post
# Remove symlink pointing to old location (4.2.3-1.8 and older)
if [ "$1" = "2" ] && test -L %{_localstatedir}/yp/nicknames \
       && [ "$(readlink %{_localstatedir}/yp/nicknames)" = ../../usr/lib/yp/nicknames ]; then
    rm -f %{_localstatedir}/yp/nicknames
fi

%postun
if [ "$1" = "0" ]; then
   test -L %{_localstatedir}/yp/nicknames && rm -f %{_localstatedir}/yp/nicknames ||:
fi

%posttrans
if [ -z ${TRANSACTIONAL_UPDATE} ]; then
  %tmpfiles_create yp-tools.conf
fi

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_bindir}/ypcat
%{_bindir}/ypchfn
%{_bindir}/ypchsh
%{_bindir}/ypmatch
%{_bindir}/yppasswd
%{_bindir}/ypwhich
%dir %{_libexecdir}/yp
%{_libexecdir}/yp/match_printcap
%dir %{_datadir}/yp
%{_datadir}/yp/nicknames
%{_prefix}/lib/tmpfiles.d/yp-tools.conf
%{_mandir}/man1/ypcat.1%{?ext_man}
%{_mandir}/man1/ypchfn.1%{?ext_man}
%{_mandir}/man1/ypchsh.1%{?ext_man}
%{_mandir}/man1/ypmatch.1%{?ext_man}
%{_mandir}/man1/yppasswd.1%{?ext_man}
%{_mandir}/man1/ypwhich.1%{?ext_man}
%{_mandir}/man5/nicknames.5%{?ext_man}
%{_mandir}/man8/yppoll.8%{?ext_man}
%{_mandir}/man8/ypset.8%{?ext_man}
%{_mandir}/man8/yp_dump_binding.8%{?ext_man}
%{_sbindir}/yppoll
%{_sbindir}/ypset
%{_sbindir}/yp_dump_binding
%{_sbindir}/yptest

%changelog
