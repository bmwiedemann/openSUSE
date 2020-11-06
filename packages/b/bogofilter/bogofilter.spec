#
# spec file for package bogofilter
#
# Copyright (c) 2020 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == ""
ExclusiveArch:  do-not-build
%else
%define dash -
%define src -src
%if "%{flavor}" == "db"
%define with_db 1
%endif
%if "%{flavor}" == "sqlite3"
%define with_sqlite3 1
%endif
%if "%{flavor}" == "kyotocabinet"
%define with_kyotocabinet 1
%endif
%endif

%define _name   bogofilter
Name:           %{_name}%{?dash}%{?flavor}%{?src}
Version:        1.2.4
Release:        0
Summary:        Fast Anti-Spam Filtering by Bayesian Statistical Analysis
License:        GPL-2.0-or-later
URL:            http://bogofilter.sourceforge.net/
Source:         http://downloads.sourceforge.net/bogofilter/bogofilter-%{version}.tar.bz2
Source10:       README.SUSE
# PATCH-FEATURE-OPENSUSE bogofilter-kyotocabinet.patch --replace tokyocabinet with kyotocabinet following
# tokyocabinet recommendations
Patch0:         bogofilter-kyotocabinet.patch
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?with_db}
BuildRequires:  db-devel
%endif
BuildRequires:  flex
BuildRequires:  gsl-devel
BuildRequires:  sharutils
%if 0%{?with_sqlite3}
BuildRequires:  sqlite3-devel
%endif
BuildRequires:  xmlto
%if 0%{?with_kyotocabinet}
BuildRequires:  libkyotocabinet-devel
BuildRequires:  libxml2-tools
%endif

%description
Bogofilter is a Bayesian spam filter.  In normal operation, it takes an
e-mail message or text from standard input, does a statistical check
against lists of "good" and "bad" words, and returns a status code
indicating whether the message is spam.  Bogofilter is designed with
fast algorithms (including the Berkeley DB system), coded directly in
C, and tuned for speed, so it can be used for production by sites that
process a lot of mail.

%package -n %{_name}-common
Summary:        Fast Anti-Spam Filtering by Bayesian Statistical Analysis
Requires:       %{_name}-backend = %{version}
BuildArch:      noarch

%description -n %{_name}-common
Bogofilter is a Bayesian spam filter.  In normal operation, it takes an
e-mail message or text from standard input, does a statistical check
against lists of "good" and "bad" words, and returns a status code
indicating whether the message is spam.  Bogofilter is designed with
fast algorithms (including the Berkeley DB system), coded directly in
C, and tuned for speed, so it can be used for production by sites that
process a lot of mail.

This package contains shared files for various %{_name} backends

%package -n %{_name}-doc
Summary:        Bogofilter documentation
BuildArch:      noarch

%description -n %{_name}-doc
This package contains the documentation of %{_name}

%package -n %{_name}-kyotocabinet
Summary:        Bogofilter kyotocabinet backend
Requires:       %{_name}-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{_name}-backend = %{version}-%{release}
Provides:       %{_name}-tokyocabinet = %{version}
# Please remove the "=" of the obsoletes tag with the next update
Obsoletes:      %{_name}-tokyocabinet <= %{version}

%description -n %{_name}-kyotocabinet
This package contains %{_name} build with the tokyocabinet backend.

%package -n %{_name}-sqlite3
Summary:        Bogofilter sqlite3 backend
Requires:       %{_name}-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{_name}-backend = %{version}-%{release}
%if 0%{?suse_version} == 1310
Conflicts:      %{_name}-db
%endif

%description -n %{_name}-sqlite3
This package contains %{_name} build with the sqlite3 backend.

%package -n %{_name}-db
Summary:        Bogofilter libdb backend
Requires:       %{_name}-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{_name} = %{version}-%{release}
Obsoletes:      %{_name}
Provides:       %{_name}-backend = %{version}-%{release}
%if 0%{?suse_version} == 1310
Conflicts:      %{_name}-sqlite3
%endif

%description -n %{_name}-db
This package contains %{_name} build with the libdb backend.

%prep
%setup -q -n %{_name}-%{version}
%if 0%{?suse_version} > 1320
%patch0 -p1
%endif

%build
autoreconf -fiv
%configure \
	--with-database=%{flavor} \
	--program-suffix=-%{flavor}
make %{?_smp_mflags}

%install
%make_install
# create a dummy target for alternatives
install -d %{buildroot}%{_sysconfdir}/alternatives
for i in bogofilter bogolexer bogotune bogoutil bf_compact bf_copy bf_tar; do
	touch %{buildroot}%{_sysconfdir}/alternatives/${i}
	touch %{buildroot}%{_sysconfdir}/alternatives/${i}.1.gz
	ln -s %{_sysconfdir}/alternatives/${i} %{buildroot}%{_bindir}/${i}
%if "%{flavor}" == "db"
	ln -s %{_sysconfdir}/alternatives/${i}.1.gz %{buildroot}%{_mandir}/man1/${i}.1.gz
%endif
done
%if "%{flavor}" == "db"
mv %{buildroot}/%{_sysconfdir}/bogofilter.cf.example %{buildroot}/%{_sysconfdir}/bogofilter.cf
# bogoupgrade is written in perl and therefore belongs to the common package
mv %{buildroot}/%{_bindir}/bogoupgrade-db %{buildroot}/%{_bindir}/bogoupgrade
mv %{buildroot}/%{_mandir}/man1/bogoupgrade-db.1 %{buildroot}/%{_mandir}/man1/bogoupgrade.1

for d in contrib; do
	install -d %{buildroot}%{_datadir}/%{_name}/${d}
	files=$( find ${d} -maxdepth 1 -type f)
	for f in ${files} ; do
		case ${f} in
			*.c|*.o|*.obj|*/Makefile*) continue ;;
			*.1)
				cp -p ${f} %{buildroot}/%{_mandir}/man1 ;;
			*)
				cp -p ${f} %{buildroot}/%{_datadir}/%{_name}/${d}
				head -n 1 ${f} | grep -q "^#\!" && \
					chmod 0755 %{buildroot}/%{_datadir}/%{_name}/${d}/${f##*/}
				;;
		esac
	done
done
# add a vendor README to the doc package
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_defaultdocdir}/bogofilter-doc/README.SUSE
%else
rm %{buildroot}/%{_bindir}/bogoupgrade-*
rm %{buildroot}/%{_mandir}/man1/bogoupgrade-*
rm %{buildroot}/%{_sysconfdir}/bogofilter.cf.example
%endif

%if "%{flavor}" == "kyotocabinet"
%post -n %{_name}-kyotocabinet
%{_sbindir}/update-alternatives --install %{_bindir}/bogofilter bogofilter %{_bindir}/bogofilter-kyotocabinet 10 \
 --slave %{_mandir}/man1/bogofilter.1.gz bogofilter.1.gz %{_mandir}/man1/bogofilter-kyotocabinet.1.gz \
 --slave %{_bindir}/bogolexer bogolexer %{_bindir}/bogolexer-kyotocabinet \
 --slave %{_mandir}/man1/bogolexer.1.gz bogolexer.1.gz %{_mandir}/man1/bogolexer-kyotocabinet.1.gz \
 --slave %{_bindir}/bogotune bogotune %{_bindir}/bogotune-kyotocabinet \
 --slave %{_mandir}/man1/bogotune.1.gz bogotune.1.gz %{_mandir}/man1/bogotune-kyotocabinet.1.gz \
 --slave %{_bindir}/bogoutil bogoutil %{_bindir}/bogoutil-kyotocabinet \
 --slave %{_mandir}/man1/bogoutil.1.gz bogoutil.1.gz %{_mandir}/man1/bogoutil-kyotocabinet.1.gz \
 --slave %{_bindir}/bf_compact bf_compact %{_bindir}/bf_compact-kyotocabinet \
 --slave %{_mandir}/man1/bf_compact.1.gz bf_compact.1.gz %{_mandir}/man1/bf_compact-kyotocabinet.1.gz \
 --slave %{_bindir}/bf_copy bf_copy %{_bindir}/bf_copy-kyotocabinet \
 --slave %{_mandir}/man1/bf_copy.1.gz bf_copy.1.gz %{_mandir}/man1/bf_copy-kyotocabinet.1.gz \
 --slave %{_bindir}/bf_tar bf_tar %{_bindir}/bf_tar-kyotocabinet \
 --slave %{_mandir}/man1/bf_tar.1.gz bf_tar.1.gz %{_mandir}/man1/bf_tar-kyotocabinet.1.gz

%postun -n %{_name}-kyotocabinet
if [ ! -f %{_bindir}/bogofilter-kyotocabinet ] ; then
	%{_sbindir}/update-alternatives --remove bogofilter %{_bindir}/bogofilter-kyotocabinet
fi
%endif

%if "%{flavor}" == "sqlite3"
%post -n %{_name}-sqlite3
%{_sbindir}/update-alternatives --install %{_bindir}/bogofilter bogofilter %{_bindir}/bogofilter-sqlite3 30 \
 --slave %{_mandir}/man1/bogofilter.1.gz bogofilter.1.gz %{_mandir}/man1/bogofilter-sqlite3.1.gz \
 --slave %{_bindir}/bogolexer bogolexer %{_bindir}/bogolexer-sqlite3 \
 --slave %{_mandir}/man1/bogolexer.1.gz bogolexer.1.gz %{_mandir}/man1/bogolexer-sqlite3.1.gz \
 --slave %{_bindir}/bogotune bogotune %{_bindir}/bogotune-sqlite3 \
 --slave %{_mandir}/man1/bogotune.1.gz bogotune.1.gz %{_mandir}/man1/bogotune-sqlite3.1.gz \
 --slave %{_bindir}/bogoutil bogoutil %{_bindir}/bogoutil-sqlite3 \
 --slave %{_mandir}/man1/bogoutil.1.gz bogoutil.1.gz %{_mandir}/man1/bogoutil-sqlite3.1.gz \
 --slave %{_bindir}/bf_compact bf_compact %{_bindir}/bf_compact-sqlite3 \
 --slave %{_mandir}/man1/bf_compact.1.gz bf_compact.1.gz %{_mandir}/man1/bf_compact-sqlite3.1.gz \
 --slave %{_bindir}/bf_copy bf_copy %{_bindir}/bf_copy-sqlite3 \
 --slave %{_mandir}/man1/bf_copy.1.gz bf_copy.1.gz %{_mandir}/man1/bf_copy-sqlite3.1.gz \
 --slave %{_bindir}/bf_tar bf_tar %{_bindir}/bf_tar-sqlite3 \
 --slave %{_mandir}/man1/bf_tar.1.gz bf_tar.1.gz %{_mandir}/man1/bf_tar-sqlite3.1.gz

%postun -n %{_name}-sqlite3
if [ ! -f %{_bindir}/bogofilter-sqlite3 ] ; then
	%{_sbindir}/update-alternatives --remove bogofilter %{_bindir}/bogofilter-sqlite3
fi
%endif

%if "%{flavor}" == "db"
%post -n %{_name}-db
%{_sbindir}/update-alternatives --install %{_bindir}/bogofilter bogofilter %{_bindir}/bogofilter-db 50 \
 --slave %{_mandir}/man1/bogofilter.1.gz bogofilter.1.gz %{_mandir}/man1/bogofilter-db.1.gz \
 --slave %{_bindir}/bogolexer bogolexer %{_bindir}/bogolexer-db \
 --slave %{_mandir}/man1/bogolexer.1.gz bogolexer.1.gz %{_mandir}/man1/bogolexer-db.1.gz \
 --slave %{_bindir}/bogotune bogotune %{_bindir}/bogotune-db \
 --slave %{_mandir}/man1/bogotune.1.gz bogotune.1.gz %{_mandir}/man1/bogotune-db.1.gz \
 --slave %{_bindir}/bogoutil bogoutil %{_bindir}/bogoutil-db \
 --slave %{_mandir}/man1/bogoutil.1.gz bogoutil.1.gz %{_mandir}/man1/bogoutil-db.1.gz \
 --slave %{_bindir}/bf_compact bf_compact %{_bindir}/bf_compact-db \
 --slave %{_mandir}/man1/bf_compact.1.gz bf_compact.1.gz %{_mandir}/man1/bf_compact-db.1.gz \
 --slave %{_bindir}/bf_copy bf_copy %{_bindir}/bf_copy-db \
 --slave %{_mandir}/man1/bf_copy.1.gz bf_copy.1.gz %{_mandir}/man1/bf_copy-db.1.gz \
 --slave %{_bindir}/bf_tar bf_tar %{_bindir}/bf_tar-db \
 --slave %{_mandir}/man1/bf_tar.1.gz bf_tar.1.gz %{_mandir}/man1/bf_tar-db.1.gz

%postun -n %{_name}-db
if [ ! -f %{_bindir}/bogofilter-db ] ; then
	%{_sbindir}/update-alternatives --remove bogofilter %{_bindir}/bogofilter-db
fi

%files -n %{_name}-common
%defattr(-,root,root)
%{_bindir}/bogoupgrade
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%{_datadir}/%{_name}

%files -n %{_name}-doc
%defattr(-,root,root)
%doc AUTHORS COPYING GETTING.STARTED NEWS README* RELEASE.NOTES*
%doc TODO bogofilter.cf.example
%doc doc/README* doc/bogofilter-SA-* doc/*.html doc/integrating*
%doc doc/programmer/ doc/rpm.notes.BerkeleyDB
%doc %{_defaultdocdir}/bogofilter-doc/README.SUSE
%{_mandir}/man1/bogofilter.1%{ext_man}
%{_mandir}/man1/bogolexer.1%{ext_man}
%{_mandir}/man1/bogoupgrade.1%{ext_man}
%{_mandir}/man1/bogotune.1%{ext_man}
%{_mandir}/man1/bogoutil.1%{ext_man}
%{_mandir}/man1/bf_compact.1%{ext_man}
%{_mandir}/man1/bf_copy.1%{ext_man}
%{_mandir}/man1/bf_tar.1%{ext_man}

%files -n %{_name}-db
%defattr(-,root,root)
%ghost %{_sysconfdir}/alternatives/bogofilter
%ghost %{_sysconfdir}/alternatives/bogolexer
%ghost %{_sysconfdir}/alternatives/bogotune
%ghost %{_sysconfdir}/alternatives/bogoutil
%ghost %{_sysconfdir}/alternatives/bf_compact
%ghost %{_sysconfdir}/alternatives/bf_copy
%ghost %{_sysconfdir}/alternatives/bf_tar
%ghost %{_sysconfdir}/alternatives/bogofilter.1.*
%ghost %{_sysconfdir}/alternatives/bogolexer.1.*
%ghost %{_sysconfdir}/alternatives/bogotune.1.*
%ghost %{_sysconfdir}/alternatives/bogoutil.1.*
%ghost %{_sysconfdir}/alternatives/bf_compact.1.*
%ghost %{_sysconfdir}/alternatives/bf_copy.1.*
%ghost %{_sysconfdir}/alternatives/bf_tar.1.*
%{_bindir}/bogofilter
%{_bindir}/bogolexer
%{_bindir}/bogotune
%{_bindir}/bogoutil
%{_bindir}/bf_compact
%{_bindir}/bf_copy
%{_bindir}/bf_tar
%{_bindir}/*-db
%{_mandir}/man1/*-db.1%{ext_man}
%endif

%if "%{flavor}" == "kyotocabinet"
%files -n %{_name}-kyotocabinet
%defattr(-,root,root)
%ghost %{_sysconfdir}/alternatives/bogofilter
%ghost %{_sysconfdir}/alternatives/bogolexer
%ghost %{_sysconfdir}/alternatives/bogotune
%ghost %{_sysconfdir}/alternatives/bogoutil
%ghost %{_sysconfdir}/alternatives/bf_compact
%ghost %{_sysconfdir}/alternatives/bf_copy
%ghost %{_sysconfdir}/alternatives/bf_tar
%ghost %{_sysconfdir}/alternatives/bogofilter.1.*
%ghost %{_sysconfdir}/alternatives/bogolexer.1.*
%ghost %{_sysconfdir}/alternatives/bogotune.1.*
%ghost %{_sysconfdir}/alternatives/bogoutil.1.*
%ghost %{_sysconfdir}/alternatives/bf_compact.1.*
%ghost %{_sysconfdir}/alternatives/bf_copy.1.*
%ghost %{_sysconfdir}/alternatives/bf_tar.1.*
%{_bindir}/bogofilter
%{_bindir}/bogolexer
%{_bindir}/bogotune
%{_bindir}/bogoutil
%{_bindir}/bf_compact
%{_bindir}/bf_copy
%{_bindir}/bf_tar
%{_bindir}/*-kyotocabinet
%{_mandir}/man1/*-kyotocabinet.1%{ext_man}
%endif

%if "%{flavor}" == "sqlite3"
%files -n %{_name}-sqlite3
%defattr(-,root,root)
%ghost %{_sysconfdir}/alternatives/bogofilter
%ghost %{_sysconfdir}/alternatives/bogolexer
%ghost %{_sysconfdir}/alternatives/bogotune
%ghost %{_sysconfdir}/alternatives/bogoutil
%ghost %{_sysconfdir}/alternatives/bf_compact
%ghost %{_sysconfdir}/alternatives/bf_copy
%ghost %{_sysconfdir}/alternatives/bf_tar
%ghost %{_sysconfdir}/alternatives/bogofilter.1.*
%ghost %{_sysconfdir}/alternatives/bogolexer.1.*
%ghost %{_sysconfdir}/alternatives/bogotune.1.*
%ghost %{_sysconfdir}/alternatives/bogoutil.1.*
%ghost %{_sysconfdir}/alternatives/bf_compact.1.*
%ghost %{_sysconfdir}/alternatives/bf_copy.1.*
%ghost %{_sysconfdir}/alternatives/bf_tar.1.*
%{_bindir}/bogofilter
%{_bindir}/bogolexer
%{_bindir}/bogotune
%{_bindir}/bogoutil
%{_bindir}/bf_compact
%{_bindir}/bf_copy
%{_bindir}/bf_tar
%{_bindir}/*-sqlite3
%{_mandir}/man1/*-sqlite3.1%{ext_man}
%endif

%changelog
