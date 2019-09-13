#
# spec file for package gup
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gup
Version:        0.3
Release:        0
Summary:        Group Update Program for INN and C-News
License:        SUSE-Public-Domain
Group:          Productivity/Networking/News/Utilities
Source:         gup.tar.gz
Patch0:         gup.dif
Patch1:         gup-fdleak.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       inn
%if 0%{?suse_version} >= 1330
Requires(pre):  group(news)
Requires(pre):  user(news)
%endif

%description
A Group Update Program that accepts commands by mail to edit a
newsgroup subscription file.  It can be used by news systems such as
INN and C-News.

%prep
%setup -n gup
%patch0
%patch1

%build
export RPM_OPT_FLAGS
make all %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/news/bin
install gup sample/{gupdate,gupadd,gupverify} $RPM_BUILD_ROOT/usr/lib/news/bin/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 gup.1 $RPM_BUILD_ROOT%{_mandir}/man1/
var=/var/lib/news/gup
mkdir -p $RPM_BUILD_ROOT$var/sites $RPM_BUILD_ROOT$var/default
install -m 600 sample/config $RPM_BUILD_ROOT$var
install -m 644 sample/{gup_headers,gupconfig,newsfeeds.{start,end}} $RPM_BUILD_ROOT$var
install -m 644 sample/default/{exclude,groups,header,trailer} $RPM_BUILD_ROOT$var/default/
touch $RPM_BUILD_ROOT$var/log
chmod 600 $RPM_BUILD_ROOT$var/log

%files
%defattr(-,root,root)
%doc README README.linux
%dir /usr/lib/news
%dir /usr/lib/news/bin
/usr/lib/news/bin/gup
/usr/lib/news/bin/gupadd
/usr/lib/news/bin/gupdate
/usr/lib/news/bin/gupverify
%{_mandir}/man1/gup.1.gz
%defattr(-,news,news)
%dir /var/lib/news
%dir /var/lib/news/gup
%dir /var/lib/news/gup/default
%dir /var/lib/news/gup/sites
%config(noreplace) /var/lib/news/gup/config
/var/lib/news/gup/default/exclude
/var/lib/news/gup/default/groups
/var/lib/news/gup/default/header
/var/lib/news/gup/default/trailer
/var/lib/news/gup/gup_headers
%config(noreplace) /var/lib/news/gup/gupconfig
%ghost /var/lib/news/gup/log
/var/lib/news/gup/newsfeeds.end
/var/lib/news/gup/newsfeeds.start

%changelog
