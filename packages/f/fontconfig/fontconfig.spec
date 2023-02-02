#
# spec file for package fontconfig
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


Name:           fontconfig
%define lname   libfontconfig1
Version:        2.14.2
Release:        0
Summary:        Library for Font Configuration
License:        MIT
Group:          System/Libraries
URL:            https://www.freedesktop.org/wiki/Software/fontconfig/
Source0:        https://www.freedesktop.org/software/fontconfig/release/fontconfig-%{version}.tar.xz
Source4:        baselibs.conf
Source5:        local.conf
Patch1:         skip-network-test.patch
BuildRequires:  automake >= 1.11
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(uuid)
Provides:       ipa-fonts-config = 003.02
Obsoletes:      ipa-fonts-config < 003.02
Provides:       IPA-fonts-config = 003.02
Obsoletes:      IPA-fonts-config < 003.02

%description
Fontconfig is a library for configuring and customizing font access. It
contains two essential modules: the configuration module, which builds
an internal configuration from XML files, and the matching module,
which accepts font patterns and returns the nearest matching font.

%lang_package

%package -n %{lname}
Summary:        Library for font configuration
Group:          System/Libraries
Requires:       %{name}

%description -n %{lname}
Fontconfig is a library for configuring and customizing font access. It
contains two essential modules: the configuration module, which builds
an internal configuration from XML files, and the matching module,
which accepts font patterns and returns the nearest matching font.

%package doc
Summary:        Documentation for fontconfig
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Extended documentation for the fontconfig library.

%package devel
Summary:        Header files for fontconfig
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       gettext-devel
Requires:       glibc-devel
Requires:       pkgconfig(freetype2)

%description devel
This package countains all include files, libraries, configuration
files needed for compiling applications which use the fontconfig
library.

%package devel-doc
Summary:        Developer documentation for libfontconfig
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
HTML documentation and manual pages for developers using the
fontconfig library.

%prep
%autosetup -p1
# use suse-specific doc path:
find -name \*.1 -o -name \*.sgml -exec sed -i -e 's/usr\/share\/doc\/fontconfig/usr\/share\/doc\/packages\/fontconfig/g' {} +

%build
# We don't want to rebuild the docs, but we want to install the included ones.
export HASDOCBOOK=no
%configure \
        --docdir=%{_docdir}/%{name} \
        --disable-silent-rules \
        --with-arch=%{_host_cpu} \
        --disable-static \
  	--disable-libxml2 \
  	--with-add-fonts=%{_prefix}/X11R6/lib/X11/fonts,/opt/kde3/share/fonts,%{_prefix}/local/share/fonts
make %{?_smp_mflags}

%check
export MALLOC_CHECK_=2
make %{?_smp_mflags} check
unset MALLOC_CHECK_

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# package /etc/fonts/conf.avail for compatibility reasons
mkdir %{buildroot}%{_sysconfdir}/fonts/conf.avail
install -m 644 conf.d/README %{buildroot}%{_sysconfdir}/fonts/conf.d
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/fonts
# tune links in conf.d
pushd %{buildroot}%{_sysconfdir}/fonts/conf.d
    mv 50-user.conf 56-user.conf
    rm 51-local.conf
    ln -s ../local.conf 55-local.conf
    # leave place for 60-family-prefer.conf from fonts-config
    mv 60-latin.conf 61-latin.conf
popd
mkdir -p %{buildroot}/%{_docdir}/%{name}
%find_lang %{name}
%find_lang %{name}-conf

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%dir %{_sysconfdir}/fonts
%dir %{_sysconfdir}/fonts/conf.d
# packaging /etc/fonts/conf.avail for compatibility reasons
%dir %{_sysconfdir}/fonts/conf.avail
%config %{_sysconfdir}/fonts/fonts.conf
%config %{_sysconfdir}/fonts/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/fonts/local.conf
%{_sysconfdir}/fonts/conf.d/README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/conf.avail
%{_datadir}/%{name}/conf.avail/*.conf
%dir %{_datadir}/xml/%{name}
%{_datadir}/xml/%{name}/fonts.dtd
%dir %{_localstatedir}/cache/fontconfig/
%{_mandir}/man5/fonts-conf.5%{ext_man}
%{_mandir}/man1/*

%files lang -f %{name}.lang -f %{name}-conf.lang

%files doc
%doc AUTHORS ChangeLog README
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/fontconfig-user.html
%{_docdir}/%{name}/fontconfig-user.pdf
%{_docdir}/%{name}/fontconfig-user.txt

%files devel
%{_libdir}/pkgconfig/fontconfig.pc
%{_libdir}/libfontconfig.so
%{_includedir}/fontconfig/
%dir %{_datadir}/gettext/its/
%{_datadir}/gettext/its/fontconfig.*

%files devel-doc
%{_docdir}/%{name}/%{name}-devel/
%{_docdir}/%{name}/fontconfig-devel.pdf
%{_docdir}/%{name}/fontconfig-devel.txt
%{_mandir}/man3/*

%files -n %{lname}
%{_libdir}/libfontconfig.so.*

%changelog
