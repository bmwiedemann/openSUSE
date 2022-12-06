#
# spec file for package genders
#
# Copyright (c) 2022 SUSE LLC
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


# Check file META in sources: update so_version to (API_CURRENT - API_AGE)
%define c_api 0
%define cpp_api 2
%define slash_ver 1-28-1

Name:           genders
Version:        1.28.1
Release:        0
Summary:        Static cluster configuration database
License:        GPL-2.0-or-later
Group:          System/Management
Source:         https://github.com/chaos/genders/archive/genders-%{slash_ver}/%{name}-%{version}.tar.gz
Patch1:         Fix-Python-package-installation-use-root.patch
Patch2:         Remove-PERL_DESTDIR-use-DESTDIR-instead.patch
Patch4:         lua_bindings.patch
Patch5:         also-check-for-python3.patch
URL:            https://github.com/chaos/genders
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  patchelf
BuildRequires:  python3-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       %{name}-base

%description
Genders is a static cluster configuration database used for cluster
configuration management.  It is used by a variety of tools and
scripts for management of large clusters.  The genders database is
typically replicated on every node of the cluster. It describes the
layout and configuration of the cluster so that tools and scripts can
sense the variations of cluster nodes. By abstracting this information
into a plain text file, it becomes possible to change the
configuration of a cluster by modifying only one file.

%package base
Summary:        Base configuration for gender programs and libraries
Group:          System/Management

%description base
Base configuration files needed by the gender and libgender packages

%package perl-compat
Summary:        Perl compatibility Library
Group:          Development/Languages/Perl

%description -n %{name}-perl-compat
Perl genders API for the most part used exclusively by LLNL. It is compatible with earlier releases of genders.

%package devel
Summary:        Headers and development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
genders headers and libraries files needed for development

%package -n python3-%{name}
Summary:        Python bindings for genders
Group:          Development/Languages/Python
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name}
Requires:       %{name} = %{version}

%description -n python3-%{name}
Necessary files for using genders with Python.

%package -n lua-%{name}
Summary:        Lua bindings for genders
Group:          Development/Languages/Lua
Requires:       %{name} = %{version}
Requires:       lua

%description -n lua-%{name}
Necessary files for using genders with lua.

%package -n perl-%{name}
Summary:        Perl bindings for genders
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}
Requires:       perl-base = %{perl_version}

%description -n perl-%{name}
Necessary files for using genders with Perl.

%package -n lib%{name}%{c_api}
Summary:        C library API for genders
Group:          System/Libraries
Requires:       %{name}-base

%description -n  lib%{name}%{c_api}
This package contains the library needed to run programs dynamically linked
with genders. This is the C API.

%package -n lib%{name}plusplus%{cpp_api}
Summary:        C++ library API for genders
Group:          System/Libraries
Requires:       %{name}-base

%description -n lib%{name}plusplus%{cpp_api}
This package contains the library needed to run programs dynamically linked
with genders. This is the C++ API.

%{!?_with_perl_extensions: %{!?_without_perl_extensions: %global _with_perl_extensions --with-perl-extensions}}
%{!?_with_python_extensions: %{!?_without_python_extensions: %global _with_python_extensions --with-python-extensions}}
%{!?_with_cplusplus_extensions: %{!?_without_cplusplus_extensions: %global _with_cplusplus_extensions --with-cplusplus-extensions}}

# choose vendor arch by default
%{!?_with_perl_site_arch: %{!?_with_perl_vendor_arch: %global _with_perl_vendor_arch --with-perl-vendor-arch}}

%if %{?_with_perl_site_arch:1}%{!?_with_perl_site_arch:0}
%define _perldir %(perl -e 'use Config; $T=$Config{installsitearch}; $P=$Config{siteprefix}; $T=~/$P\\/(.*)/; print "%{_prefix}/$1\\n"')
%endif
%if %{?_with_perl_vendor_arch:1}%{!?_with_perl_vendor_arch:0}
%define _perldir %(perl -e 'use Config; $T=$Config{installvendorarch}; $P=$Config{vendorprefix}; $T=~/$P\\/(.*)/; print "%{_prefix}/$1\\n"')
%endif

%prep
%setup -c -q -n %{name}-%{version}
mv genders-genders-%{slash_ver}/* .
rm -r genders-genders-%{slash_ver}
%autopatch -p1

%build
export PYTHON=python3
aclocal --force --install -I config
libtoolize -f -i
automake -a -f
autoconf --force
export GENDERS_LIBDIR=%{_libdir}
%configure --program-prefix=%{?_program_prefix:%{_program_prefix}} \
    %{?_with_perl_extensions} \
    %{?_without_perl_extensions} \
    %{?_with_perl_site_arch} \
    %{?_without_perl_site_arch} \
    %{?_with_perl_vendor_arch} \
    %{?_without_perl_vendor_arch} \
    %{?_with_python_extensions} \
    %{?_without_python_extensions} \
    %{?_with_cplusplus_extensions} \
    %{?_without_cplusplus_extensions} \
    --with-lua-extensions \
    --without-java-extensions \
    --disable-static

make all #%%{?_smp_mflags}

%install
# turn off rpath check... causes failure on libgenders library
# is a bug in perl-ExtUtils-MakeMaker
export NO_BRP_CHECK_RPATH=true

%make_install

find "%{buildroot}" -name .packlist -exec sed -i "s#%{buildroot}##" {} +
find "%{buildroot}" -name .packlist -exec sed -i '/BUILDROOT/d'        {} +

for file in %{buildroot}%{_prefix}/lib/genders/*.pl; do grep '#!/usr/bin/perl' $file || sed -i '1s,^,#!/usr/bin/perl\n,' $file ;done

# remove .a files
%if %{?_with_cplusplus_extensions:1}%{!?_with_cplusplus_extensions:0}
rm -v %{buildroot}%{_libdir}/libgendersplusplus.la
%endif
rm -v %{buildroot}%{_libdir}/libgenders.la
find %{buildroot}%{_libdir}/lua -name \*.la -delete
mkdir -p  %{buildroot}%{_sysconfdir}
# create sample config, but remove comments
cat > %{buildroot}%{_sysconfdir}/genders <<EOF
# Sample genders file which should be the same on all nodes, with following format.
# Each line of the genders file may have one of the following formats
# The nodename(s) is the shortened[2] hostname of a node.  This is followed by
# any number of spaces or tabs, and then the comma-separated list of attributes,
# each of which can optionally have a value.  The substitution string "%n" can
# be used in an attribute value to represent the nodename.  Nodenames can be
# listed on multiple lines, so a node's attributes can be specified on multiple
# lines. However, no single node may have duplicate attributes. Genders database
# accepts ranges of nodenames in the general form: prefix[n-m,l-k,...],
# where n < m and l < k, etc., as an alternative to explicit lists of nodenames.
#
# Following is a sample genders configuration setup
#
EOF
LD_PRELOAD=%{buildroot}%{_libdir}/libgenders.so.0 %{buildroot}%{_bindir}/nodeattr -f genders.sample --compress >> %{buildroot}%{_sysconfdir}/genders

sed -i -e 's/^\([^#]\)/## \1/' %{buildroot}%{_sysconfdir}/genders
# remove rpath the hard way
brklib=$(find %{buildroot} -name Libgenders.so -print)
chmod 644 $brklib
patchelf --remove-rpath $brklib
chmod 444 $brklib

%post -n lib%{name}plusplus%{cpp_api} -p /sbin/ldconfig

%postun -n lib%{name}plusplus%{cpp_api} -p /sbin/ldconfig

%post -n lib%{name}%{c_api} -p /sbin/ldconfig

%postun -n lib%{name}%{c_api} -p /sbin/ldconfig

%files
%defattr(-,root,root)
# It doesn't matter if the user chooses a 32bit or 64bit target.  The
# packaging must work off whatever Perl is installed.
%{_mandir}/man1/*
%{_bindir}/*

%files base
%doc README NEWS ChangeLog DISCLAIMER DISCLAIMER.UC TUTORIAL genders.sample
%license COPYING
%config(noreplace) %{_sysconfdir}/genders

%files perl-compat
%dir %{_prefix}/lib/genders
%{_prefix}/lib/genders/*
%{_mandir}/man3/gendlib*

%files devel
%{_includedir}/*
%{_libdir}/libgenders.so
%if %{?_with_cplusplus_extensions:1}%{!?_with_cplusplus_extensions:0}
%{_libdir}/libgendersplusplus.so
%endif
%{_mandir}/man3/genders*
%{_mandir}/man3/libgenders*

%if %{?_with_python_extensions:1}%{!?_with_python_extensions:0}
%files -n python3-%{name}
%{_libdir}/python*
%endif

%files -n lua-%{name}
%{_libdir}/lua

%if %{?_with_perl_extensions:1}%{!?_with_perl_extensions:0}
%files -n perl-%{name}
%{_mandir}/man3/Libgenders*
%{_mandir}/man3/Genders*
%{_perldir}/*
%endif

%files -n lib%{name}%{c_api}
%{_libdir}/libgenders.so.*

%if %{?_with_cplusplus_extensions:1}%{!?_with_cplusplus_extensions:0}
%files -n lib%{name}plusplus%{cpp_api}
%{_libdir}/libgendersplusplus.so.*
%endif

%changelog
