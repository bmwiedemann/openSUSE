#
# spec file for package openwsman
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1140 || 0%{?fedora_version} > 14
%define has_systemd 1
%else
%define has_systemd 0
%endif

%if 0%{?suse_version} > 1500 || 0%{?fedora_version} > 14
%define has_firewalld 1
%else
%define has_firewalld 0
%endif

%if 0%{?suse_version} >= 1500
%define want_python3 1
%else
%define want_python3 0
%endif

Name:           openwsman
BuildRequires:  cmake >= 3.12
BuildRequires:  cunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  pam-devel
BuildRequires:  sblim-sfcc-devel
BuildRequires:  swig >= 2.0.5

BuildRequires:  perl
%if 0%{?want_python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python-devel
%endif

%if 0%{?rhel_version} > 0
#!BuildIgnore:  vim
%endif

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:  curl-devel

%if 0%{?fedora} == 16 || (0%{?centos_version}>=500 && 0%{?centos_version}<700) || (0%{?rhel_version}>=500 && 0%{?rhel_version}<700)
BuildRequires:  java-1.6.0-openjdk-devel
%else
%if (0%{?fedora} >= 17 && 0%{?fedora} < 22) || 0%{?centos_version} >= 700 || 0%{?rhel_version} >= 700
BuildRequires:  java-1.7.0-openjdk-devel
%else
BuildRequires:  java-devel
%endif
%endif

BuildRequires:  openssl-3-devel
BuildRequires:  pkgconfig
BuildRequires:  ruby

%if 0%{?fedora} + 0%{?rhel_version} + 0%{?centos_version}  > 0

%if 0%{?rhel_version} < 700
BuildRequires:  ruby-devel
%endif

BuildRequires:  ruby-libs

%endif

%if 0%{?rhel_version} >= 700 || 0%{?centos_version} >= 700 || 0%{?fedora} > 16
BuildRequires:  rubygem-rdoc
%else
BuildRequires:  ruby-rdoc
%endif

%if 0%{?fedora} > 18
BuildRequires:  rubypick
%endif

%if 0%{?fedora} > 0 || 0%{?rhel_version} >= 600  || 0%{?centos_version} >= 600
BuildRequires:  perl-devel
%endif
%endif

%if 0%{?suse_version} > 0
BuildRequires:  java-devel
# No jni_md.h on SLE10 :-/
#%%if 0%%{?suse_version} < 1100
#BuildRequires:  java-1_5_0-ibm-devel
#BuildRequires:  libgcj-devel
#BuildRequires:  update-alternatives
#%%endif

%if 0%{?suse_version} > 1500
BuildRequires:  strip-nondeterminism
%endif
%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
%else
# SLE10
BuildRequires:  curl-devel
BuildRequires:  libidn-devel
BuildRequires:  openssl-devel
%endif

%if 0%{?suse_version} > 910
%if 0%{?suse_version} < 1110
# SLE 10 has Ruby 1.8.6 and runs into http://help.rubygems.org/discussions/problems/859-trying-to-install-rubygems
BuildRequires:  rubygems <= 1.3.7
%else
BuildRequires:  rubygems
%endif
BuildRequires:  pkg-config
BuildRequires:  ruby-devel
%else
# SLE9
BuildRequires:  pkgconfig
BuildRequires:  ruby
%endif

%endif

%if 0%{?has_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif

%if 0%{?has_firewalld}
BuildRequires:  firewall-macros
%endif

Requires(pre):  sed coreutils grep /bin/hostname
Version:        2.8.1
Release:        0
# Mandriva:
# Release %%mkrel 1
URL:            http://www.openwsman.org/
Summary:        An implementation of the WS-MAN specification
License:        BSD-3-Clause AND GPL-2.0-only
Group:          System/Management
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.rpmlintrc
Source21:       %{name}.pam.rh
Source22:       %{name}.pam
Patch1:         openwsman-redhat-initscript.patch
# https://github.com/Openwsman/openwsman/commit/e619555c3484264a188396bc8b9c77c39ef47bb2
Patch2:         openwsman-gcc15.patch
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%define pamfile %{S:21}
%else
%define pamfile %{S:22}
%endif
Source3:        %{name}.SuSEfirewall2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source4:        %{name}.service
Source5:        %{name}.firewalld

%description
OpenWSMAN is an implementation of the WS-Management protocol stack.
Web Services for Management (WS-MAN) is a specification for managing
computer systems using web services standards.

%package -n libwsman1
Summary:        An implementation of the WS-MAN specification
Group:          System/Libraries
Conflicts:      libwsman3

%description -n libwsman1
OpenWSMAN is an implementation of the WS-Management protocol stack.
Web Services for Management (WS-MAN) is a specification for managing
computer systems using web services standards.

This subpackage provides the common libraries of OpenWSMAN.

%package -n libwsman_client5
Summary:        An implementation of the WS-MAN specification
Group:          System/Libraries

%description -n libwsman_client5
OpenWSMAN is an implementation of the WS-Management protocol stack.
Web Services for Management (WS-MAN) is a specification for managing
computer systems using web services standards.

This subpackage provides the client libraries of OpenWSMAN.

%package -n libwsman-devel
Summary:        Development files for OpenWSMAN
Group:          Development/Libraries/C and C++
Provides:       openwsman-devel = %{version}
Obsoletes:      openwsman-devel < %{version}
Requires:       %{name}-server = %{version}
Requires:       libwsman1 = %{version}-%{release}
Requires:       libwsman_client5 = %{version}-%{release}
Requires:       libxml2-devel
Requires:       pam-devel
Requires:       sblim-sfcc-devel

%description -n libwsman-devel
OpenWSMAN is an implementation of the WS-Management protocol stack.

This subpackage provides the header files for its libraries.

%package -n libwsman_clientpp1
Summary:        C++ bindings to the OpenWSMAN client library
Group:          System/Libraries
Provides:       openwsman-client = %{version}
Obsoletes:      openwsman-client < %{version}

%description -n libwsman_clientpp1
OpenWSMAN is an implementation of the WS-Management protocol stack.

This subpackage provides a C++ API library for OpenWSMAN.

%package -n libwsman_clientpp-devel
Summary:        C++ development files for OpenWSMAN
Group:          Development/Libraries/C and C++
Requires:       libwsman-devel = %{version}
Requires:       libwsman_clientpp1 = %{version}

%description -n libwsman_clientpp-devel
OpenWSMAN is an implementation of the WS-Management protocol stack.

Development files for the C++ interface to the OpenWSMAN client library.

%package server
Requires(pre):  sed coreutils grep diffutils /bin/hostname
%if 0%{?suse_version}
Requires(pre):  fillup
%endif
Summary:        OpenWSMAN server and service libraries
Group:          System/Management

%description server
OpenWSMAN server and service libraries.

%package server-plugin-ruby
Requires:       openwsman-server
Summary:        OpenWSMAN Server Plugin for Ruby extensions
Group:          System/Management

%description server-plugin-ruby
This package provides a OpenWSMAN server plugin to write a
WS-Management resource handler in Ruby.

%if 0%{?want_python3}
%package -n python3-%{name}
Summary:        Python3 bindings for OpenWSMAN client API
Group:          Development/Libraries/Python
Provides:       %{name}-python
%{!?python3_sitelib: %global python3_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python3_sitearch: %global python3_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?py3_requires: %define py3_requires Requires: python3}
%{py3_requires}

%description -n python3-%{name}
This package provides Python3 bindings to access the OpenWSMAN client
API.

%else

%package python
Summary:        Python bindings for OpenWSMAN client API
Group:          Development/Libraries/Python
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?py_requires: %define py_requires Requires: python}
%{py_requires}

%description python
This package provides Python bindings to access the OpenWSMAN client
API.

%endif

# RHEL7 does not have ruby-devel
%if 0%{?rhel_version} != 700

%package ruby
Requires:       ruby

# RbConfig::CONFIG["ruby_version"] is empty in Fedora > 18 !?
%if 0%{?fedora} > 18 || 0%{?rhel_version} >= 700 || 0%{?centos_version} >= 700
%{!?ruby_version: %global ruby_version %(ruby -r rbconfig -e 'print(RbConfig::CONFIG["RUBY_PROGRAM_VERSION"])')}
%else
%{!?ruby_version: %global ruby_version %(ruby -r rbconfig -e 'print(RbConfig::CONFIG["ruby_version"])')}
%endif

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires:       ruby(abi) = %{ruby_version}
%endif

%if 0%{?suse_version} > 1120
Requires:       ruby(abi) = %{ruby_version}
%endif

%if 0%{?suse_version} == 1010
%{!?ruby_sitelib: %global ruby_sitelib %(ruby -r rbconfig -e 'vd = RbConfig::CONFIG["vendorlibdir"]; print(vd ? vd : RbConfig::CONFIG["sitelibdir"])')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -r rbconfig -e 'vad = RbConfig::CONFIG["vendorarchdir"]; print(vad ? vad : RbConfig::CONFIG["sitearchdir"])')}
%else
# SLES 10 can't parse this :-/
%if 0%{?ruby_sitelib} == 0
%if (0%{?fedora} && 0%{?fedora} < 16) || (0%{?centos_version} && 0%{?centos_version}<600) || (0%{?rhel_version} && 0%{?rhel_version}<500)
# Fedora15, RHEL-5 and CentOS-5 don't have vendor lib
# CMAKE checks for "ruby -r vendor-specific" and fails
%{!?ruby_sitelib: %global ruby_sitelib %(ruby -r rbconfig -e 'print(RbConfig::CONFIG["sitelibdir"])')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -r rbconfig -e 'print(RbConfig::CONFIG["sitearchdir"])')}
%else
%{!?ruby_sitelib: %global ruby_sitelib %(ruby -r rbconfig -e 'vd = RbConfig::CONFIG["vendorlibdir"]; print(vd ? vd : RbConfig::CONFIG["sitelibdir"])')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -r rbconfig -e 'vad = RbConfig::CONFIG["vendorarchdir"]; print(vad ? vad : RbConfig::CONFIG["sitearchdir"])')}
%endif
%endif
%endif

Summary:        Ruby bindings for OpenWSMAN client API
Group:          System/Management

%description ruby
This package provides Ruby bindings to access the OpenWSMAN client API.

%package ruby-docs
Summary:        HTML documentation for OpenWSMAN Ruby bindings
Group:          Documentation/HTML
BuildArch:      noarch

%description ruby-docs
This package provides HTML documentation for the OpenWSMAN Ruby
bindings.

# - endif not rhel7
%endif

%package perl
%if 0%{?fedora}
%define perl_version %(eval "`%{__perl} -V:version`"; echo $version)
%define perl_requires perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{perl_requires}
%else
Requires:       perl = %{perl_version}
%endif
Summary:        Perl bindings for OpenWSMAN client API
Group:          System/Management

%description perl
This package provides Perl bindings to access the OpenWSMAN client API.


%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1100

%package java
Requires:       java
Requires:       libwsman1 = %{version}
Summary:        Java bindings for OpenWSMAN client API
Group:          System/Management
BuildArch:      noarch

%description java
This package provides Java bindings to access the OpenWSMAN client API.


%endif

# RHEL7 does not have ruby-devel
%if 0%{?rhel_version} != 700
%package -n winrs
Summary:        Windows Remote Shell
Group:          System/Management
Requires:       openwsman-ruby = %{version}
BuildArch:      noarch

%description -n winrs
This is a command line tool for the Windows Remote Shell protocol.
It can be used to send shell commands to remote Windows hosts.

%endif

%prep
%setup -q
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%patch -P 1 -p1
%endif
%patch -P 2 -p1

%build
rm -rf build
mkdir build
%if 0%{?fedora}
# [ curl-Bugs-1924441 ] SSL callback option with NSS-linked libcurl
# CURLOPT_SSL_CTX_FUNCTION is defined, but does not work on e.g. Fedora
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DNO_SSL_CALLBACK"
%endif
# SLES 10 needs explicit java bytecode target
%if 0%{?suse_version} == 1010 || 0%{?suse_version} == 1110
export EXPLICIT_SOURCE=1.5
export EXPLICIT_TARGET=1.5
%endif

cd build
# SLE 10 Java doesn't like EXPLICIT_TARGET any more, disable
cmake \
  -DCMAKE_INSTALL_PREFIX=/usr \
%if 0%{?suse_version} == 1010
  -DBUILD_JAVA=FALSE \
%endif
%if 0%{?want_python3}
  -DBUILD_PYTHON=FALSE \
  -DBUILD_PYTHON3=TRUE \
%else
  -DBUILD_PYTHON=TRUE \
  -DBUILD_PYTHON3=FALSE \
%endif
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
  -DCMAKE_SKIP_RPATH=1 \
  -DPACKAGE_ARCHITECTURE=`uname -m` \
  -DEXPLICIT_SOURCE="$EXPLICIT_SOURCE" \
  -DEXPLICIT_TARGET="$EXPLICIT_TARGET" \
  -DLIB=%{_lib} \
  -DBUILD_RUBY_GEM=no \
  -DBUILD_CUNIT_TESTS=on \
  ..

make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}/%{_docdir}
# don't copy ruby docs if they don't exist
[ -d build/bindings/ruby/html ] && cp -a build/bindings/ruby/html %{buildroot}/%{_docdir}/%{name}-ruby-docs

rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/plugins/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/authenticators/*.la
[ -d %{buildroot}/%{ruby_sitelib} ] && rm -f %{buildroot}/%{ruby_sitelib}/openwsmanplugin.rb
[ -d %{buildroot}/%{ruby_vendorlib} ] && rm -f %{buildroot}/%{ruby_vendorlib}/openwsmanplugin.rb

%if 0%{?has_systemd}
install -D -m 644 %{S:4} %{buildroot}/%{_unitdir}/%{name}.service
%if 0%{?suse_version} < 1600
# rcopenwsman
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
%endif
%else
# no systemd, assume sysv style init
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 755 build/etc/init/openwsmand.sh %{buildroot}/%{_sysconfdir}/init.d/openwsmand
ln -sf %{_sysconfdir}/init.d/openwsmand %{buildroot}/%{_sbindir}/rcopenwsmand
%endif

%if 0%{?has_firewalld}
mkdir -p %{buildroot}/%{_prefix}/lib/firewalld/services
install -D -m 644 %{S:5} %{buildroot}/%{_prefix}/lib/firewalld/services/%{name}.xml
%else
install -D -m 644 %{S:3} %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

#install -m 644 etc/%{name}.conf %{buildroot}/%{_sysconfdir}/%{name}
#install -m 644 etc/openwsman_client.conf %{buildroot}/%{_sysconfdir}/%{name}
#install -m 644 etc/ssleay.cnf %{buildroot}/%{_sysconfdir}/%{name}
#install -m 644 %{pamfile} %{buildroot}/%{_sysconfdir}/pam.d/%{name}

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}/%{_sysconfdir}/pam.d/%{name} %{buildroot}/%{_pam_vendordir}
# for reproducible build:
strip-nondeterminism %{buildroot}/%{_javadir}/*jar
%endif

%if 0%{?rhel_version} == 700
rm -f %{buildroot}/%{_bindir}/winrs
%endif

%post -n libwsman1 -p /sbin/ldconfig
%postun -n libwsman1 -p /sbin/ldconfig

%post -n libwsman_client5 -p /sbin/ldconfig
%postun -n libwsman_client5 -p /sbin/ldconfig

%pre server
%if 0%{?has_systemd}
if [ -f /var/lib/systemd/migrated/%{name} ]; then
%service_add_pre %{name}.service
fi
%endif
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/%{name} ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans server
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/%{name} ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
echo Server certificates length must be 2048 bits or more. Check and recreate certificates if needed.
%endif

%post server
/sbin/ldconfig
%if 0%{?has_systemd}
%service_add_post %{name}.service
%else
%if 0%{?suse_version}
%{fillup_and_insserv openwsmand}
%else
# FIXME: chkconfig?!
%endif
%endif
%if 0%{?has_firewalld}
%firewalld_reload
%endif

%preun server
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%if 0%{?suse_version}
%{stop_on_removal openwsmand}
%else
# FIXME: chkconfig?!
%endif
%endif

%postun server
rm -f /var/log/wsmand.log
/sbin/ldconfig
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%if 0%{?suse_version}
%{restart_on_update openwsmand}
%{insserv_cleanup openwsmand}
%else
# FIXME: chkconfig?!
%endif
%endif

%post -n libwsman_clientpp1 -p /sbin/ldconfig

%postun -n libwsman_clientpp1 -p /sbin/ldconfig

%files -n libwsman1
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.md TODO src/plugins/redirect/redirect-README
%license COPYING
%{_libdir}/libwsman.so.*
%{_libdir}/libwsman_curl_client_transport.so.*

%files -n libwsman_client5
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_libdir}/libwsman_client.so.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/openwsman_client.conf

%files -n libwsman-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%exclude %{_includedir}/%{name}/cpp/*.h
%exclude %{_libdir}/libwsman_clientpp.so

%if 0%{?want_python3}
%files -n python3-%{name}
%defattr(-,root,root)
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%else

%files python
%defattr(-,root,root)
%{python_sitearch}/*.so
%{python_sitearch}/*.py*
%endif

# RHEL7 does not have ruby-devel
%if 0%{?rhel_version} != 700
%files ruby
%defattr(-,root,root)
%if 0%{?mandriva_version}
%{ruby_sitearchdir}/_openwsman.so
%dir %{ruby_sitelibdir}/%{name}
%{ruby_sitelibdir}/openwsman.rb
%{ruby_sitelibdir}/%{name}/*.rb
%else
%{ruby_sitearch}/_openwsman.so
%dir %{ruby_sitelib}/%{name}
%{ruby_sitelib}/openwsman.rb
%{ruby_sitelib}/%{name}/*.rb
%endif

%files ruby-docs
%defattr(-,root,root)
%dir %{_docdir}/%{name}-ruby-docs
%{_docdir}/%{name}-ruby-docs
# - endif not rhel-7
%endif

%files perl
%defattr(-,root,root)
%{perl_vendorarch}/%{name}.so
%{perl_vendorlib}/%{name}.pm

%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1100

%files java
%defattr(-,root,root)
%{_javadir}/*jar
%endif

%files server
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/ssleay.cnf
%attr(0755,root,root) %{_sysconfdir}/%{name}/owsmangencert.sh
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/%{name}
%else
%config %{_sysconfdir}/pam.d/%{name}
%endif
%if 0%{?has_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml
%else
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%if 0%{?suse_version} < 1600
%{_sbindir}/rc%{name}
%endif
%else
%attr(0755,root,root) %{_sysconfdir}/init.d/openwsmand
%{_sbindir}/rc%{name}d
%endif
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/authenticators
%{_libdir}/%{name}/authenticators/*.so
%{_libdir}/%{name}/authenticators/*.so.*
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*.so
%{_libdir}/%{name}/plugins/*.so.*
%exclude %{_libdir}/%{name}/plugins/*ruby*.so*
%{_sbindir}/openwsmand
%{_libdir}/libwsman_server.so.*

# RHEL7 does not have ruby-devel
%if 0%{?rhel_version} != 700
%files server-plugin-ruby
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*ruby*.so
%endif

%files -n libwsman_clientpp1
%defattr(-,root,root)
%{_libdir}/libwsman_clientpp.so.*

%files -n libwsman_clientpp-devel
%defattr(-,root,root)
%{_libdir}/libwsman_clientpp.so
%dir %{_includedir}/%{name}/cpp
%{_includedir}/%{name}/cpp/*.h

# RHEL7 does not have ruby-devel
%if 0%{?rhel_version} != 700
%files -n winrs
%defattr(-,root,root)
%{_bindir}/winrs
%endif

%changelog
