#
# spec file for package source-highlight
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


%define soname  4
Name:           source-highlight
Version:        3.1.9
Release:        0
Summary:        Source Code Highlighter with Support for Many Languages
License:        GPL-3.0-only
Group:          Productivity/Publishing/Other
URL:            https://www.gnu.org/software/src-highlite
Source0:        https://ftp.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Source4:        source-highlight-apache2.conf
Patch0:         source-highlight-doxygen_disable_timestamp_in_footer.patch
# PATCH-FIX-OPENSUSE use-lessopen.patch boo#1016309 fcrozat@suse.com -- use lessopen, not lesspipe
Patch1:         use-lessopen.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Remove-throw-specifications.patch
BuildRequires:  bison
BuildRequires:  ctags
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  help2man
BuildRequires:  libboost_regex-devel
BuildRequires:  libicu-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  texinfo
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Source-highlight reads source language specifications dynamically, thus it can
be easily extended (without recompiling the sources) for handling new
languages. It also reads output format specifications dynamically, and thus it
can be easily extended (without recompiling the sources) for handling new
output formats. The syntax for these specifications is quite easy (take a look
at the manual).

%package -n libsource-highlight%{soname}
Summary:        Source Code Highlighting C++ Library
Group:          System/Libraries
# libsource-highlight is only used by gdb, which does not use the ctags
# feature. Use a recommendation instead of a hard requirement, bsc#1193401
Recommends:     ctags

%description -n libsource-highlight%{soname}
Source-highlight reads source language specifications dynamically, thus it can
be easily extended (without recompiling the sources) for handling new
languages. It also reads output format specifications dynamically, and thus it
can be easily extended (without recompiling the sources) for handling new
output formats. The syntax for these specifications is quite easy (take a look
at the manual).

libsource-highlight is a C++ library that provides the features of
Source-highlight.

%package -n libsource-highlight-devel
Summary:        Source Code Highlighting C++ Library
Group:          Development/Libraries/C and C++
Requires:       libsource-highlight%{soname} = %{version}-%{release}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description -n libsource-highlight-devel
Source-highlight reads source language specifications dynamically, thus it can
be easily extended (without recompiling the sources) for handling new
languages. It also reads output format specifications dynamically, and thus it
can be easily extended (without recompiling the sources) for handling new
output formats. The syntax for these specifications is quite easy (take a look
at the manual).

libsource-highlight is a C++ library that provides the features of
Source-highlight.

%package cgi
Summary:        Source Code Highlighting CGI
Group:          Productivity/Networking/Web/Utilities
Requires:       apache2

%description cgi
Source-highlight reads source language specifications dynamically, thus it can
be easily extended (without recompiling the sources) for handling new
languages. It also reads output format specifications dynamically, and thus it
can be easily extended (without recompiling the sources) for handling new
output formats. The syntax for these specifications is quite easy (take a look
at the manual).

This package contains a CGI that can be used to highlight source code on
your webserver using source-highlight.

%prep
%autosetup -p1

sed -i 's/\r//g' doc/*.css

%build
BOOST_REGEX=$(/bin/ls -1 "%{_libdir}"/libboost_regex*mt*.so 2>/dev/null | head -1)
[ -n "$BOOST_REGEX" ] || BOOST_REGEX=$(/bin/ls -1 "%{_libdir}"/libboost_regex*.so 2>/dev/null | head -1)
if [ -n "$BOOST_REGEX" ]; then
    BOOST_REGEX="${BOOST_REGEX##*/lib}"
    BOOST_REGEX="${BOOST_REGEX%.so}"
    BOOST_REGEX_PARAM="--with-boost-regex=${BOOST_REGEX}"
else
    BOOST_REGEX_PARAM=""
fi

%configure \
  "$BOOST_REGEX_PARAM" \
  --with-bash-completion="%{_sysconfdir}/bash_completion.d" \
  --with-doxygen \
  --enable-static=no
%make_build
%make_build -C src source-highlight-cgi

%install
%make_install

install -d "%{buildroot}/srv/source-highlight"
libtool --mode=install install -m 0755 src/source-highlight-cgi "%{buildroot}/srv/source-highlight/source-highlight.cgi"
install -D -m0644 "%{SOURCE4}" "%{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf"

find %{buildroot} -type f -name "*.la" -delete -print

rm -rf "%{buildroot}%{_docdir}/%{name}/html"
rm -rf "%{buildroot}%{_datadir}/doc"

chmod 0644 AUTHORS ChangeLog COPYING CREDITS NEWS README THANKS TODO.txt

%if 0%{?suse_version} >= 1030
%fdupes -s "%{buildroot}%{_datadir}/"
%endif

%post
%install_info --info-dir="%{_infodir}" "%{_infodir}/source-highlight".info%{ext_info}

%preun
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/source-highlight".info%{ext_info}

%post -n libsource-highlight-devel
%install_info --info-dir="%{_infodir}" "%{_infodir}/source-highlight-lib".info%{ext_info}

%preun -n libsource-highlight-devel
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/source-highlight-lib".info%{ext_info}

%post   -n libsource-highlight%{soname} -p /sbin/ldconfig
%postun -n libsource-highlight%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog CREDITS NEWS README THANKS TODO.txt
%config %{_sysconfdir}/bash_completion.d/source-highlight
%{_bindir}/*
%{_datadir}/source-highlight
%{_mandir}/man1/*.1%{?ext_man}
%{_infodir}/source-highlight.info%{ext_man}

%files -n libsource-highlight%{soname}
%{_libdir}/libsource-highlight.so.%{soname}
%{_libdir}/libsource-highlight.so.%{soname}.*.*

%files -n libsource-highlight-devel
%{_includedir}/srchilite
%{_libdir}/libsource-highlight.so
%{_libdir}/pkgconfig/source-highlight.pc
%{_infodir}/source-highlight-lib.info%{?ext_info}

%files cgi
%config(noreplace) %{_sysconfdir}/apache2/conf.d/source-highlight.conf
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%dir /srv/source-highlight
/srv/source-highlight/source-highlight.cgi

%changelog
