#
# spec file for package htdig
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


%define apache_serverroot %(%{_sbindir}/apxs2 -q datadir 2>/dev/null || %{_sbindir}/apxs2 -q PREFIX)
Name:           htdig
Version:        3.2.0b6
Release:        0
Summary:        WWW Index and Search System
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.htdig.org
Source:         http://switch.dl.sourceforge.net/sourceforge/htdig/htdig-%{version}.tar.bz2
Source1:        %{name}-README.SUSE
Patch1:         %{name}-google-style.patch
Patch2:         %{name}-rundig.patch
Patch3:         %{name}-ExternalParser-typo.patch
Patch4:         %{name}-SSLConnection.patch
Patch5:         %{name}-simpleUTF8.patch
Patch8:         %{name}-cleanup-db.diff
Patch9:         %{name}-cross-site-CAN-2005-0085.patch
Patch10:        %{name}-3.2.0b6-strictaliasing.diff
Patch11:        htsearch-gcc41.patch
Patch14:        %{name}-quoting.patch
# PATCH-FIX-UPSTREAM gmtime-lastday.patch use INT32_MAX to define last day (bnc##231196), related to (bnc#343913)
Patch15:        %{name}-gmtime-lastday.patch
# PATCH-FIX-UPSTREAM htdig-unsigned-char.patch dimstar@opensuse.org -- use unsigned char to be sure we can store values up to (int)255
Patch16:        %{name}-unsigned-char.patch
Patch17:        htdig-gcc7.patch
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libapr-util1-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  postfix
BuildRequires:  rrdtool
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ht://Dig system is a complete World Wide Web index and search
system for a small domain or intranet. This system is not meant to
replace the need for powerful Internet-wide search systems like Lycos,
Infoseek, Webcrawler, or AltaVista. Instead it is meant to cover the
search needs of a single company, campus, or even a particular
subsection of a Web site.

Unlike some WAIS-based or Web server-based search engines, ht://Dig can
span several Web servers at a site. The type of these Web servers does
not matter as long as they understand the HTTP 1.0 protocol.

%package devel
Summary:        Development files for htdig
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
The ht://Dig system is a complete World Wide Web index and search
system for a small domain or intranet. This system is not meant to
replace the need for powerful Internet-wide search systems like Lycos,
Infoseek, Webcrawler, or AltaVista. Instead it is meant to cover the
search needs of a single company, campus, or even a particular
subsection of a Web site.

This package is needed if you want to develop other applications on
htdig.

%package doc
Summary:        WWW Index and Search System Documentation
Group:          Productivity/Networking/Web/Utilities
Requires:       %{name} = %{version}

%description doc
The ht://Dig system is a complete World Wide Web index and search
system for a small domain or intranet. This system is not meant to
replace the need for powerful Internet-wide search systems like Lycos,
Infoseek, Webcrawler, or AltaVista. Instead it is meant to cover the
search needs of a single company, campus, or even a particular
subsection of a Web site.

This package provides additional documentation for htdig in
%{_docdir}/htdig/

%prep
%setup -q
cp %{SOURCE1} README.SUSE
%patch1
%patch2
%patch3
%patch4
%patch5
%patch8 -p 1
%patch9 -p1
%patch10 -p1
%patch11
%patch14 -p1
%patch15
%patch16 -p1
%patch17 -p1
%build
%{?suse_update_config:%{suse_update_config -f db/dist}}
pushd contrib 1>/dev/null
find . -type f | xargs -n 1 sed -i "s@%{_prefix}/local/bin/perl@%{_bindir}/perl@"
popd 1>/dev/null
rm -f acconfig.h db/dist/acconfig.h aclocal.m4 configure db/dist/configure
autoreconf --force --install
%configure \
   --with-config-dir=%{_sysconfdir}/htdig \
   --with-common-dir=%{apache_serverroot}/htdig/common \
   --with-database-dir=%{_localstatedir}/lib/htdig/db \
   --with-cgi-bin-dir=%{apache_serverroot}/cgi-bin \
   --with-image-dir=%{apache_serverroot}/htdig/images \
   --with-image-url-prefix=images \
   --with-search-dir=%{apache_serverroot}/htdig \
   --with-ssl \
   --with-zlib \
   --enable-bigfile \
   --disable-static
make %{?_smp_mflags}

%install
find . -name \*.orig -o -name .cvsignore | xargs rm  -f
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# remove static libs as nobody uses them
find %{buildroot}/%{_libdir}/ -name *.*a | xargs rm  -f
pushd %{buildroot}/%{_sysconfdir}/htdig 1>/dev/null
# try to use only one mime.types file (from aaa_base) for the distri
rm mime.types
ln -s ../mime.types mime.types
# adapt the htdig.conf file
sed -e "s@start_url:.*http://www.htdig.org/@start_url:      http://localhost/@g" htdig.conf > htdig.conf.new
mv htdig.conf.new htdig.conf
popd 1>/dev/null
# install the documentation files in the right directory
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/
pushd %{_builddir}/%{name}-%{version} 1>/dev/null
cp -a contrib %{buildroot}/%{_defaultdocdir}/%{name}/
cp -a htdoc %{buildroot}/%{_defaultdocdir}/%{name}/
cp COPYING ChangeLog README* STATUS %{buildroot}/%{_defaultdocdir}/%{name}/

%files devel
%defattr(-,root,root)
%dir %{_includedir}/htdig
%dir %{_includedir}/htdig_db
%{_includedir}/htdig/*
%{_includedir}/htdig_db/*

%files doc
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/contrib
%doc %{_defaultdocdir}/%{name}/htdoc
#disable execute permission
%attr(644, root, root) %{_defaultdocdir}/%{name}/htdoc/cf_generate.pl
#delete Makefile waste from doc
%exclude %{_defaultdocdir}/%{name}/htdoc/Makefile*

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*
%exclude %{_defaultdocdir}/%{name}/contrib
%exclude %{_defaultdocdir}/%{name}/htdoc
%config(noreplace) %{_sysconfdir}/htdig
%dir %{apache_serverroot}/htdig
%{apache_serverroot}/htdig/search.html
%{apache_serverroot}/htdig/common
%{apache_serverroot}/htdig/images
%dir %{_localstatedir}/lib/htdig
%{_localstatedir}/lib/htdig/db
%{apache_serverroot}/cgi-bin/htsearch
%{apache_serverroot}/cgi-bin/qtest
%{_mandir}/*/*
%{_libdir}/h*
%{_bindir}/*

%changelog
