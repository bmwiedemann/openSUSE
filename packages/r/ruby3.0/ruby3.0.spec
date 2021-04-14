#
# spec file for package ruby3.0
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ruby3.0

####
#!!!
#!!! when updating, check versions of embedded rubygems in package stdlib below
#!!!
####

%define patch_level p0
Version:        3.0.1
Release:        0
%define pkg_version %{version}
# make the exported API version explicit
%define api_version 3.0.0
%define rb_binary_suffix .ruby3.0
%define rb_soname ruby3.0
%define _rb_ua_weight 30

# ruby-macros and ruby-common version
%define rpm_macros_version 3

#
%define libname libruby3_0-3_0
# keep in sync with macro file!
%define rb_ver  %{api_version}
%define rb_arch %(echo %{_target_cpu}-linux-gnu | sed -e "s/ppc/powerpc/")
%define rb_arch_short %(echo %{_target_cpu}-linux | sed -e "s/ppc/powerpc/ ; s/i[0-9]86/x86/")
%define rb_libdir                         %{_libdir}/ruby/%{rb_ver}/
%define rb_archdir                        %{_libdir}/ruby/%{rb_ver}/%{rb_arch}
%define rb_extdir                         %{_libdir}/ruby/gems/%{rb_ver}/extensions/
%define rb_extarchdir                     %{_libdir}/ruby/gems/%{rb_ver}/extensions/%{rb_arch_short}/
%define rb_extversionedarchdir            %{_libdir}/ruby/gems/%{rb_ver}/extensions/%{rb_arch_short}/%{rb_ver}
%define rb_extdocdir                      %{_libdir}/ruby/gems/%{rb_ver}/doc/extensions
%define rb_extarchdocdir                  %{_libdir}/ruby/gems/%{rb_ver}/doc/extensions/%{rb_arch_short}

%if "%{rb_default_ruby_suffix}" == "%{rb_soname}"
%define is_default_ruby 1
%define rb_ua_weight 1%{_rb_ua_weight}
%else
%define rb_ua_weight %{_rb_ua_weight}
%endif

%define ua_binaries bundle bundler racc rake rbs rdoc ri typeprof
# keep in sync with macro file!
#
# from valgrind.spec
%ifarch %ix86 x86_64 ppc ppc64
%define use_valgrind 1
%endif
# turn on testsuite by default. we dont hard fail anyway.
%bcond_without run_tests
%bcond_without build_docs
%if 0%{?sle_version} >= 150000
%bcond_without jemalloc
%else
%bcond_with    jemalloc
%endif
%bcond_with    clang
%bcond_with    separate_stdlib

#
URL:            https://www.ruby-lang.org/
Source:         https://cache.ruby-lang.org/pub/ruby/3.0/ruby-%{pkg_version}.tar.xz
#
Source3:        %{name}.macros
Source4:        %{name}-default.macros
Source98:       series
Source99:       %{name}-rpmlintrc
Patch:          use-pie.patch
#
BuildRequires:  ruby-bundled-gems-rpmhelper
%if %{with clang}
BuildRequires:  binutils-gold
BuildRequires:  clang
BuildRequires:  llvm-devel
%endif
BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
%if %{with jemalloc}
BuildRequires:  jemalloc-devel
%endif
BuildRequires:  autoconf
BuildRequires:  libffi-devel
BuildRequires:  libyaml-devel
BuildRequires:  ncurses-devel
BuildRequires:  netcfg
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  procps
BuildRequires:  readline-devel
BuildRequires:  timezone
BuildRequires:  zlib-devel
%if 0%{?use_valgrind}
%if 0%{?suse_version} < 1550
BuildRequires:  valgrind-devel
%else
BuildRequires:  valgrind-client-headers
%endif
%endif
BuildRequires:  xz
Provides:       ruby(abi) = %{rb_ver}
Conflicts:      ruby(abi) = %{rb_ver}
Provides:       ruby30  = %{version}-%{release}
%if 0%{?is_default_ruby}
Provides:       ruby-default = %{version}-%{release}
Conflicts:      otherproviders(ruby-default)
%endif
Requires:       %{libname} = %{version}
%if %{with separate_stdlib}
Requires:       %{name}-stdlib = %{version}
%else
Provides:       %{name}-stdlib = %{version}-%{release}
Obsoletes:      %{name}-stdlib < %{version}-%{release}
%endif
PreReq:         update-alternatives
BuildRequires:  update-alternatives
Requires:       ruby-common

#
Summary:        An Interpreted Object-Oriented Scripting Language
License:        BSD-2-Clause OR Ruby
Group:          Development/Languages/Ruby

%description
Ruby is an interpreted scripting language for object-oriented programming. It
has many features for processing text files and performing system management
tasks (as in Perl).  It is extensible.

* Ruby features:

- Simple Syntax

- *Normal* Object-Oriented features (class, method calls, for
   example)

- *Advanced* Object-Oriented features(Mix-in, Singleton-method, for
   example)

- Operator Overloading

- Exception Handling

- Iterators and Closures

- Garbage Collection

- Dynamic Loading of Object Files (on some architectures)

%package -n %{libname}
Summary:        Dynamic runtime library for Ruby
# Both ruby and ruby-stdlib now depend explicitly on libruby by version,
# however it was not always the case, so the conflicts statements below
# are needed to handle updates.
Group:          System/Libraries
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name}-stdlib < %{version}-%{release}

%description -n %{libname}
Dynamic runtime library for Ruby

%package doc
Summary:        Documentation and samples for Ruby
Group:          Development/Languages/Ruby

%description doc
Documentation and samples for Ruby

%if %{with separate_stdlib}
%package stdlib
Summary:        The Ruby standard library
Group:          Development/Languages/Ruby
Provides:       ruby-stdlib = %{version}-%{release}
Requires:       %{libname} = %{version}

%description stdlib
The Ruby standard library
%endif

%package devel
Summary:        Development files to link against Ruby
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
Provides:       rubygems = 3.0.1
Provides:       rubygems_with_buildroot_patch
%if %{with jemalloc}
Requires:       jemalloc-devel
%endif

%description devel
Development files to link against Ruby.

%package devel-extra
Summary:        Special development files of ruby, normally not installed
Group:          Development/Languages/Ruby
Requires:       %{name}-devel = %{version}

%description devel-extra
Development files to link against Ruby.

%package doc-ri
Summary:        Ruby Interactive Documentation
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc-ri
This package contains the RI docs for ruby

%package doc-html
Summary:        This package contains the HTML docs for ruby
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc-html
This package contains the HTML docs for ruby

%package examples
Summary:        Example scripts for ruby
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
BuildArch:      noarch

%description examples
Example scripts for ruby

%package test-suite
Requires:       %{name} = %{version}
Summary:        An Interpreted Object-Oriented Scripting Language
Group:          Development/Languages/Ruby
BuildArch:      noarch

%description test-suite
Ruby is an interpreted scripting language for object-oriented programming.  It
has many features for processing text files and performing system management
tasks (as in Perl).  It is extensible.

* Ruby features:

- Simple Syntax

- *Normal* Object-Oriented features (class, method calls, for
   example)

- *Advanced* Object-Oriented features(Mix-in, Singleton-method, for
   example)

- Operator Overloading

- Exception Handling

- Iterators and Closures

- Garbage Collection

- Dynamic Loading of Object Files (on some architectures)

%prep
%autosetup -p1 -n ruby-%{pkg_version}
find sample -type f -perm /a=x -ls -exec chmod a-x \{\} \+
# replace "/usr/bin/env ruby" and "/usr/local/bin/ruby" with correct path
grep -Erl '^#! */.*ruby' benchmark bootstraptest ext lib sample test \
  | xargs -r perl -p -i -e 's|^#!\s*\S+\s*ruby\S*(\s+.*)?$|#!/usr/bin/ruby%{rb_binary_suffix} $1|'

%build
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
%if %{with clang}
export CC="clang"
export CXX="clang++"
export LD="ld.gold"
%endif
# iseq.c needs -fno-strict-aliasing
export CFLAGS="%{optflags} -fno-strict-aliasing -std=gnu99"
%configure \
  %if %{with jemalloc}
  --with-jemalloc \
  %endif
  --enable-pie \
  %if 0%{?suse_version} >= 1550
  --with-compress-debug-sections=none \
  %endif
  --program-suffix="%{rb_binary_suffix}"  \
  --with-soname=%{rb_soname} \
  --target=%{_target_platform} \
  %if 0%{?use_valgrind}
  --with-valgrind \
  %endif
  %if %{without build_docs}
  --disable-install-doc  \
  --disable-install-rdoc \
  --disable-install-capi \
  %endif
  --with-mantype=man \
  --enable-shared \
  --disable-static \
  --disable-rpath
make %{?_smp_mflags} all V=1 STRIP=/bin/true

%install
%makeinstall V=1 STRIP=/bin/true
perl -p -i -e 's|#!/usr/local/bin/ruby|%{_bindir}/ruby|g' $(grep -r -l /usr/local/bin/ruby %{buildroot})
echo "%defattr(-,root,root,-)" > devel-extra-excludes
echo "%defattr(-,root,root,-)" > devel-extra-list
for i in iseq.h insns.inc insns_info.inc revision.h version.h  thread_pthread.h \
  ruby_atomic.h method.h internal.h id.h vm_core.h vm_opts.h node.h eval_intern.h vm_debug.h; do
  install -m 644 $i %{buildroot}%{_includedir}/ruby-%{rb_ver}/
  echo "%exclude %{_includedir}/ruby-%{rb_ver}/$i" >> devel-extra-excludes
  echo "%{_includedir}/ruby-%{rb_ver}/$i" >> devel-extra-list
done

# Create gem native extensions dir
# use shell scripting here as we're executing the just installed binary
%define rb_binary %{buildroot}/usr/bin/ruby -I %{buildroot}%{rb_libdir} -I %{buildroot}%{rb_archdir}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

install -D -m 0644 %{S:3} %{buildroot}%{_rpmmacrodir}/macros.suse-ruby3.0
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%if 0%{?is_default_ruby}
  install -D -m 0644 %{S:4} %{buildroot}%{_rpmmacrodir}/macros.suse-ruby3.0-default
  for bin in %{buildroot}%{_bindir}/{erb,gem,irb,ruby}%{rb_binary_suffix} ; do
    # yes really hard links
    ln $bin ${bin%%%{rb_binary_suffix}}
  done
  for man in %{buildroot}%{_mandir}/man1/*%{rb_binary_suffix}.1* ; do
    # yes really hard links
    # TODO: this is dangerous as we cant anc
    ln $man ${man%%%{rb_binary_suffix}.1}.1
  done
  ln -s lib%{rb_soname}.so %{buildroot}%{_libdir}/libruby.so
%endif
for bin in %{ua_binaries}; do
  # dummy
  mv %{buildroot}%_bindir/${bin}%{rb_binary_suffix} %{buildroot}%_bindir/$bin.ruby%{rb_binary_suffix}
  #
  ln -s $bin                      %{buildroot}%{_sysconfdir}/alternatives/$bin
  ln -s %{_sysconfdir}/alternatives/$bin %{buildroot}%_bindir/$bin
  #
  ln -s ${bin}%{rb_binary_suffix} %{buildroot}%{_sysconfdir}/alternatives//$bin%{rb_binary_suffix}
  ln -s %{_sysconfdir}/alternatives/$bin%{rb_binary_suffix} %{buildroot}%_bindir/$bin%{rb_binary_suffix}
done
install -dD %{buildroot}%{rb_extdir} %{buildroot}%{rb_extarchdir} %{buildroot}%{rb_extversionedarchdir} %{buildroot}%{rb_extarchdocdir}
chmod -vR go-w,go+rX %{buildroot}%{_libdir}/ruby

%post
for bin in %{ua_binaries}; do
  /usr/sbin/update-alternatives --install \
    %{_bindir}/$bin $bin %{_bindir}/$bin.ruby%{rb_binary_suffix} %{rb_ua_weight}
  /usr/sbin/update-alternatives --install \
    %{_bindir}/$bin%{rb_binary_suffix} $bin%{rb_binary_suffix} %{_bindir}/$bin.ruby%{rb_binary_suffix} %{rb_ua_weight}
done

%preun
if [ "$1" = 0 ] ; then
  for bin in %{ua_binaries}; do
    /usr/sbin/update-alternatives --remove $bin %{_bindir}/$bin.ruby%{rb_binary_suffix}
    /usr/sbin/update-alternatives --remove $bin%{rb_binary_suffix} %{_bindir}/$bin.ruby%{rb_binary_suffix}
  done
fi

%if %{with run_tests}
%check
DISABLE_TESTS=""
%ifarch armv7l armv7hl armv7hnl
# test_call_double(DL::TestDL) fails on ARM HardFP
# http://bugs.ruby-lang.org/issues/6592
DISABLE_TESTS="-x test_dl2.rb $DISABLE_TESTS"

# Workaround OpenSSL::TestPKeyRSA#test_sign_verify_memory_leak timeouts on ARM.
# https://bugs.ruby-lang.org/issues/9984
sed -i -e 's|20_000|10_000|g' test/openssl/test_pkey_rsa.rb
%endif
# Allow MD5 in OpenSSL.
# https://bugs.ruby-lang.org/issues/9154
export OPENSSL_ENABLE_MD5_VERIFY=1
export LD_LIBRARY_PATH="$PWD"
# we know some tests will fail when they do not find a /usr/bin/ruby
make check V=1 TESTOPTS="$DISABLE_TESTS" ||:
%endif

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%ghost %{_sysconfdir}/alternatives/erb*
%ghost %{_sysconfdir}/alternatives/rbs*
%ghost %{_sysconfdir}/alternatives/racc*
%ghost %{_sysconfdir}/alternatives/rake*
%ghost %{_sysconfdir}/alternatives/rdoc*
%ghost %{_sysconfdir}/alternatives/ri*
%ghost %{_sysconfdir}/alternatives/bundle*
%ghost %{_sysconfdir}/alternatives/typeprof*
%{_bindir}/bundle*
%{_bindir}/erb*
%{_bindir}/gem*
%{_bindir}/irb*
%{_bindir}/rake*
%{_bindir}/rdoc*
%{_bindir}/rbs*
%{_bindir}/ri*
%{_bindir}/ruby*
%{_bindir}/racc*
%{_bindir}/typeprof*
%{_mandir}/man1/irb*.1*
%{_mandir}/man1/erb*.1*
#{_mandir}/man1/rake*.1*
%{_mandir}/man1/ri*.1*
%{_mandir}/man1/ruby*.1*
%doc ChangeLog  KNOWNBUGS.rb NEWS.md README.EXT README.EXT.ja README.ja.md README.md CONTRIBUTING.md
%license COPYING  COPYING.ja  GPL  LEGAL BSDL
%{_rpmmacrodir}/macros.suse-ruby3.0*

%if %{with separate_stdlib}
%files stdlib
%endif
%{_libdir}/ruby/
%exclude %{_libdir}/ruby/gems/%{api_version}/gems/*/test/
%dir %rb_extdir
%dir %rb_extarchdir
%dir %rb_extversionedarchdir
%dir %rb_extdocdir
%dir %rb_extarchdocdir

%files -n %{libname}
%{_libdir}/libruby*.so.*

%files devel -f devel-extra-excludes
%{_includedir}/ruby-%{rb_ver}
%{_libdir}/libruby*.so
%{_libdir}/pkgconfig/ruby-3.0.pc

%files devel-extra -f devel-extra-list

%if %{with build_docs}
%files doc
%doc doc/* sample/

%files doc-ri
%dir %{_datadir}/ri/
%{_datadir}/ri/%{rb_ver}/
%endif

%changelog
