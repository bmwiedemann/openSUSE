#
# spec file for package sphinx
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


%global sphinx_user sphinx
%global sphinx_group sphinx
%global daemon searchd
%global sphinx_home %{_localstatedir}/lib/sphinx
%global soname 0_0_1
# For being able to build for SLE_11
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}
%if 0%{?suse_version} > 1210
%define has_systemd 1
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
%else
Requires(pre):  %insserv_prereq
%endif
Name:           sphinx
Version:        2.2.11
Release:        0
Summary:        SQL full-text search engine
License:        GPL-2.0-only
Group:          Productivity/Databases/Servers
URL:            https://sphinxsearch.com/
Source0:        https://sphinxsearch.com/files/%{name}-%{version}-release.tar.gz
Source1:        %{daemon}.service
Source2:        %{daemon}.init
Patch0:         obs.patch
Patch2:         sphinx-default_listen.patch
Patch3:         reproducible.patch
# for fix-ups
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  mysql-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libecpg) >= 9.6
BuildRequires:  pkgconfig(libecpg_compat) >= 9.6
BuildRequires:  pkgconfig(libpgtypes) >= 9.6
BuildRequires:  pkgconfig(libpq) >= 9.6
Requires:       logrotate
Provides:       %{daemon}
Requires(pre):  %{_bindir}/getent
Requires(pre):  /usr/sbin/useradd
%if 0%{?suse_version}
Requires(post): %fillup_prereq
#Requires(pre):  permissions >= 2014.11
%else
Requires(post): /sbin/chkconfig
Requires(postun): /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
%endif
#

%description
Sphinx is a standalone search engine providing size-efficient and
relevant full-text search functions to other applications. Sphinx
integrates with SQL databases and scripting languages.

Data source drivers support fetching data either via direct
connection to MySQL, PostgreSQL, or from a pipe in a custom XML
format.

The Search API is natively ported to PHP, Python, Perl, Ruby, Java,
and also available as a pluggable MySQL storage engine.

Sphinx is an acronym which is officially decoded as SQL Phrase Index.

%package -n libsphinxclient-%{soname}
Summary:        Pure C searchd client API library
Group:          System/Libraries

%description -n libsphinxclient-%{soname}
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com/

%package -n libsphinxclient-devel
Summary:        Development libraries and header files for libsphinxclient
Group:          Development/Libraries/Other
Requires:       libsphinxclient-%{soname} = %{version}-%{release}

%description -n libsphinxclient-devel
Provides necessary development files for sphinx api and shared libs for sphinx client.
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com/

# Comment
# we don't package api language java,ruby,php,python
# upstream don't recommend their usage.

%prep
%setup -q -n "%{name}-%{version}-release"
%patch0 -p1
%patch2 -p1
%patch3 -p1

find -type d -name CVS -exec rm -Rf {} +

%build
#@todo we should move it to cmake
set -x
export pg_includes="$(pkg-config --cflags --libs libpq | sed 's,^-I,,g')"

%configure --sysconfdir=%{_sysconfdir}/%{name}/ \
    --enable-id64 \
    --with-mysql \
    --with-pgsql \
    --with-pgsql-includes="${pg_includes}" \
    --with-pgsql-libs="%{_libdir}"

make %{?_smp_mflags} VERBOSE=1

pushd api/libsphinxclient
 %configure --sysconfdir=%{_sysconfdir}/%{name}/
 make VERBOSE=1 # Not supported upstream %%{?_smp_mflags}
popd

%install
%make_install VERBOSE=1 %{?_smp_mflags}

pushd api/libsphinxclient
 %make_install VERBOSE=1 %{?_smp_mflags}
popd

find %{buildroot} "(" -name "*.a" -o -name "*.la" ")" -print -delete

# Create /var/log/sphinx
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

# Create /var/run/sphinx
mkdir -p %{buildroot}/run/%{name}

# Create /var/lib/sphinx
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data/index

# etc/sphinx.conf preparation
# Adjust sphinx*.conf.dist to our location
for CONF in %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.dist\
 %{buildroot}%{_sysconfdir}/%{name}/%{name}-min.conf.dist;
do

 sed -i 's|%{_localstatedir}/log/%{daemon}.log|%{_localstatedir}/log/%{name}/%{daemon}.log|g' ${CONF}

 sed -i 's|%{_localstatedir}/log/query.log|%{_localstatedir}/log/%{name}/query.log|g' ${CONF}

 sed -i 's|%{_localstatedir}/log/%{daemon}.pid|/run/%{name}/%{daemon}.pid|g' ${CONF}

 sed -i 's|%{_localstatedir}/data|%{_localstatedir}/lib/%{name}/data|g' ${CONF}
done

cp -v %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf{.dist,}

# Create /etc/logrotate.d/sphinx
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << EOF
%{_localstatedir}/log/%{name}/*.log {
       weekly
       rotate 10
       copytruncate
       delaycompress
       compress
       notifempty
       missingok
       create 640 %{sphinx_user} root
}
EOF

%if 0%{?has_systemd}
# Create /usr/tempfiles.d/sphinx
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf << EOF
d /run/%{name} 755 sphinx root -
EOF
%endif

# systemd vs SysVinit
mkdir -p %{buildroot}%{_sbindir}
%if 0%{?has_systemd}
  install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{daemon}.service
  ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{daemon}
%else
#SysVinit
  install -D %{SOURCE2} %{buildroot}%{_sysconfdir}/init.d/%{daemon}
 %if 0%{?suse_version}
  ln -sf %{_sysconfdir}/init.d/%{daemon} %{buildroot}%{_sbindir}/rc%{daemon}
 %endif
%endif

%pre
getent group %{sphinx_group} >/dev/null || groupadd -r %{sphinx_group}
getent passwd %{sphinx_user} >/dev/null || \
useradd -r -g %{sphinx_group} -d %{sphinx_home} -s /bin/sh \
-c "Sphinx Searchd daemon" %{sphinx_user}
%if 0%{?has_systemd}
%service_add_pre %{daemon}.service
%endif

%post
%if 0%{?has_systemd}
%service_add_post %{daemon}.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || true
%else
 %if 0%{?suse_version}
%{fillup_and_insserv -n "%{daemon}"}
 %else
   /sbin/chkconfig --add %{daemon}
 %endif
%endif
# Create empty log files with correct rights if not exist
for LOG in %{_localstatedir}/log/%{name}/%{daemon}.log\
 %{_localstatedir}/log/%{name}/query.log;
do
  if [ ! -f ${LOG} ];then
   touch ${LOG}
   chmod 0640 ${LOG}
   chown %{sphinx_user}:root ${LOG}
  fi
done

%preun
%if 0%{?has_systemd}
%service_del_preun %{daemon}.service
%{_bindir}/systemd-tmpfiles --remove %{_tmpfilesdir}/%{name}.conf || true
%else
 %if 0%{?suse_version}
%stop_on_removal %{daemon}
 %else
   if [ $1 = 0 ] ; then
     service %{daemon} stop >/dev/null 2>&1
     /sbin/chkconfig --del %{daemon}
   fi
 %endif
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{daemon}.service
%else
 %if 0%{?suse_version}
%restart_on_update %{daemon}
%insserv_cleanup
 %else
  if [ "$1" -ge "1" ] ; then
    service %{daemon} restart >/dev/null 2>&1
  fi
 %endif
%endif

%posttrans
# chown -R %%{sphinx_user}:root %%{_localstatedir}/log/sphinx/
chown -R %{sphinx_user}:%{sphinx_group} %{_localstatedir}/lib/%{name}/

%post -n libsphinxclient-%{soname} -p /sbin/ldconfig
%postun -n libsphinxclient-%{soname} -p /sbin/ldconfig

%files
%defattr(750,root,root,-)
%config %dir %{_sysconfdir}/%{name}
# Restrict rights access to conf files they can contain sql db credentials
%defattr(640,root,%{sphinx_group},-)
%config %{_sysconfdir}/%{name}/example.sql
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config %{_sysconfdir}/%{name}/%{name}.conf.dist
%config %{_sysconfdir}/%{name}/%{name}-min.conf.dist
%if 0%{?has_systemd}
%{_unitdir}/%{daemon}.service
%{_tmpfilesdir}/%{name}.conf
%ghost /run/%{name}
%else
%{_sysconfdir}/init.d/%{daemon}
%endif
%{_sbindir}/rc%{daemon}
%config %{_sysconfdir}/logrotate.d/%{name}
%attr(755,root,root) %{_bindir}/spelldump
%attr(755,root,root) %{_bindir}/indexer
%attr(755,root,root) %{_bindir}/searchd
%attr(755,root,root) %{_bindir}/indextool
%attr(755,root,root) %{_bindir}/wordbreaker
%license COPYING
%doc contrib/
%doc doc/*.html doc/*.css doc/*.txt
%doc %attr(644, root, man) %{_mandir}/man1/indexer.1*
%doc %attr(644, root, man) %{_mandir}/man1/indextool.1*
%doc %attr(644, root, man) %{_mandir}/man1/searchd.1*
%doc %attr(644, root, man) %{_mandir}/man1/spelldump.1*
%dir %attr(0750, root, %{sphinx_group}) %{_localstatedir}/log/%{name}
#Doesn't work on SLE_11 :-(
%if 0%{?suse_version} > 1230
%ghost %attr(0640, %{sphinx_user}, root) %{_localstatedir}/log/%{name}/%{daemon}.log
%ghost %attr(0640, %{sphinx_user}, root) %{_localstatedir}/log/%{name}/query.log
%endif
%dir %attr(0755, %{sphinx_user}, %{sphinx_group}) %{_localstatedir}/lib/%{name}
%dir %attr(0755, %{sphinx_user}, %{sphinx_group}) %{_localstatedir}/lib/%{name}/data
%dir %attr(0755, %{sphinx_user}, %{sphinx_group}) %{_localstatedir}/lib/%{name}/data/index

%files -n libsphinxclient-%{soname}
%license COPYING
%attr(755, root, root) %{_libdir}/libsphinxclient-0.0.1.so

%files -n libsphinxclient-devel
%license COPYING
%{_includedir}/sphinxclient.h
%{_libdir}/libsphinxclient.so

%changelog
