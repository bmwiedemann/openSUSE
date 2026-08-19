#
# spec file for package thrift
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "perl"
%global pkgname thrift-perl
%global build_perl 1
%endif

%if "%{flavor}" == "php"
%global pkgname thrift-php
# Not %%{flavor}: the flavor is the language, php_name is the PHP stack the
# extension is compiled against. php8 is the only one in the distribution
# today; a php9 would become a second flavor with its own php_name.
%global php_name php8
%global build_php 1
%endif

%if "%{flavor}" == "python"
# Not named python-thrift: the singlespec generator rejects any unmarked
# %%files section in a package called python-*, and this spec carries the
# core's %%files too. python_subpackage_only turns that check off and makes
# the bindings a subpackage instead, which is what they are here.
%global pkgname thrift-python
%global python_subpackage_only 1
%global build_python 1
%endif

# Anything that is not one of the binding flavors is the C++/C core.
%if "%{?pkgname}" == ""
%global pkgname thrift
%global build_core 1
%endif

%if 0%{?build_python}
%{?sle15_python_module_pythons}
%endif
# Unrelated to %%{version}: this is the real SOVERSION of libthrift_c_glib,
# which is versioned conventionally. Bump only when the C ABI breaks.
%global libgversion 0
Name:           %{pkgname}
Version:        0.24.0
Release:        0
# The C++ libraries are built with libtool -release, so the version is baked
# into the file name (libthrift-0.24.0.so) and there is no libthrift.so.N
# symlink; the shared library packages therefore have to carry %%{version} in
# their name. Spelled out rather than derived with %%(echo ... | tr . _),
# because OBS's spec parser cannot expand %%(...) and warns on every build.
# %%build asserts that it still matches, so a missed bump is an FTBFS.
%global libversion 0_24_0
Summary:        Framework for scalable cross-language services development
License:        Apache-2.0
URL:            https://thrift.apache.org
Source0:        https://archive.apache.org/dist/thrift/%{version}/thrift-%{version}.tar.gz
Source1:        https://archive.apache.org/dist/thrift/%{version}/thrift-%{version}.tar.gz.asc
Source2:        thrift.keyring
Source3:        thrift-rpmlintrc
%if 0%{?build_core}
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%endif
%if 0%{?build_python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# The fastbinary accelerator is C++. setup.py catches a failed compile and
# falls back to a pure-Python wheel, which lands in sitelib and so misses the
# sitearch-only %%files below. A missing compiler is therefore an FTBFS rather
# than a silently degraded package - and %%check says why.
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%endif
%if 0%{?build_perl}
BuildRequires:  perl
BuildRequires:  perl-macros
# Class::Accessor is in Makefile.PL's PREREQ_PM but no shipped module uses
# it; kept as a BuildRequires only to silence the MakeMaker warning.
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Class::Accessor)
# Needed by %%check, which compile-checks every shipped module.
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LWP::UserAgent)
%endif
%if 0%{?build_php}
# /usr/bin/php, used by %%check.
BuildRequires:  %{php_name}-cli
# php_extdir, php_cfgdir, php_core_api and php_zend_api all come from this.
BuildRequires:  %{php_name}-devel
# thrift_protocol is a C++ extension.
BuildRequires:  gcc-c++
%endif

%description
Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%if 0%{?build_python}
%package -n python-thrift
Summary:        Python bindings for the Thrift software framework
License:        Apache-2.0
# Floors taken from setup.py's tornado/twisted extras.
Suggests:       python-Twisted >= 24.3.0
Suggests:       python-tornado >= 6.3.0

%description -n python-thrift
Python bindings for the Thrift software framework, including the
fastbinary C accelerator module.

%python_subpackages
%endif

%if 0%{?build_perl}
%package -n perl-thrift
Summary:        Perl bindings to the Thrift software framework
License:        Apache-2.0
# Thrift::BinaryProtocol needs this on every code path.
Requires:       perl(Bit::Vector)
# Optional transports: Thrift::HttpClient and Thrift::SSLSocket.
Recommends:     perl(HTTP::Request)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(IO::String)
Recommends:     perl(LWP::UserAgent)
BuildArch:      noarch
%{perl_requires}

%description -n perl-thrift
Perl bindings to the Thrift software framework.
%endif

%if 0%{?build_php}
%package -n %{php_name}-thrift
Summary:        PHP bindings for the Thrift software framework
License:        Apache-2.0
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}
Provides:       php-thrift = %{version}

%description -n %{php_name}-thrift
PHP bindings for the Thrift software framework: the Thrift\ class
library, installed on PHP's include path, together with the
thrift_protocol extension that accelerates binary (de)serialization.
%endif

%if 0%{?build_core}
%package -n libthrift-%{libversion}
Summary:        C++ API for the Thrift software framework
License:        Apache-2.0

%description -n libthrift-%{libversion}
Shared library providing the C++ API for the Thrift software framework.

%package -n libthriftnb-%{libversion}
Summary:        Thrift non-blocking server library
License:        Apache-2.0

%description -n libthriftnb-%{libversion}
Shared library providing the non-blocking server component of the
Thrift software framework.

%package -n libthriftz-%{libversion}
Summary:        Thrift Zlib API
License:        Apache-2.0

%description -n libthriftz-%{libversion}
A shared library from the Thrift software framework.

%package -n libthrift_c_glib%{libgversion}
Summary:        C API for the Thrift software framework
License:        Apache-2.0

%description -n libthrift_c_glib%{libgversion}
Shared library providing the C API for the Thrift software framework.

%package -n libthrift-devel
Summary:        Thrift C++ library development files
License:        Apache-2.0
Requires:       libthrift-%{libversion} = %{version}
Requires:       libthriftnb-%{libversion} = %{version}
Requires:       libthriftz-%{libversion} = %{version}

%description -n libthrift-devel
Development files for the C++ API of the Thrift software framework.

%package -n libthrift_c_glib-devel
Summary:        Thrift C (GLib) library development files
License:        Apache-2.0
Requires:       libthrift_c_glib%{libgversion} = %{version}
Requires:       pkgconfig(glib-2.0)

%description -n libthrift_c_glib-devel
Development files for the GLib based C API of the Thrift software
framework. Kept apart from libthrift-devel so that C++ consumers do
not pull in the GLib stack, and vice versa.
%endif

%prep
%autosetup -p1 -n thrift-%{version}

%build
%if 0%{?build_core}
# Keep the libthrift-%%{libversion} package names in step with the file names
# %%files pins to %%{version}; see the comment on %%{libversion} above.
test "%{libversion}" = "$(echo %{version} | tr . _)" || {
	echo "libversion (%{libversion}) does not match version (%{version})" >&2
	exit 1
}

# tests require a static boost library, which openSUSE does not ship
# (boost is built link=shared runtime-link=shared).
# The Perl and Python bindings are built by the perl and python
# _multibuild flavors, not here.
%configure \
	--disable-tests \
	--enable-static=no \
	--without-perl \
	--without-py3 \
	--without-python
%make_build
%endif

%if 0%{?build_python}
pushd lib/py
%pyproject_wheel
popd
%endif

%if 0%{?build_perl}
# Built here rather than by the top-level configure: upstream's
# lib/perl/Makefile.am passes INSTALL_BASE=$PERL_PREFIX (default /usr/local),
# which overrides INSTALLDIRS=vendor in ExtUtils::MakeMaker and installs
# outside the vendor tree. Driving Makefile.PL directly avoids that.
pushd lib/perl
perl Makefile.PL INSTALLDIRS=vendor
%make_build
popd
%endif

%if 0%{?build_php}
# Only the extension needs building; the class library is plain PHP. Driven
# through phpize rather than the top-level configure, whose --with-php-extension
# is a no-op unless lib/php/src/ext/thrift_protocol/configure already exists -
# and that file is generated by phpize, so it is absent from the tarball.
pushd lib/php/src/ext/thrift_protocol
%{__phpize}
%configure
%make_build
popd
%endif

%install
%if 0%{?build_core}
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%endif

%if 0%{?build_python}
pushd lib/py
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if 0%{?build_perl}
pushd lib/perl
%perl_make_install
popd
%perl_process_packlist
# The bindings are pure Perl and the subpackage is noarch, but the build
# itself is arch-ful, so packlist processing leaves an empty auto/ tree under
# vendorarch. Left in place it would put an architecture path into a noarch
# package (filelist-forbidden-noarch).
rm -rf %{buildroot}%{perl_vendorarch}
%perl_gen_filelist
%endif

%if 0%{?build_php}
pushd lib/php/src/ext/thrift_protocol
%make_install INSTALL_ROOT=%{buildroot}
popd
install -D -p -m 0644 lib/php/thrift_protocol.ini \
	%{buildroot}%{php_cfgdir}/thrift_protocol.ini
# Every class is namespaced Thrift\..., so lib/php/lib is the root of the
# Thrift\ prefix; /usr/share/%%{php_name} is on the stock include_path.
mkdir -p %{buildroot}%{_datadir}/%{php_name}
cp -a lib/php/lib %{buildroot}%{_datadir}/%{php_name}/Thrift
%endif

%if 0%{?build_python}
%check
# The bulk of lib/py/test needs the thrift compiler to generate stubs first,
# which would make this flavor depend on the core. Verify instead that the
# package imports out of the buildroot and that the fastbinary C accelerator
# really was built and loads - that is the part which silently degrades to the
# pure-Python fallback when the extension fails to compile.
%python_expand cd %{_tmppath} && PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "from thrift.protocol import fastbinary; from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated; print(fastbinary.__file__)"
%endif

%if 0%{?build_perl}
%check
# Upstream's t/ suite needs stubs from the thrift compiler (Makefile.PL adds
# -Igen-perl -Igen-perl2), which would make this flavor depend on the core.
# Compile-check every shipped module instead: this catches syntax errors and
# missing runtime prerequisites, which is what actually breaks here.
modules=$(find %{buildroot}%{perl_vendorlib} -name '*.pm' | wc -l)
# Assert the tree was actually found, so a future path change turns into a
# failure rather than a silently empty (and therefore passing) check.
test "$modules" -gt 0 || { echo "no .pm found under %{buildroot}%{perl_vendorlib}" >&2; exit 1; }
find %{buildroot}%{perl_vendorlib} -name '*.pm' -print0 |
    xargs -0 -n1 perl -I %{buildroot}%{perl_vendorlib} -c
%endif

%if 0%{?build_php}
%check
# Upstream's phpunit suite needs stubs from the thrift compiler, which would
# make this flavor depend on the core. Check the two things that actually break
# instead: that the extension loads and exports the functions the class library
# probes for with function_exists(), and that every shipped class parses.
%{__php} -n -d extension=%{buildroot}%{php_extdir}/thrift_protocol.so \
	-r 'exit((int) !(function_exists("thrift_protocol_write_binary") && function_exists("thrift_protocol_read_binary")));'
classes=$(find %{buildroot}%{_datadir}/%{php_name}/Thrift -name '*.php' | wc -l)
# Assert the tree was found, so a future path change fails rather than passing
# on an empty list.
test "$classes" -gt 0 || { echo "no .php found under %{buildroot}%{_datadir}/%{php_name}/Thrift" >&2; exit 1; }
find %{buildroot}%{_datadir}/%{php_name}/Thrift -name '*.php' -print0 |
    xargs -0 -n1 %{__php} -n -l
%endif

%if 0%{?build_core}
%ldconfig_scriptlets -n libthrift-%{libversion}
%ldconfig_scriptlets -n libthriftnb-%{libversion}
%ldconfig_scriptlets -n libthriftz-%{libversion}
%ldconfig_scriptlets -n libthrift_c_glib%{libgversion}

%files
%doc CHANGES.md
%license LICENSE NOTICE
%{_bindir}/thrift

%files -n libthrift-%{libversion}
%license LICENSE NOTICE
%{_libdir}/libthrift-%{version}.so

%files -n libthriftnb-%{libversion}
%license LICENSE NOTICE
%{_libdir}/libthriftnb-%{version}.so

%files -n libthriftz-%{libversion}
%license LICENSE NOTICE
%{_libdir}/libthriftz-%{version}.so

%files -n libthrift_c_glib%{libgversion}
%license LICENSE NOTICE
%{_libdir}/libthrift_c_glib.so.%{libgversion}*

%files -n libthrift-devel
%license LICENSE NOTICE
%{_includedir}/thrift
%exclude %{_includedir}/thrift/c_glib
%{_libdir}/libthrift.so
%{_libdir}/libthriftnb.so
%{_libdir}/libthriftz.so
%{_libdir}/pkgconfig/thrift.pc
%{_libdir}/pkgconfig/thrift-nb.pc
%{_libdir}/pkgconfig/thrift-z.pc

%files -n libthrift_c_glib-devel
%license LICENSE NOTICE
%dir %{_includedir}/thrift
%{_includedir}/thrift/c_glib
%{_libdir}/libthrift_c_glib.so
%{_libdir}/pkgconfig/thrift_c_glib.pc
%endif

%if 0%{?build_python}
%files %{python_files thrift}
%license LICENSE NOTICE
%doc lib/py/README.md
%{python_sitearch}/thrift
%{python_sitearch}/thrift-%{version}.dist-info
%endif

%if 0%{?build_perl}
%files -n perl-thrift -f %{name}.files
%license LICENSE NOTICE
%doc lib/perl/README.md
%endif

%if 0%{?build_php}
%files -n %{php_name}-thrift
%license LICENSE NOTICE
%doc lib/php/README.md
%config(noreplace) %{php_cfgdir}/thrift_protocol.ini
%{php_extdir}/thrift_protocol.so
%{_datadir}/%{php_name}/Thrift
%endif

%changelog
