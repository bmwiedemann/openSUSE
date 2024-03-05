#
# spec file for package gup
#
# Copyright (c) 2024 SUSE LLC
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


%define _buildshell /bin/bash
Name:           gup
Version:        0.3
Release:        0
Summary:        Group Update Program for INN and C-News
License:        SUSE-Public-Domain
Group:          Productivity/Networking/News/Utilities
Source:         gup.tar.gz
Patch0:         gup.dif
Patch1:         gup-fdleak.dif
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
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{PATCH0}
%patch -P 0
%patch -P 1

%build
export RPM_OPT_FLAGS
make all %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_libexecdir}/news/bin
install gup sample/{gupdate,gupadd,gupverify} %{buildroot}/%{_libexecdir}/news/bin/
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 gup.1 %{buildroot}/%{_mandir}/man1/
var=/var/lib/news/gup
mkdir -p %{buildroot}/$var/sites %{buildroot}/$var/default
install -m 600 sample/config %{buildroot}/$var
install -m 644 sample/{gup_headers,gupconfig,newsfeeds.{start,end}} %{buildroot}/$var
install -m 644 sample/default/{exclude,groups,header,trailer} %{buildroot}/$var/default/
touch %{buildroot}/$var/log
chmod 600 %{buildroot}/$var/log

%files
%doc README README.linux
%dir %{_libexecdir}/news
%dir %{_libexecdir}/news/bin
%{_libexecdir}/news/bin/gup
%{_libexecdir}/news/bin/gupadd
%{_libexecdir}/news/bin/gupdate
%{_libexecdir}/news/bin/gupverify
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
