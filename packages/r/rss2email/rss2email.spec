#
# spec file for package rss2email
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


Name:           rss2email
Version:        3.10
Release:        0
Summary:        Receive RSS feeds by email
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Languages/Python
Url:            http://pypi.python.org/pypi/rss2email/
Source:         rss2email-%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-feedparser
BuildRequires:  python3-html2text
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-feedparser
Requires:       python3-html2text
Requires:       python3-xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A free, open-source tool for Windows, Mac OS and UNIX for
getting news from RSS feeds in email. It is a simple program which you
can run in your crontab.  It watches RSS feeds and sends you nicely
formatted email message for each new item.

%prep
%setup -q -n rss2email-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -Dm644 r2e.1 %{buildroot}/%{_mandir}/man1/r2e.1

%files
%defattr(-,root,root,-)
%dir %{python3_sitelib}/rss2email
%{python3_sitelib}/rss2email/*
%dir %{python3_sitelib}/rss2email-%{version}-py*.egg-info
%{python3_sitelib}/rss2email-%{version}-py*.egg-info
%_mandir/*/r2e.1*
%doc AUTHORS CHANGELOG README.rst
%license COPYING
/usr/bin/r2e

%changelog
