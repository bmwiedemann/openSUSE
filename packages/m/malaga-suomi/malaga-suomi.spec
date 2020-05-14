#
# spec file for package malaga-suomi
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


%define _name voikko-fi
%define _altname suomi-malaga
Name:           malaga-suomi
Version:        2.3
Release:        0
Summary:        Description of Finnish morphology written for libvoikko
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
URL:            http://voikko.puimula.org/
Source0:        http://www.puimula.org/voikko-sources/%{_name}/%{_name}-%{version}.tar.gz
Source1:        http://www.puimula.org/voikko-sources/%{_name}/%{_name}-%{version}.tar.gz.asc
Source2:        %{_name}.keyring
# voikospell/libvoikko requires malaga-suomi for proper runtime. But to build malaga-suomi we don't need it yet
#!BuildIgnore:  malaga-suomi
BuildRequires:  foma
BuildRequires:  python3
BuildRequires:  voikkospell >= 4.0
Provides:       %{_name} = %{version}
Obsoletes:      %{_name} < %{version}
Provides:       %{_altname} = %{version}
Obsoletes:      %{_altname} < %{version}
BuildArch:      noarch

%description
Voikko-fi (previously known as suomi-malaga) is a description of Finnish 
morphology written for libvoikko. 

This package contains a compiled version of Voikko-fi using the new
unweighted VFST dictionary format. It is suitable for use in spell checking,
grammar checking and hyphenation system Voikko, provided by the libvoikko
library.

%prep
%setup -q -n %{_name}-%{version}

%build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
make %{?_smp_mflags} vvfst EXTRA_LEX=vocabulary/erikoisalat/linux-distributions.lex SM_BUILDDATE="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%{s})}")"

%install
make vvfst-install DESTDIR=%{buildroot}%{_datadir}/voikko

%files
%license COPYING
%doc CONTRIBUTORS ChangeLog README.md
%dir %{_datadir}/voikko/
%{_datadir}/voikko/*

%changelog
