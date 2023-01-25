#
# spec file for package urlview (Version 0.9)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           urlview
Version:        0.9
Release:        663
License:        GPL-2.0+
Summary:        An URL extractor/viewer
Url:            https://github.com/sigpipe/urlview
Group:          Productivity/Networking/Web/Browsers
Source:         urlview-%{version}.tar.bz2
Source1:        skel.urlview
Patch0:         urlview-%{version}.dif
Patch1:         url_handler.diff
BuildRequires:  ncurses-devel automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
urlview presents a menu of all URLs from a given text file (e.g., a
mail). The user may then view the information located on those URLs.

%prep
%setup -q
%patch0
%patch1

%__rm -rf regex/

%build
aclocal
automake -a --foreign
autoconf
CC="%__cc" \
CFLAGS="-W -Wall -Wstrict-prototypes -Wpointer-arith %{optflags} -pipe -I. -D_GNU_SOURCE" \
%configure
%__make %{?_smp_flags}

%install
mkdir -p "%{buildroot}%{_sysconfdir}"
mkdir -p "%{buildroot}%{_mandir}/man1"
make DESTDIR=%{buildroot} install
%if 0%{?suse_version}
%__install -m 755 url_handler.sh.suse "%{buildroot}%{_bindir}/url_handler.sh"
%__install -m 644 urlview.conf.suse "%{buildroot}%{_sysconfdir}/urlview.conf"
%__install -D -m 644 "%{S:1}" "%{buildroot}%{_sysconfdir}/skel/.urlview"
%endif

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%if 0%{?suse_version}
%config(noreplace) %{_sysconfdir}/skel/.urlview
# maybe a user edits this...
%config %{_bindir}/url_handler.sh
%config %{_sysconfdir}/urlview.conf
%endif
%{_bindir}/urlview
%doc %{_mandir}/man1/urlview.1%{ext_man}

%changelog
