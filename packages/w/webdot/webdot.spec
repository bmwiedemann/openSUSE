#
# spec file for package webdot
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


%define cgibindir  %{apache_serverroot}/cgi-bin
%define htmldir    %{apache_serverroot}/htdocs
%define httpdconf  %(rpm -ql apache2 | grep '/uid\\\.conf$')
%define cachedir   %{_localstatedir}/cache/webdot
%define tclsh83bin %(rpm -ql tcl | grep '/tclsh$')
Name:           webdot
Version:        2.30
Release:        0
Summary:        A CGI graph server script that uses tcldot from graphviz
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://www.graphviz.org/
Source:         http://www.graphviz.org/pub/graphviz/stable/SOURCES//%{name}-%{version}.tar.gz
Patch1:         rpm-specifics.diff
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
BuildRequires:  graphviz
BuildRequires:  libapr-util1-devel
BuildRequires:  perl-GD
BuildRequires:  tcl-devel
Requires:       ghostscript
Requires:       http_daemon
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         filesystem
PreReq:         fileutils
BuildArch:      noarch

%description
A cgi-bin program that produces clickable graphs in web pages when
provided with an href to a .dot file.  Uses Tcldot from the graphviz
rpm. By default, only requests from localhost are served.

%prep
%setup -q
%patch1 -p1

%build

%install
make install						\
    DESTDIR=%{buildroot}				\
    BUILD_DIR=.						\
    CGI-BIN_DIR=%{cgibindir}				\
    HTML_DIR=%{htmldir}					\
    CACHE_DIR=%{_localstatedir}/cache				\
    HTTPD-USER-GROUP=%{apache_user}:%apache_group		\
    TCLSH_EXECUTABLE=%{tclsh83bin}			\
    GS=%(which gs)					\
    PS2EPSI=%(which ps2epsi)
rm -f %{buildroot}%{cgibindir}/webdot.tcl

%files
%license COPYING
%doc README AUTHORS CHANGES
%attr(755,root,root) %{cgibindir}/webdot
%attr(-,root,root) %{htmldir}/webdot/
%attr(700,%{apache_user},%{apache_group}) %{cachedir}/

%changelog
