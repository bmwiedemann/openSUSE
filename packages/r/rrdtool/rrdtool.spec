#
# spec file for package rrdtool
#
# Copyright (c) 2023 SUSE LLC
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


%define python python
%if 0%{?suse_version} >= 1500
 %define python python3
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without  lua
%bcond_without  python
%bcond_without  ruby
%bcond_without  tcl
%bcond_without  libdbi
%bcond_without  libwrap
%bcond_with     rados
Name:           rrdtool
Version:        1.8.0
Release:        0
Summary:        Round Robin Database Tool to store and display time-series data
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://oss.oetiker.ch/rrdtool/
Source0:        https://github.com/oetiker/%{name}-1.x/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source2:        sysconfig.rrdcached
Source4:        rrdcached-systemd-pre
Source5:        rrdcached.service
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM -- Fix BUILD_DATE in rrdtool help output (fix segfault)
# https://github.com/oetiker/rrdtool-1.x/commit/e59f703bbcc0af949ee365206426b6394c340c6f.patch
Patch1:         e59f703bbcc0af949ee365206426b6394c340c6f.patch
# PATCH-FIX-UPSTREAM -- Prevent possible segfault
Patch3:         rrdtool-tclsegfault.patch
# PATCH-FIX-UPSTREAM -- bnc#793636
Patch12:        rrdtool-zero_vs_nothing.patch
# Needed for tests
BuildRequires:  bc
BuildRequires:  cairo-devel >= 1.2
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  groff
BuildRequires:  intltool >= 0.35.0
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pango-devel >= 1.14
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       dejavu
Patch14:        harden_rrdcached.service.patch
%if %{with python}
BuildRequires:  %{python}-devel
BuildRequires:  %{python}-setuptools
%endif
%if %{with lua}
BuildRequires:  lua-devel
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
%endif
%if %{with tcl}
BuildRequires:  tcl-devel >= 8.0
%endif
%if %{with libdbi}
BuildRequires:  libdbi-devel
%endif
%if %{with libwrap}
BuildRequires:  tcpd-devel
%endif
%if %{with rados}
BuildRequires:  librados2-devel
%endif

%description
RRD stands for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%package -n librrd8
Summary:        Round Robin Database tool library
Group:          System/Libraries

%description -n librrd8
RRD stands for Round Robin Database. RRD is a system to store and
display time-series data.

%package devel
Summary:        RRDtool header files
Group:          Development/Libraries/C and C++
Requires:       librrd8 = %{version}-%{release}

%description devel
RRD stands for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to build programs making
use of the library.

%package doc
Summary:        Documentation for rrdtool
Group:          Documentation/Howto

%description doc
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

%package -n perl-%{name}
Summary:        Perl bindings for RRDtool
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}-%{release}
Requires:       perl = %{perl_version}

%description -n perl-%{name}
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

This package contains the Perl bindings.

%if %{with lua}
%package -n lua-%{name}
Summary:        Lua bindings for RRDtool
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}

%description -n lua-%{name}
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

This package contains the Lua bindings.
%endif

%if %{with python}
%package -n %{python}-%{name}
Summary:        Python bindings for RRDtool
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
Requires:       %{python}

%description -n %{python}-%{name}
Python RRDtool bindings.
%endif

%if %{with ruby}
%package -n ruby-%{name}
Summary:        Ruby bindings for RRDtool
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}-%{release}
Requires:       ruby(abi) >= %{rb_ver}

%description -n ruby-%{name}
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

This package contains the Ruby bindings.
%endif

%if %{with tcl}
%package -n tcl-%{name}
Summary:        Tcl bindings for RRDtool
Group:          Development/Languages/Tcl
Requires:       %{name} = %{version}-%{release}
Requires:       tcl >= 8.0

%description -n tcl-%{name}
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

This package contains the Tcl bindings.
%endif

%package cached
%define         rrdcached_user  rrdcached
%define         rrdcached_group rrdcached
Summary:        Data caching daemon for RRDtool
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}-%{release}
Requires(post): %fillup_prereq
Requires(pre):  shadow

%description cached
rrdcached is a daemon that receives updates to existing RRD files,
accumulates them and, if enough have been received or a defined time has
passed, writes the updates to the RRD file.  The daemon was written with
big setups in mind which usually runs into I/O related problems.  This
daemon was written to alleviate these problems.

%prep
%setup -q
%patch1 -p1
%patch3
%patch12 -p1
%patch14 -p1

# rrd_tool/rrd_cgi: use the date of the last change
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -name '*.c' -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" "{}" "+"

%build
# we are patching configure, we need to reconf
autoreconf -fi

# --disable-nls: there is only partial hungarian translation, does not make %{?_smp_mflags}
#                much sense to ship package for it
%configure \
        --disable-nls \
        --disable-silent-rules \
        --enable-shared \
        --disable-static\
        --disable-rpath \
%if %{with lua}
        --enable-lua \
        --enable-lua-site-install \
%else
        --disable-lua \
%endif
        --enable-perl \
        --enable-perl-site-install \
        --with-perl-options='INSTALLDIRS="vendor"' \
%if %{with python}
        --enable-python \
%else
        --disable-python \
%endif
%if %{with ruby}
        --enable-ruby \
        --enable-ruby-site-install \
        --with-ruby-options='sitedir="%{rb_sitearchdir}"' \
%else
        --disable-ruby \
%endif
%if %{with tcl}
        --enable-tcl \
        --enable-tcl-site \
        --with-tcllib=%{_libdir} \
%else
        --disable-tcl \
%endif
        --with-rrd-default-font="monospace" \
        --with-pic \
        --with-gnu-ld \
        --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}

%install
make \
        DESTDIR=%{buildroot} \
        idocdir=%{_docdir}/%{name}/txt/ \
        ihtmldir=%{_docdir}/%{name}/html/ \
        examplesdir=%{_docdir}/%{name}/examples/ \
        libdir=%{_libdir} \
%if %{with tcl}
        pkglibdir=%{tcl_archdir}/tclrrd%{version} \
%endif
        install

%perl_process_packlist

%if %{with lua}
# Move lua lib to the right point, in case lua did not expose the right INSTALL_CMOD variable
mv %{buildroot}%{_prefix}/local/lib/lua %{buildroot}%{_libdir}/lua || true
%endif

%if %{with ruby}
install -D bindings/ruby/RRD.so %{buildroot}%{rb_sitearchdir}/RRD.so
%endif

# remove cruft
find %{buildroot} -type f -name "*.la" -delete -print

# documentation
rm %{buildroot}%{_docdir}/%{name}/txt/*.pod
find %{buildroot}%{_docdir}/%{name}/examples/ -type f -exec chmod 0644 "{}" "+"

# install rrdcached specials
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.rrdcached

# install systemd specific files
install -D -m 0755 %{SOURCE4} %{buildroot}%{_datadir}/rrdcached/rrdcached-systemd-pre
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/rrdcached.service
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
echo "d /run/rrdcached 0755 %{rrdcached_user} %{rrdcached_group}" > %{buildroot}%{_tmpfilesdir}/rrdcached.conf
chmod 644 %{buildroot}%{_tmpfilesdir}/rrdcached.conf

mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrrdcached

%check
# Follow upstream, disable the following, failing tests: rpn1
# https://github.com/oetiker/rrdtool-1.x/blob/master/.travis.yml#L30
make %{?_smp_mflags} check TESTS="modify1 modify2 modify3 modify4 modify5 rpn2 xport1 \
tune1 tune2 graph1 rrdcreate dump-restore create-with-source-1 create-with-source-2 \
create-with-source-3 create-with-source-4 create-with-source-and-mapping-1 \
create-from-template-1 dcounter1 vformatter1 list1 pdp-calc1"

%pre cached
getent group %{rrdcached_group} >/dev/null || groupadd %{rrdcached_group}
getent passwd %{rrdcached_user} >/dev/null || useradd -s /sbin/nologin -g %{rrdcached_group} -c %{rrdcached_user} -d %{_localstatedir}/lib %{rrdcached_user}
%service_add_pre rrdcached.service rrdcached.socket

%post cached
%fillup_only rrdcached
%service_add_post rrdcached.servicet rrdcached.socket
%tmpfiles_create %{_tmpfilesdir}/rddcached.conf

%preun cached
%service_del_preun rrdcached.service rrdcached.socket

%postun cached
%service_del_postun rrdcached.service rrdcached.socket

%post   -n librrd8 -p /sbin/ldconfig
%postun -n librrd8 -p /sbin/ldconfig

%files
%exclude %{_docdir}/%{name}
%{_mandir}/*/*
%exclude %{_mandir}/man1/rrdcached*
%exclude %{_mandir}/man3/RRD*
%{_bindir}/*
%exclude %{_bindir}/rrdcached

%files -n librrd8
%{_libdir}/librrd.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/librrd.so
%{_libdir}/pkgconfig/librrd.pc

%files doc
%doc CONTRIBUTORS COPYRIGHT NEWS THREADS TODO
%doc %{_docdir}/rrdtool
%exclude %{_docdir}/rrdtool/html/RRD*.html

%files -n perl-%{name}
%doc %{_docdir}/rrdtool/html/RRD*.html
%{_mandir}/man3/RRD*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%{perl_vendorarch}/auto/*

%if %{with lua}
%files -n lua-%{name}
%doc bindings/lua/README
%dir %{_libdir}/lua
%dir %{_libdir}/lua/*
%{_libdir}/lua/*/rrd.so
%{_libdir}/lua/*/rrd.so.*
%endif

%if %{with python}
%files -n %{python}-%{name}
%license bindings/python/COPYING
%doc bindings/python/README.md
%if 0%{?suse_version} >= 1500
%{python3_sitearch}/*
%else
%{python_sitearch}/*
%endif
%endif

%if %{with ruby}
%files -n ruby-%{name}
%doc bindings/ruby/README
%{rb_sitearchdir}/RRD.so
%endif

%if %{with tcl}
%files -n tcl-%{name}
%doc bindings/tcl/README
%{tcl_archdir}/*
%{_libdir}/tclrrd*.so
%endif

%files cached
%{_mandir}/man1/rrdcached*
%{_bindir}/rrdcached
%{_sbindir}/rcrrdcached
%{_fillupdir}/sysconfig.rrdcached
%{_datadir}/rrdcached
%{_datadir}/rrdcached/rrdcached-systemd-pre
%{_unitdir}/rrdcached.service
%{_unitdir}/rrdcached.socket
%if 0%{?suse_version} <= 1320
%dir %{_libexecdir}/tmpfiles.d
%endif
%{_tmpfilesdir}/rrdcached.conf
%ghost /run/rrdcached

%changelog
