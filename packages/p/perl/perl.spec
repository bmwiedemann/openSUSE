#
# spec file for package perl
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


%define pversion 5.28.1
%global versionlist 5.28.0
Name:           perl
Version:        5.28.1
Release:        0
Summary:        The Perl interpreter
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Development/Languages/Perl
Url:            https://www.perl.org/
Source:         https://www.cpan.org/src/5.0/perl-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        macros.perl
Source3:        README.macros
Source4:        baselibs.conf
Patch0:         perl-5.28.0.dif
Patch2:         perl-regexp-refoverflow.diff
Patch3:         perl-nroff.diff
Patch4:         perl-netcmdutf8.diff
Patch5:         perl-HiRes.t-timeout.diff
Patch6:         perl-saverecontext.diff
# PATCH-FIX-OPENSUSE perl-5.22.0_wrong_rpm_provides.diff Prevent generating bad RPM provides
Patch7:         perl-5.22.0_wrong_rpm_provides.diff
Patch8:         skip_time_hires.patch
Patch9:         perl-incfix.diff
Patch11:        perl-5.18.2-overflow.diff
# PATCH-FIX-OPENSUSE
Patch12:        perl-reproducible.patch
Patch13:        perl_skip_flaky_tests_powerpc.patch
Patch14:        posix-sigaction.patch
Patch15:        perl-gdbm-test-no-mmap.diff
Patch16:        perl-revert-caretx.diff
# PATCH-FIX-UPSTREAM unmerged
Patch17:        perl-fix2020.patch
# PATCH-FIX-UPSTREAM unmerged https://www.nntp.perl.org/group/perl.perl5.porters/2018/12/msg253240.html
Patch18:        perl-reproducible2.patch
BuildRequires:  db-devel
BuildRequires:  gdbm-devel
BuildRequires:  libbz2-devel
BuildRequires:  ncurses-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       perl-base = %{version}
Suggests:       perl-doc = %{version}
Provides:       perl-500
Provides:       perl-Filter-Simple = 0.95
Provides:       perl(:MODULE_COMPAT_%{pversion})
Obsoletes:      perl-Filter-Simple <= 0.95
Provides:       perl-I18N-LangTags = 0.43
Obsoletes:      perl-I18N-LangTags <= 0.43
Provides:       perl-MIME-Base64 = 3.15
Obsoletes:      perl-MIME-Base64 <= 3.15
Provides:       perl-Storable = 3.08
Obsoletes:      perl-Storable <= 3.08
Provides:       perl-Test-Simple = 1.302133
Obsoletes:      perl-Test-Simple <= 1.302133
Provides:       perl-Text-Balanced = 2.03
Obsoletes:      perl-Text-Balanced <= 2.03
Provides:       perl-Time-HiRes = 1.9759
Obsoletes:      perl-Time-HiRes <= 1.9759
Provides:       perl-libnet = 3.11
Obsoletes:      perl-libnet <= 3.11
Provides:       perl-Compress-Raw-Zlib = 2.076
Obsoletes:      perl-Compress-Raw-Zlib <= 2.076
Provides:       perl-Compress-Zlib = 2.074
Obsoletes:      perl-Compress-Zlib <= 2.074
Provides:       perl-IO-Compress-Base = 2.074
Obsoletes:      perl-IO-Compress-Base <= 2.074
Provides:       perl-IO-Compress-Zlib = 2.074
Obsoletes:      perl-IO-Compress-Zlib <= 2.074
Provides:       perl-IO-Zlib = 1.10
Obsoletes:      perl-IO-Zlib <= 1.10
Provides:       perl-Archive-Tar = 2.30
Obsoletes:      perl-Archive-Tar <= 2.30
Provides:       perl-Locale-Maketext-Simple = 0.21
Obsoletes:      perl-Locale-Maketext-Simple <= 0.21
Provides:       perl-Pod-Escapes = 1.07
Obsoletes:      perl-Pod-Escapes <= 1.07
Provides:       perl-Pod-Simple = 3.35
Obsoletes:      perl-Pod-Simple <= 3.35
Provides:       perl-ExtUtils-ParseXS = 3.39
Obsoletes:      perl-ExtUtils-ParseXS <= 3.39
Provides:       perl-CPAN-Meta = 2.150010
Obsoletes:      perl-CPAN-Meta <= 2.150010
Provides:       perl-CPAN-Meta-YAML = 0.018
Obsoletes:      perl-CPAN-Meta-YAML <= 0.018
Provides:       perl-ExtUtils-CBuilder = 0.280230
Obsoletes:      perl-ExtUtils-CBuilder <= 0.280230
Provides:       perl-IO-Socket-IP = 0.39
Obsoletes:      perl-IO-Socket-IP <= 0.39
Provides:       perl-Parse-CPAN-Meta = 2.150010
Obsoletes:      perl-Parse-CPAN-Meta <= 2.150010
Provides:       perl-PathTools = 3.63
Obsoletes:      perl-PathTools <= 3.63
Provides:       perl-autodie = 2.29
Obsoletes:      perl-autodie <= 2.29
Provides:       perl-Test-Harness = 3.42
Obsoletes:      perl-Test-Harness <= 3.42
Provides:       perl-version = 0.9923
Obsoletes:      perl-version <= 0.9923
%if "%{version}" != "%{pversion}"
Provides:       perl = %{pversion}-%{release}
%endif

%description
perl - Practical Extraction and Report Language

Perl is optimized for scanning arbitrary text files, extracting
information from those text files, and printing reports based on that
information.  It is also good for many system management tasks. Perl is
intended to be practical (easy to use, efficient, and complete) rather
than beautiful (tiny, elegant, and minimal).

Some of the modules available on CPAN can be found in the "perl"
series.

%package base
Summary:        The Perl interpreter
Group:          Development/Languages/Perl
Provides:       perl-Digest
Provides:       perl-Digest-MD5 = 2.55
%if "%{version}" != "%{pversion}"
Provides:       perl-base = %{pversion}-%{release}
%endif

%description base
perl - Practical Extraction and Report Language

Perl is optimized for scanning arbitrary text files, extracting
information from those text files, and printing reports based on that
information.  It is also good for many system management tasks.

Perl is intended to be practical (easy to use, efficient, and complete)
rather than beautiful (tiny, elegant, and minimal).

This package contains only some basic modules and the perl binary
itself.

%package doc
Summary:        Perl Documentation
Group:          Development/Languages/Perl
Requires:       perl = %{version}
Provides:       perl-macros = 2.0
Provides:       perl:%{_mandir}/man3/CORE.3pm.gz
Obsoletes:      perl-macros < 2.0
BuildArch:      noarch

%description doc
Perl man pages and pod files.

%prep
%setup -q -n perl-%{pversion}
cp -p %{SOURCE3} .
%patch0
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%ifarch ppc ppc64 ppc64le
%patch8 -p1
%patch13
%endif
%patch9
%patch11
%patch12 -p1
%patch14 -p1
%patch15
%patch16
%patch17 -p1
%patch18 -p1

%build
%define _lto_cflags %{nil}
cp -a lib savelib
export BZIP2_LIB=%{_libdir}
export BZIP2_INCLUDE=%{_includedir}
export BUILD_BZIP2=0
options="-Doptimize='%{optflags} -Wall -pipe'"
%ifarch alpha
# -mieee needed for bad alpha gcc optimization
options="-Doptimize='%{optflags} -Wall -pipe -mieee'"
%endif
%ifarch ppc ppc64
options="$options -Duse64bitint"
%endif
# this needs an installed perl, sorry
archname=%(perl -V:archname | sed "s!.*='!!;s!'.*!!")
test -n "$archname"
versionlist=
for v in %{?versionlist} ; do
  test "$v" == none || versionlist="$versionlist $v/$archname $v"
done
test -n "$versionlist" || versionlist=none
versionlist=${versionlist# }
# always use glibc's setenv
options="$options -Accflags='-DPERL_USE_SAFE_PUTENV'"
options="$options -Dotherlibdirs=%{_libexecdir}/perl5/site_perl -Dinc_version_list='$versionlist'"
chmod 755 ./configure.gnu
./configure.gnu --prefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dinstallusrbinperl -Dusethreads -Di_db -Di_dbm -Di_ndbm -Di_gdbm -Dd_dbm_open -Duseshrplib=\'true\' $options
make %{?_smp_mflags}
cp -p libperl.so savelibperl.so
cp -p lib/Config.pm saveConfig.pm
cp -p lib/Config_heavy.pl saveConfig_heavy.pl
make -j1 clobber
rm -rf lib
mv savelib lib
./configure.gnu --prefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dinstallusrbinperl -Dusethreads -Di_db -Di_dbm -Di_ndbm -Di_gdbm -Dd_dbm_open $options
make %{?_smp_mflags}

%check
%if !0%{?qemu_user_space_build}
TEST_JOBS="%{jobs}" make %{?_smp_mflags} test
%endif

%install
%make_install
cp -a %{buildroot}%{_libexecdir}/perl5/site_perl %{buildroot}%{_libexecdir}/perl5/vendor_perl
cpa=`echo %{buildroot}%{_libexecdir}/perl5/*/*/CORE | sed -e 's@/CORE$@@'`
cp=`echo "$cpa" | sed -e 's@/[^/]*$@@'`
vpa=`echo $cpa | sed -e 's@/perl5/@/perl5/vendor_perl/@'`
vp=`echo "$vpa" | sed -e 's@/[^/]*$@@'`
install -d $vp/auto
install -d $vpa/auto
install -m 555 savelibperl.so $cpa/CORE/libperl.so
install -m 444 saveConfig.pm $cpa/Config.pm
install -m 444 saveConfig_heavy.pl $cpa/Config_heavy.pl
# install macros.perl file
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/rpm/macros.perl
pushd %{_includedir}
( rpm -ql glibc-devel | fgrep '.h'
  find %{_includedir}/asm/ -name \*.h
  find %{_includedir}/asm-generic -name \*.h
  find %{_includedir}/linux -name \*.h
) | while read f; do
  %{buildroot}%{_bindir}/perl -I$cp -I$cpa %{buildroot}%{_bindir}/h2ph -d $vpa ${f/\/usr\/include\//} || :
done
popd
d="`gcc -print-file-name=include`"
test -f "$d/stdarg.h" && (cd $d ; %{buildroot}%{_bindir}/perl -I$cp -I$cpa %{buildroot}%{_bindir}/h2ph -d $vpa stdarg.h stddef.h float.h)
# remove broken pm - we don't have the module
rm -f %{buildroot}%{_libexecdir}/perl5/*/Pod/Perldoc/ToTk.pm
# we don't need this in here
rm -f %{buildroot}%{_libexecdir}/perl5/*/*/CORE/libperl.a
# test CVE-2007-5116
%{buildroot}%{_bindir}/perl -e '$r=chr(128)."\\x{100}";/$r/'
# test perl-regexp-refoverflow.diff, should not crash or hang
%{buildroot}%{_bindir}/perl -e 'eval "/\\6666666666/"'
cat << EOF > perl-base-filelist
%{_libexecdir}/perl5/%{pversion}/B/Deparse.pm
%{_libexecdir}/perl5/%{pversion}/Carp.pm
%{_libexecdir}/perl5/%{pversion}/Carp/
%{_libexecdir}/perl5/%{pversion}/Class/
%{_libexecdir}/perl5/%{pversion}/Config/
%{_libexecdir}/perl5/%{pversion}/Digest.pm
%{_libexecdir}/perl5/%{pversion}/Digest/
%{_libexecdir}/perl5/%{pversion}/English.pm
%{_libexecdir}/perl5/%{pversion}/Exporter.pm
%{_libexecdir}/perl5/%{pversion}/Exporter/
%{_libexecdir}/perl5/%{pversion}/File/
%{_libexecdir}/perl5/%{pversion}/Getopt/
%{_libexecdir}/perl5/%{pversion}/IPC/
%{_libexecdir}/perl5/%{pversion}/Text/
%{_libexecdir}/perl5/%{pversion}/Tie/Hash.pm
%{_libexecdir}/perl5/%{pversion}/XSLoader.pm
%{_libexecdir}/perl5/%{pversion}/warnings.pm
%{_libexecdir}/perl5/%{pversion}/warnings/
%{_libexecdir}/perl5/%{pversion}/AutoLoader.pm
%{_libexecdir}/perl5/%{pversion}/FileHandle.pm
%{_libexecdir}/perl5/%{pversion}/SelectSaver.pm
%{_libexecdir}/perl5/%{pversion}/Symbol.pm
%{_libexecdir}/perl5/%{pversion}/base.pm
%{_libexecdir}/perl5/%{pversion}/bytes.pm
%{_libexecdir}/perl5/%{pversion}/bytes_heavy.pl
%{_libexecdir}/perl5/%{pversion}/constant.pm
%{_libexecdir}/perl5/%{pversion}/fields.pm
%{_libexecdir}/perl5/%{pversion}/feature.pm
%{_libexecdir}/perl5/%{pversion}/integer.pm
%{_libexecdir}/perl5/%{pversion}/locale.pm
%{_libexecdir}/perl5/%{pversion}/overload.pm
%{_libexecdir}/perl5/%{pversion}/overloading.pm
%{_libexecdir}/perl5/%{pversion}/parent.pm
%{_libexecdir}/perl5/%{pversion}/strict.pm
%{_libexecdir}/perl5/%{pversion}/unicore/Heavy.pl
%{_libexecdir}/perl5/%{pversion}/utf8.pm
%{_libexecdir}/perl5/%{pversion}/utf8_heavy.pl
%{_libexecdir}/perl5/%{pversion}/vars.pm
%{_libexecdir}/perl5/%{pversion}/version.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Data/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Digest/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/File/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/List/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Scalar/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Dir.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/File.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Handle.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Pipe.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Poll.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Seekable.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Select.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Socket.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/IO/Socket/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/B.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Config.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Config_heavy.pl
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Cwd.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/DynaLoader.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Errno.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Fcntl.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/POSIX.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/Socket.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/attributes.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/Data/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/Digest/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/Fcntl/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/File/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/IO/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/List/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/Cwd/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/Socket/
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/POSIX/POSIX.so
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/lib.pm
%{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/re.pm
EOF
{
  sed -e 's/^/%%exclude /' perl-base-filelist
  (cd %{buildroot}
   for i in usr/lib/perl5/*/pod/*; do
     case $i in */perldiag.pod) ;;
     *) echo "%%exclude /$i" ;;
     esac
   done)
} > perl-base-excludes

%files base -f perl-base-filelist
%license Copying Artistic
%dir %{_libexecdir}/perl5
%dir %{_libexecdir}/perl5/%{pversion}
%dir %{_libexecdir}/perl5/%{pversion}/B
%dir %{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*
%dir %{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto
%dir %{_libexecdir}/perl5/%{pversion}/*-linux-thread-multi*/auto/POSIX
%{_bindir}/perl
%{_bindir}/perl%{pversion}
%{_mandir}/man1/perl.1%{?ext_man}

%files -f perl-base-excludes
%exclude %{_bindir}/perl
%exclude %{_bindir}/perl%{pversion}
%{_bindir}/*
%{_libexecdir}/perl5/*
%config %{_sysconfdir}/rpm/macros.perl

%files doc
%doc README.macros
%exclude %{_mandir}/man1/perl.1.gz
%exclude %{_libexecdir}/perl5/*/pod/perldiag.pod
%{_mandir}/man1/*
%{_mandir}/man3/*
%doc %{_libexecdir}/perl5/*/pod

%changelog
