#
# spec file for package libprelude
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_sitearch3: %global python_sitearch3 %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitearchdir"] ')}
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%{!?luapkgdir: %global luapkgdir %{_libdir}/lua/%{luaver}}
%define sover 28
%define sover_cpp 8
Name:           libprelude
Version:        5.0.0
Release:        0
Summary:        Secure Connections between all Sensors and the Prelude Manager
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
# libmissing/test is GPL-3.0+
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-or-later
Group:          Productivity/Networking/Security
Url:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
# Known bug on gnulib side and will be fixed
Patch0:         libprelude-disable_gnulib_test_lock.patch
# Wrong test
Patch1:         libprelude-fix_prelude_tests_timer.patch
# pthread_atfork was automatically linked before but not anymore
Patch2:         libprelude-fix_pthread_atfork.patch
# Fix time comparaison
Patch3:         libprelude-fix_timegm.patch
# Wrong FSF address
Patch4:         libprelude-fsf-address.patch
# Correctly link for Perl bindings
Patch5:         libprelude-linking.patch
# Fix 64 bit portability issues
Patch6:         libprelude-fix_64bit_portability_issues.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libgnutls-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  lua-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1310
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
%endif
%endif

%description
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package -n %{name}%{sover}
Summary:        Prelude Libraries
Group:          System/Libraries

%description -n %{name}%{sover}
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package -n %{name}cpp%{sover_cpp}
Summary:        Prelude Libraries
Group:          System/Libraries

%description -n %{name}cpp%{sover_cpp}
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package -n prelude-tools
Summary:        Tools for libprelude
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description -n prelude-tools
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package devel
Summary:        Development files for libprelude
Group:          Development/Libraries/C and C++
Requires:       libgcrypt-devel
Requires:       libgnutls-devel
Requires:       libgpg-error-devel
Requires:       libprelude%{sover} = %{version}
Requires:       libpreludecpp%{sover_cpp} = %{version}

%description devel
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package devel-bindings
Summary:        Development files for libprelude
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       lua-devel
Requires:       python-devel
Requires:       python3-devel
Requires:       ruby-devel
Requires:       swig

%description devel-bindings
Libprelude is a library that guarantees secure connections between all sensors
and the Prelude Manager. Libprelude provides an Application Programming Interface
(API) for the communication with Prelude sub-systems, it supplies the necessary
functionality for generating and emitting IDMEF events with Prelude and automates
the saving and re-transmission of data in times of temporary interruption of one
of the components of the system.

%package -n python2-%{name}
Summary:        Python 2 bindings for libprelude
Group:          Development/Languages/Python
Provides:       python-%{name} = %version
Obsoletes:      python-%{name} < %version 
Requires:       libprelude%{sover} = %{version}
Requires:       python = %{py_ver}

%description -n python2-%{name}
Python 2 bindings for libprelude generated by SWIG.

%package -n perl-%{name}
Summary:        Perl bindings for libprelude
Group:          Development/Languages/Perl
BuildRequires:  perl
Requires:       libprelude%{sover} = %{version}
Requires:       perl = %{perl_version}

%description -n perl-%{name}
Perl bindings for libprelude generated by SWIG.

%package -n python3-%{name}
Summary:        Python 3 bindings for libprelude
Group:          Development/Languages/Python
Requires:       libprelude%{sover} = %{version}
Requires:       python = %{py3_ver}

%description -n python3-%{name}
Python 3 bindings for libprelude generated by SWIG.

%package -n ruby-%{name}
Summary:        Ruby bindings for libprelude
Group:          Development/Languages/Ruby
Requires:       libprelude%{sover} = %{version}
Requires:       ruby

%description -n ruby-%{name}
Ruby bindings for libprelude generated by SWIG.

%package -n lua-%{name}
Summary:        Lua bindings for libprelude
Group:          Development/Languages/Lua
Requires:       libprelude%{sover} = %{version}
Requires:       lua

%description -n lua-%{name}
Lua bindings for libprelude generated by SWIG.

%package doc
Summary:        Libprelude documentation
Group:          System/Libraries

%description doc
Libprelude documentation files.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6

%build
%configure    --disable-static \
              --with-html-dir=%{_defaultdocdir}/%{name}-%{version}/html \
              --with-perl-installdirs=vendor \
              --enable-gtk-doc \
  	      gl_cv_func_printf_directive_n=yes \
  	      gl_cv_func_printf_infinite_long_double=yes

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%perl_process_packlist
%perl_gen_filelist
mkdir -p %{buildroot}/${_localstatedir}/spool/prelude
mv %{buildroot}/%{_datadir}/libprelude %{buildroot}/%{_datadir}/libprelude%{sover}

%post -n libprelude%{sover} -p /sbin/ldconfig
%post -n libpreludecpp%{sover_cpp} -p /sbin/ldconfig
%postun -n libprelude%{sover} -p /sbin/ldconfig
%postun -n libpreludecpp%{sover_cpp} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%{_libdir}/libprelude.so.%{sover}*
%dir %{_localstatedir}/spool/prelude

%files -n prelude-tools
%defattr(-,root,root)
%{_bindir}/prelude-adduser
%{_bindir}/prelude-admin
%{_mandir}/man1/prelude-admin.1%{ext_man}
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%dir %{_sysconfdir}/prelude/profile
%config(noreplace) %{_sysconfdir}/prelude/default/client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/global.conf
%config(noreplace) %{_sysconfdir}/prelude/default/idmef-client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/tls.conf

%files -n %{name}cpp%{sover_cpp}
%defattr(-,root,root)
%{_libdir}/libpreludecpp.so.%{sover_cpp}*

%files devel
%defattr(-,root,root)
%{_bindir}/libprelude-config
%{_includedir}/libprelude
%{_libdir}/libprelude.so
%{_libdir}/libpreludecpp.so
%{_libdir}/pkgconfig/libprelude.pc
%{_datadir}/aclocal/libprelude.m4

%files devel-bindings
%defattr(-,root,root)
%dir %{_datadir}/libprelude%{sover}/
%dir %{_datadir}/libprelude%{sover}/swig
%{_datadir}/libprelude%{sover}/swig/libpreludecpp.i
%dir %{_datadir}/libprelude%{sover}/swig/lua/
%{_datadir}/libprelude%{sover}/swig/lua/libpreludecpp-lua.i
%dir %{_datadir}/libprelude%{sover}/swig/perl/
%{_datadir}/libprelude%{sover}/swig/perl/libpreludecpp-perl.i
%dir %{_datadir}/libprelude%{sover}/swig/python/
%{_datadir}/libprelude%{sover}/swig/python/libpreludecpp-python.i
%dir %{_datadir}/libprelude%{sover}/swig/ruby/
%{_datadir}/libprelude%{sover}/swig/ruby/libpreludecpp-ruby.i

%files -n python2-%{name}
%defattr(-,root,root)
%{python_sitearch}/*

%files -n perl-%{name} -f %{name}.files
%defattr(-,root,root)
%exclude %{_bindir}/libprelude-config
%exclude %{_bindir}/prelude-adduser
%exclude %{_bindir}/prelude-admin
%exclude %{_mandir}/man1/prelude-admin.1.gz

%files -n python3-%{name}
%defattr(-,root,root)
%{python_sitearch3}/*

%files -n ruby-%{name}
%defattr(-,root,root)
%{ruby_sitearch}/Prelude.so

%files -n lua-%{name}
%defattr(-,root,root)
%{luapkgdir}/prelude.so

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}
%doc AUTHORS ChangeLog README NEWS COPYING LICENSE.README HACKING.README

%changelog
