#
# spec file for package webdot
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           webdot
BuildRequires:  apache2-devel
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
BuildRequires:  graphviz
BuildRequires:  libapr-util1-devel
BuildRequires:  perl-GD
BuildRequires:  tcl-devel
Version:        2.30
Release:        0
Requires:       ghostscript
Requires:       http_daemon
Summary:        A CGI graph server script that uses tcldot from graphviz
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Graph
Source:         http://www.graphviz.org/pub/graphviz/stable/SOURCES//%{name}-%{version}.tar.gz
Patch1:         rpm-specifics.diff
Url:            http://www.graphviz.org/
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         filesystem fileutils
%define apache_serverroot %(/usr/sbin/apxs2 -q datadir 2>/dev/null || /usr/sbin/apxs -q PREFIX)
%define cgibindir  %apache_serverroot/cgi-bin
%define htmldir    %apache_serverroot/htdocs
%define httpdconf  %(rpm -ql apache2 | grep '/uid\\\.conf$')
%define apacheuser %(grep -i '^user ' %{httpdconf} | awk '{print $2}')
%define apachegroup nogroup
%define cachedir   /var/cache/webdot
%define tclsh83bin %(rpm -ql tcl | grep '/tclsh$')

%description
A cgi-bin program that produces clickable graphs in web pages when
provided with an href to a .dot file.  Uses Tcldot from the graphviz
rpm. By default, only requests from localhost are served.



Authors:
--------
    John Ellson <ellson@lucent.com>

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build

%install
make install						\
    DESTDIR=$RPM_BUILD_ROOT				\
    BUILD_DIR=.						\
    CGI-BIN_DIR=%{cgibindir}				\
    HTML_DIR=%{htmldir}					\
    CACHE_DIR=/var/cache				\
    HTTPD-USER-GROUP=%apacheuser:%apachegroup		\
    TCLSH_EXECUTABLE=%tclsh83bin			\
    GS=%(which gs)					\
    PS2EPSI=%(which ps2epsi)
rm -f $RPM_BUILD_ROOT%{cgibindir}/webdot.tcl

%files
%defattr(-,root,root)
%doc COPYING README AUTHORS CHANGES
%attr(755,root,root) %{cgibindir}/webdot
%attr(-,root,root) %{htmldir}/webdot/
%attr(700,%{apacheuser},%{apachegroup}) %{cachedir}/

%changelog
