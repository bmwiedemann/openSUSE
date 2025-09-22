#
# spec file for package readpe (formerly known as 'pev')
#
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           readpe
Version:        0.85.1
Release:        0
Summary:        Text-based tool to analyze PE files
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://github.com/mentebinaria/readpe
#Git-Clone:     https://github.com/mentebinaria/readpe.git
Source:         https://github.com/mentebinaria/readpe/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libopenssl-devel
BuildRequires:  pcre2-devel
Obsoletes:      pev < %{version}
Provides:       bundled(udis86) = 1.7.2

%description
A tool to get information of PE32/PE32+ executables (EXE, DLL, OCX, ...)
like headers, sections, resources and more.

%package -n libpe1
Summary:        Library for PE file parsing
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libpe1
The PE library used by pev - the PE file toolkit.
Features
 * Support for both 32 and 64-bits PE files.
 * ssdeep support (built-in libfuzzy).
 * Disassemble support (built-in libudis86).
 * Imphash support.
 * Crypographic digests calculation (using OpenSSL).

This subpackage contains shared library part of libpe.

%prep
%autosetup
sed -e '1{/^#!/ d}' -i completion/bash/readpe

%build
%make_build CFLAGS="%{optflags}" prefix=%{_prefix} libdir=%{_libdir}

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
rm %{buildroot}%{_libdir}/libpe.so
# HACK: fix library permissions
chmod +x %{buildroot}/%{_libdir}/libpe.so.*

install -Dm 0644 completion/bash/readpe %{buildroot}/%{_datadir}/bash-completion/completions/%{name}.bash
install -Dm 0644 completion/zsh/_readpe %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

%ldconfig_scriptlets -n libpe1

%files
%license LICENSE LICENSE.OpenSSL
%doc README.md
%{_bindir}/ofs2rva
%{_bindir}/pedis
%{_bindir}/pehash
%{_bindir}/peldd
%{_bindir}/pepack
%{_bindir}/peres
%{_bindir}/pescan
%{_bindir}/pesec
%{_bindir}/pestr
%{_bindir}/readpe
%{_bindir}/rva2ofs
%dir %{_libdir}/pev
%dir %{_libdir}/pev/plugins
%{_libdir}/pev/plugins/csv_plugin.so
%{_libdir}/pev/plugins/html_plugin.so
%{_libdir}/pev/plugins/json_plugin.so
%{_libdir}/pev/plugins/text_plugin.so
%{_libdir}/pev/plugins/xml_plugin.so
%dir %{_datadir}/pev
%{_datadir}/pev/userdb.txt
%{_mandir}/man1/*%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}.bash
%{_datadir}/zsh

%files -n libpe1
%{_libdir}/libpe.so.*

%changelog
