#
# spec file for package chawan
#
# Copyright (c) 2026 mantarimay
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


Name:           chawan
Version:        0.3.3
Release:        0
Summary:        Modern terminal-based web browser and pager
License:        Unlicense
URL:            https://git.sr.ht/~bptato/chawan
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildRequires:  libopenssl-devel
BuildRequires:  libbrotli-devel
BuildRequires:  libssh2-devel
BuildRequires:  nim
ExcludeArch:    i586 armv7hl

%description
Chawan is a text-based web browser and pager designed to run entirely
in a terminal. The browser supports HTML with CSS styling, inline image
rendering in compatible terminals, and JavaScript execution for
interactive pages.

%prep
%autosetup -n %{name}-v%{version}

%build
%make_build

%install
%make_install PREFIX=/usr

%files
%license UNLICENSE res/license.md
%doc README.md
%{_bindir}/cha
%{_bindir}/mancha
%if 0%{?suse_version} > 1600
%dir %{_libexecdir}/chawan
%dir %{_libexecdir}/chawan/cgi-bin
%{_libexecdir}/chawan/cgi-bin/*
%{_libexecdir}/chawan/*
%else
%dir %{_prefix}/libexec/chawan
%{_prefix}/libexec/chawan/*
%endif
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%changelog
