#
# spec file for package apache2-mod_encoding
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


%define snapshot 20021209
%define mod_name mod_encoding
%define mod_conf httpd-encoding.conf
%define mod_so %{mod_name}.so
Name:           apache2-%{mod_name}
Version:        0.0.%{snapshot}
Release:        0
Summary:        Non-ASCII filename interoperability module for the Apache web server
# not exactly OpenSSL license, but similar
License:        OpenSSL
Group:          Productivity/Networking/Web/Servers
Url:            http://webdav.todo.gr.jp/
Source0:        mod_encoding-%{version}.tar.bz2
Source1:        %{mod_conf}
Patch0:         mod_mod_encoding-0.0.20021209-apache220.diff
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  file
BuildRequires:  openssl-devel
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2 >= 2.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package -n libiconv_hook1
Summary:        Extension of iconv for libapache-mod-encoding
Group:          System/Libraries

%package -n libiconv_hook-devel
Summary:        Header files of libiconv-hook
Group:          Development/Libraries/C and C++
Requires:       libiconv_hook1 = %version

%description
mod_encoding is an Apache module for improved non-ASCII filename
interoperability (and for mod_dav).

%description -n libiconv_hook1
This code is an iconv-compatible interface routine for mod_encoding.

%description -n libiconv_hook-devel
Development and header files for libiconv_hook1

%prep
%setup -q -n mod_encoding-%{snapshot}
%patch0  -b .apache220

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
pushd lib
[ -r iconv.h ] && rm -f iconv.h
%configure --with-apxs=%{apache_apxs} --with-iconv-hook --with-openssl --disable-static
# --enable-shared=no
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"
ln -s -f  iconv.h.replace iconv.h
popd

cp -a lib/.libs/libiconv_hook.so* .

%{apache_apxs} -c -I$PWD/lib -L. -liconv_hook %{mod_name}.c

%install
pushd lib
%{make_install}
rm %{buildroot}%{_libdir}/libiconv_hook.la
popd
mkdir -p %{buildroot}/%{apache_libexecdir}
mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
cp -p .libs/%{mod_name}.so %{buildroot}/%{apache_libexecdir}
cp -p %{SOURCE1} %{buildroot}/%{apache_sysconfdir}/conf.d/

%post   -n libiconv_hook1 -p /sbin/ldconfig
%postun -n libiconv_hook1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%attr(0644,root,root) %config(noreplace) %{apache_sysconfdir}/conf.d/%{mod_conf}
%{apache_libexecdir}/%{mod_name}.so

%files -n libiconv_hook1
%defattr(-,root,root)
%{_libdir}/libiconv_hook.so.1
%{_libdir}/libiconv_hook.so.1.0.0

%files -n libiconv_hook-devel
%defattr(-,root,root)
%dir %{_includedir}/iconv_hook
%{_includedir}/iconv_hook/iconv.h
%{_includedir}/iconv_hook/iconv_hook.h
%{_libdir}/libiconv_hook.so

%changelog
