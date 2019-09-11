#
# spec file for package surfraw
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


# Requires perl-WWW-OpenSearch not in factory
%bcond_with     elvi_opensearch

Name:           surfraw
Version:        2.3.0
Release:        0
Summary:        Command Line Interface to WWW Search Engines
License:        SUSE-Public-Domain
Group:          Productivity/Networking/Web/Browsers
URL:            https://gitlab.com/surfraw/Surfraw
Source:         https://gitlab.com/surfraw/Surfraw/uploads/2de827b2786ef2fe43b6f07913ca7b7f/%{name}-%{version}.tar.gz
Patch0:         test-show-failing-url.patch
# PATCH-FIX-UPSTREAM
Patch1:         reproducible.patch
BuildRequires:  htdig
BuildRequires:  make
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-LWP-Protocol-https
BuildRequires:  perl-libwww-perl
%if %{with elvi_opensearch}
BuildRequires:  perl-WWW-OpenSearch
%endif
BuildRequires:  sed
BuildRequires:  w3m
BuildRequires:  wget
Requires:       sed
Requires:       w3m
Requires:       xdg-utils
BuildArch:      noarch

%description
Surfraw provides a Unix command line interface to a variety of
WWW search engines and other artifacts of information and makes
them available as extensions to the shell.
Surfraw abstracts the browser away from input. Interpretation of
linguistic forms is handed back to the shell.

%if %{with elvi_opensearch}
%package opensearch
Summary:        Surfraw OpenSearch support
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Requires:       perl-HTML-Parser
Requires:       perl-LWP-Protocol-https
Requires:       perl-WWW-OpenSearch
Requires:       perl-libwww-perl

%description opensearch
Surfraw OpenSearch provides opensearch support.
%endif

%package woffle
Summary:        Surfraw woffle
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Requires:       htdig
Requires:       wget

%description woffle
Surfraw elvi woffle.

Uses htdig to create an index that needs to be served via a webserver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod a+x elvi/phpdoc

%build
%configure --libdir=%{_libexecdir} \
%if %{without elvi_opensearch}
            --disable-opensearch \
%endif
            --with-text-browser=w3m \
            --with-graphical-browser=xdg-open
make %{?_smp_mflags}

%install
%make_install
# These depend on apt-cache
rm %{buildroot}/%{_libexecdir}/%{name}/debpkghome
rm %{buildroot}/%{_libexecdir}/%{name}/debvcsbrowse

%check
# Several elvi fail trying to re-use elvi duckduckgo and google , resulting in
# Get failed: 501 Protocol scheme 'surfraw' is not supported
# as it is trying to fetch `surfraw: duckduckgo: No elvis or bookmark with that name`
mkdir -p $HOME/.config/surfraw/elvi
cp elvi/duckduckgo $HOME/.config/surfraw/elvi
cp elvi/google $HOME/.config/surfraw/elvi

rm test/debpkghome.test
rm test/debvcsbrowse.test

export BROWSER=echo
export PATH=${PWD}/%{buildroot}/%{_libexecdir}/%{name}:$PATH
./test/runtests

%files
%doc AUTHORS ChangeLog HACKING NEWS TODO surfraw.lsm
%license COPYING
%{_bindir}/sr
%{_bindir}/%{name}
%{_bindir}/surfraw-update-path
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/bookmarks
%config(noreplace) %{_sysconfdir}/xdg/%{name}/conf
%exclude %{_libexecdir}/%{name}/woffle
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%exclude %{_mandir}/man1/opensearch-* 
%{_mandir}/man1/*.1*

%if %{with elvi_opensearch}
%files opensearch
%license COPYING
%{_bindir}/opensearch*
%{_mandir}/man1/opensearch-* 
%endif

%files woffle
%license COPYING
%{_libexecdir}/%{name}/woffle

%changelog
