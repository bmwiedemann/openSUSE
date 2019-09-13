#
# spec file for package info2html
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


Name:           info2html
BuildRequires:  apache2-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  pcre-devel
Url:            http://sourceforge.net/projects/info2html/
Provides:       inf2htm
Obsoletes:      inf2htm
Version:        2.0
Release:        0
Summary:        Program to Convert Info Pages into HTML Pages
License:        GPL-2.0+
Group:          Productivity/Publishing/Texinfo
Source0:        info2html-2.0.tar.bz2
Source1:        info2html-rpmlintrc
Source2:        arrows.tar.bz2
Patch0:         info2html-2.0.dif
%define apache_serverroot %(/usr/sbin/apxs2 -q datadir 2>/dev/null || apxs -q PREFIX)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the CGI script 'info2html' that creates HTML pages
from info documents on demand, to be sent over the HTTP protocol.

Follow references to nodes in info documents to view the corresponding info
files in HTML.


Authors:
--------
    Karl Guggisberg  <guggis@iam.unibe.ch>

%prep
%setup -n info2html-2.0 -a 2
%patch0 -b .p0

%build

%install
install -d -m 0755                $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin
install -c -m 0755 infocat        $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin/
install -c -m 0755 info2html      $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin/
install -c -m 0644 info2html.conf $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin/
install -d -m 0755                $RPM_BUILD_ROOT%{apache_serverroot}/htdocs
install -c -m 0644 info2html.css  $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/
install -d -m 0755                $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif
install -c arrows/l_arrow.gif     $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif/
install -c arrows/r_arrow.gif     $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif/
install -c arrows/u_arrow.gif     $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif/
install -c arrows/r_hand.gif      $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif/
install -c arrows/r-ball.gif      $RPM_BUILD_ROOT%{apache_serverroot}/htdocs/gif/

%files
%defattr(644,root,root,755)
%dir %{apache_serverroot}/htdocs/gif
%attr(755,root,root) %{apache_serverroot}/cgi-bin/infocat
%attr(755,root,root) %{apache_serverroot}/cgi-bin/info2html
%attr(644,root,root) %config %{apache_serverroot}/cgi-bin/info2html.conf
%attr(644,root,root) %config %{apache_serverroot}//htdocs/info2html.css
%{apache_serverroot}/htdocs/gif/l_arrow.gif
%{apache_serverroot}/htdocs/gif/r_arrow.gif
%{apache_serverroot}/htdocs/gif/r_hand.gif
%{apache_serverroot}/htdocs/gif/u_arrow.gif
%{apache_serverroot}/htdocs/gif/r-ball.gif

%changelog
