#
# spec file for package aria2
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


%define         somajor 0
Name:           aria2
Version:        1.34.0
Release:        0
Summary:        Parallelizing Multi-Protocol Utility for Downloading Files
License:        SUSE-GPL-2.0-with-openssl-exception
Group:          Productivity/Networking/Other
URL:            https://aria2.github.io
Source0:        https://github.com/aria2/aria2/releases/download/release-%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.changes
# PATCH-FIX-UPSTREAM aria2-CVE-2019-3500.patch boo#1120488
Patch0:         aria2-CVE-2019-3500.patch
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libuv) >= 1.13
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
Recommends:     ca-certificates

%description
aria2 is a utility for downloading files. It has a segmented
downloading engine in its core. It can download one file from
multiple URLs or multiple connections from one URL. This can be used
to speed up downloads with certain networks. The engine in was
implemented in a single-thread model.

aria2 currently supports HTTP, FTP, and BitTorrent.

%lang_package

%package -n lib%{name}-%{somajor}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n lib%{name}-%{somajor}
aria2 is a utility for downloading files. It has a segmented
downloading engine in its core. It can download one file from
multiple URLs or multiple connections from one URL. This can be used
to speed up downloads with certain networks. The engine in was
implemented in a single-thread model.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{somajor} = %{version}

%description devel
aria2 is a utility for downloading files. It has a segmented
downloading engine in its core. It can download one file from
multiple URLs or multiple connections from one URL. This can be used
to speed up downloads with certain networks. The engine in was
implemented in a single-thread model.

This package contains development files for its shared library.

%prep
%setup -q
%patch0 -p1
# Do not use current date
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.cc' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
%configure \
  --docdir=%{_defaultdocdir}/%{name}/ \
  --with-bashcompletiondir=%{_sysconfdir}/bash_completion.d/ \
  --enable-libaria2 \
  --with-libuv \
  --disable-silent-rules
# We don't specify a ca-bundle because that makes aria2 call gnutls_certificate_set_x509_trust_file()
# insted of gnutls_certificate_set_x509_system_trust().
#           --with-ca-bundle=/etc/ssl/ca-bundle.pem
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Only installation instructions
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/bash_completion
# Lets use more suitable location
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/aria2c \
  %{buildroot}%{_datadir}/bash-completion/completions/aria2c

%find_lang aria2 --with-man

# Testsuite needs working network connection
# %%check
# make %{?_smp_mflags} check

%post -n lib%{name}-%{somajor} -p /sbin/ldconfig
%postun -n lib%{name}-%{somajor} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.html README.rst
%{_docdir}/%{name}/xmlrpc/
%{_bindir}/aria2c
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/aria2c
%{_mandir}/man1/aria2c.1%{?ext_man}
%{_mandir}/pt/man1/aria2c.1%{?ext_man}
%{_mandir}/ru/man1/aria2c.1%{?ext_man}

%files lang -f %{name}.lang

%files -n lib%{name}-%{somajor}
%license COPYING
%{_libdir}/libaria2.so.%{somajor}*

%files devel
%license COPYING
%{_includedir}/aria2/
%{_libdir}/libaria2.so
%{_libdir}/pkgconfig/libaria2.pc

%changelog
