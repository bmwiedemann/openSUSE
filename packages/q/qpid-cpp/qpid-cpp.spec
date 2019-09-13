#
# spec file for package qpid-cpp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qpid-cpp
Version:        1.38.0
Release:        0
Summary:        Libraries for Qpid C++ client applications
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            http://qpid.apache.org
Source0:        http://www.apache.org/dist/qpid/cpp/%{version}/%{name}-%{version}.tar.gz
Source1000:     %{name}-rpmlintrc
Patch0:         0001-NO-JIRA-qpidd.service-file-for-use-on-Fedora.patch
Patch1:         qpid-0.24-date.patch
Patch2:         qpid-cpp-tests.patch
Patch3:         qpid-cpp-initdir.patch
Patch5:         %{name}-aarch64.patch
BuildRequires:  cmake
BuildRequires:  cyrus-sasl
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  mozilla-nspr
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss
BuildRequires:  mozilla-nss-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-xml
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig >= 2.0.9
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} >= 1200
BuildRequires:  systemd
%endif

%description
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%package client
Summary:        Libraries for Qpid C++ client applications
License:        Apache-2.0
Group:          Productivity/Networking/Other

%description client
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%files client
%license LICENSE.txt
%doc NOTICE.txt
%doc README.md
%doc INSTALL.txt
%{_libdir}/libqpidcommon.so.*
%{_libdir}/libqpidclient.so.*
%{_libdir}/libqpidtypes.so.*
%{_libdir}/libqpidmessaging.so.*
%dir %{_libdir}/qpid
%dir %{_sysconfdir}/qpid
%config(noreplace) %{_sysconfdir}/qpid/qpidc.conf

%post client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%package client-devel
Summary:        Header files, documentation and testing tools for developing Qpid C++ clients
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name}-client = %{version}-%{release}
Requires:       libuuid-devel
Requires:       python
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif

%description client-devel
Libraries, header files and documentation for developing AMQP clients
in C++ using Qpid.  Qpid implements the AMQP messaging specification.

%files client-devel
%dir %{_includedir}/qpid
%{_includedir}/qpid/*.h
%{_includedir}/qpid/qpid.i
%{_includedir}/qpid/swig_perl_typemaps.i
%{_includedir}/qpid/swig_python_typemaps.i
%{_includedir}/qpid/swig_ruby_typemaps.i
%{_includedir}/qpid/sys
%{_includedir}/qpid/messaging
%{_includedir}/qpid/types
%{_libdir}/libqpidcommon.so
%{_libdir}/libqpidclient.so
%{_libdir}/libqpidtypes.so
%{_libdir}/libqpidmessaging.so
%{_libdir}/pkgconfig/qpid.pc
%{_datadir}/qpid
%defattr(755,root,root,-)
%{_bindir}/qpid-perftest
%{_bindir}/qpid-topic-listener
%{_bindir}/qpid-topic-publisher
%{_bindir}/qpid-latency-test
%{_bindir}/qpid-client-test
%{_bindir}/qpid-txtest
%{_bindir}/qpid-send
%{_bindir}/qpid-receive
%dir %{_libexecdir}/qpid
%{_libexecdir}/qpid/tests
%{_libdir}/cmake/Qpid
%{_mandir}/man1/qpid-*.1%{?ext_man}

%post client-devel -p /sbin/ldconfig
%postun client-devel -p /sbin/ldconfig

%package client-devel-docs
Summary:        AMQP client development documentation
License:        Apache-2.0
Group:          Documentation/Other
BuildArch:      noarch

%description client-devel-docs
This package includes the AMQP clients development documentation in HTML
format for easy browsing.

%files client-devel-docs
%{_datadir}/doc/%{name}-%{version}

%package server
Summary:        An AMQP message broker daemon
License:        Apache-2.0
Group:          Productivity/Networking/Other
Requires:       %{name}-client = %{version}-%{release}
Requires:       cyrus-sasl
%if 0%{?suse_version} >= 1200
%systemd_requires
%endif

%description server
A message broker daemon that receives stores and routes messages using
the open AMQP messaging protocol.

%files server
%{_libdir}/libqpidbroker.so.*
%{_sbindir}/qpidd
%{_sbindir}/rcqpidd
%{_unitdir}/qpidd.service
%dir %{_sysconfdir}/qpid
%config(noreplace) %{_sysconfdir}/qpid/qpidd.conf
%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/qpidd.conf
%exclude %{_libdir}/qpid/daemon/ha.so
%{_mandir}/man1/qpidd*
%attr(755, qpidd, qpidd) %{_localstatedir}/lib/qpidd
%ghost %attr(755, qpidd, qpidd) /run/qpidd

%pre server
getent group qpidd >/dev/null || groupadd -r qpidd
getent passwd qpidd >/dev/null || \
  useradd -r -M -g qpidd -d %{_localstatedir}/lib/qpidd -s /sbin/nologin \
    -c "Owner of Qpidd Daemons" qpidd
%if 0%{?suse_version} >= 1200
%service_add_pre qpidd.service
%endif
exit 0

%post server
/sbin/ldconfig
%if 0%{?suse_version} >= 1200
%service_add_post qpidd.service
%endif
exit 0

%preun server
%if 0%{?suse_version} >= 1200
%service_del_preun qpidd.service
%endif
exit 0

%postun server
/sbin/ldconfig
%if 0%{?suse_version} >= 1200
%service_del_preun qpidd.service
%endif
exit 0

%package server-ha
Summary:        Extensions to the AMQP message broker to provide high availability
License:        Apache-2.0
Group:          Productivity/Networking/Other
Requires:       %{name}-server = %{version}-%{release}

%description server-ha
Provides extensions to the AMQP message broker to provide high availability.

%files server-ha
%dir %{_libdir}/qpid
%dir %{_libdir}/qpid/daemon
%{_libdir}/qpid/daemon/ha.so
%{_unitdir}/qpidd-primary.service

%pre server-ha
%if 0%{?suse_version} >= 1200
%service_add_pre qpidd-primary.service
%endif
exit 0

%post server-ha
/sbin/ldconfig
%if 0%{?suse_version} >= 1200
%service_add_post qpidd-primary.service
%endif
exit 0

%preun server-ha
%if 0%{?suse_version} >= 1200
%service_del_preun qpidd-primary.service
%endif
exit 0

%postun server-ha
/sbin/ldconfig
%if 0%{?suse_version} >= 1200
%service_del_postun qpidd-primary.service
%endif
exit 0

%package server-store
Summary:        Red Hat persistence extension to the Qpid messaging system
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
Requires:       %{name}-server = %{version}

%description server-store
Red Hat persistence extension to the Qpid AMQP broker: persistent message
storage using either a libaio-based asynchronous journal, or synchronously
with Berkeley DB.

%files server-store
%dir %{_libdir}/qpid
%dir %{_libdir}/qpid/daemon

%post server-store -p /sbin/ldconfig
%postun server-store -p /sbin/ldconfig

%package -n python-qpid_messaging
Summary:        Python bindings for the Qpid messaging framework
License:        Apache-2.0
Group:          Development/Libraries/Python
Requires:       python
Requires:       python-qpid-common

%description -n python-qpid_messaging
Manual pages and Python bindings for the Qpid messaging framework.

%files -n python-qpid_messaging
%{python_sitearch}/qpid_messaging.py
%{python_sitearch}/qpid_messaging.pyc
%{python_sitearch}/qpid_messaging.pyo
%{python_sitearch}/*_qpid_messaging.so

%package -n qpid-qmf
Summary:        The QPID Management Framework
License:        Apache-2.0
Group:          Productivity/Networking/Other
Requires:       python-qpid >= 0.32
Requires:       qpid-cpp-client >= %{version}

%description -n qpid-qmf
The Qpid Management Framework is a general-purpose management bus built on Qpid
messaging. It takes advantage of the scalability, security, and rich
capabilities of Qpid to provide flexible and easy-to-use manageability to a
large set of applications.

%files -n qpid-qmf
%{_libdir}/libqmf2.so.*

%post -n qpid-qmf -p /sbin/ldconfig
%postun -n qpid-qmf -p /sbin/ldconfig

%package -n qpid-qmf-devel
Summary:        Header files and tools for developing QMF extensions
License:        Apache-2.0
Group:          Development/Tools/Other
Requires:       qpid-cpp-client-devel >= %{version}
Requires:       qpid-qmf = %{version}-%{release}

%description -n qpid-qmf-devel
Header files and code-generation tools needed for developers of QMF-managed
components.

%files -n qpid-qmf-devel
%{_includedir}/qmf
%{_libdir}/libqmf2.so
%{_bindir}/qmf-gen
%{python_sitelib}/qmfgen
%{_libdir}/pkgconfig/qmf2.pc
%{_mandir}/man1/qmf-gen.1%{?ext_man}

%post -n qpid-qmf-devel -p /sbin/ldconfig
%postun -n qpid-qmf-devel -p /sbin/ldconfig

%prep
%setup -q
%patch0 -p3
%patch1 -p2 -b .date
%patch2 -p1 -b .tests
%patch3 -p1 -b .initdir
%patch5 -p2

%global perftests "qpid-perftest qpid-topic-listener qpid-topic-publisher qpid-latency-test qpid-client-test qpid-txtest"

%build
%cmake -DLIBEXEC_INSTALL_DIR=%{_libexecdir} -DENABLE_WARNING_ERROR=OFF
make %{?_smp_mflags}
make docs-user-api %{?_smp_mflags}
pushd bindings/qpid/python
make %{?_smp_mflags}
popd

%install

mkdir -p -m0755 %{buildroot}%{_unitdir}

%cmake_install
chmod 755 %{buildroot}/%{python_sitearch}/*_qpid_messaging.so

# clean up items we're not installing
rm -f  %{buildroot}%{_bindir}/qpid-python-test
rm -f  %{buildroot}%{_libdir}/libqpidbroker.so
rm -f  %{buildroot}%{_libdir}/libcqpid_perl.so
rm -f  %{buildroot}%{_libdir}/ruby/cqpid.so
rm -rf %{buildroot}%{rb_sitelib}
rm -rf %{buildroot}%{_libexecdir}/perl5
rm -rf %{buildroot}%{_libdir}/perl5
rm -rf %{buildroot}%{python_sitearch}/qpid_python*egg-info
rm -rf %{buildroot}%{python_sitearch}/mllib
rm -rf %{buildroot}%{python_sitearch}/qpid
rm -rf %{buildroot}%{python_sitelib}/qpidtoollibs
rm -rf %{buildroot}%{_libdir}/qpid/daemon/store.so*
rm -rf %{buildroot}%{_initddir}/qpidd-primary
rm -rf %{buildroot}%{_datadir}/qpid-tools
rm -rf %{buildroot}%{_libexecdir}/qpid-qls-analyze

# QMF Python management
install -d %{_builddir}/cpp/managementgen/qmfgen \
           %{buildroot}/%{python_sitelib}

# install systemd files
mkdir -p %{buildroot}%{_unitdir}
install -pm 644 %{_builddir}/%{name}-%{version}%{_sysconfdir}/qpidd.service \
    %{buildroot}%{_unitdir}
install -pm 644 %{_builddir}/%{name}-%{version}%{_sysconfdir}/qpidd-primary.service \
    %{buildroot}%{_unitdir}
rm -f %{buildroot}%{_initddir}/qpidd
rm -f %{buildroot}%{_sysconfdir}/init.d/qpidd.service

# install perftests utilities
mkdir -p %{buildroot}%{_bindir}
pushd build/src/tests
for ptest in %{perftests}; do
  libtool --mode=install install -m755 $ptest %{buildroot}%{_bindir}
done
popd

mkdir -p %{buildroot}/run
touch %{buildroot}/run/qpidd
mkdir -p %{buildroot}%{_localstatedir}/lib/qpidd

# Provide SUSE policy symlink /usr/sbin/rcFOO -> /etc/init.d/FOO
# /usr/sbin/service exists only since openSUSE 12.3:
%if 0%{?suse_version} > 1220
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcqpidd
%else
ln -s /sbin/service %{buildroot}%{_sbindir}/rcqpidd
%endif

%fdupes -s %{buildroot}

%check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
