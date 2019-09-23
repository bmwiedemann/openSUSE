#
# spec file for package wordnet
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define dbver 3.1
%define sover 3
%define lib_name libWN%{sover}

Name:           wordnet
Version:        3.0
Release:        0
Summary:        A lexical database for the English language
License:        MIT
Group:          Productivity/Office/Dictionary
Url:            http://wordnet.princeton.edu
Source0:        http://wordnetcode.princeton.edu/3.0/WordNet-%{version}.tar.bz2
# Updated dict files as drop-in replacement
Source1:        http://wordnetcode.princeton.edu/wn%{dbver}.dict.tar.gz
# PATCH-FIX-UPSTREAM wordnet-system-tk-headers.patch badshah400@gmail.com -- Use system tk headers, patch came from Fedora
Patch0:         wordnet-system-tk-headers.patch
# PATCH-FIX-UPSTREAM wordnet-libtool.patch badshah400@gmail.com -- Correct checking for libtool, patch came from Fedora
Patch1:         wordnet-libtool.patch
# PATCH-FIX-UPSTREAM wordnet-3.0-CVE-2008-2149.patch badshah400@gmail.com -- Fix buffer overflows, patch came from upstream
Patch2:         wordnet-3.0-CVE-2008-2149.patch
# PATCH-FIX-UPSTREAM wordnet-3.0-CVE-2008-3908.patch badshah400@gmail.com -- String and character corrections in various source files, patch came from upstream
Patch3:         wordnet-3.0-CVE-2008-3908.patch
# PATCH-FIX-UPSTREAM wordnet-3.0-fix_man.patch badshah400@gmail.com -- Miscellaneous correction to the man files, patch came from Fedora
Patch4:         wordnet-3.0-fix_man.patch
BuildRequires:  automake >= 1.8
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-libXext-devel
Requires:       tcl
Requires:       tk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
WordNet is a large lexical database of English.
Nouns, verbs, adjectives and adverbs are grouped into sets
of cognitive synonyms (synsets), each expressing a distinct concept. Synsets
are interlinked by means of conceptual-semantic and lexical relations. The
resulting network of meaningfully related words and concepts can be navigated
with the browser.
WordNet's structure makes it a useful tool for computational linguistics and
natural language processing.

%package -n %{lib_name}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{lib_name}
WordNet is a large lexical database of English.
Nouns, verbs, adjectives and adverbs are grouped into sets
of cognitive synonyms (synsets), each expressing a distinct concept. Synsets
are interlinked by means of conceptual-semantic and lexical relations. The
resulting network of meaningfully related words and concepts can be navigated
with the browser.
WordNet's structure makes it a useful tool for computational linguistics and
natural language processing.

This package contains shared library for %{name}.

%package devel
Summary:        The development libraries and header files for WordNet
Group:          Development/Libraries/Other
Requires:       %{lib_name} = %{version}
Requires:       tcl-devel
Requires:       tk-devel

%description devel
WordNet is a large lexical database of English.
Nouns, verbs, adjectives and adverbs are grouped into sets
of cognitive synonyms (synsets), each expressing a distinct concept. Synsets
are interlinked by means of conceptual-semantic and lexical relations. The
resulting network of meaningfully related words and concepts can be navigated
with the browser.
WordNet's structure makes it a useful tool for computational linguistics and
natural language processing.

This package contains the libraries and header files required to create
applications based on WordNet.

%prep
%setup -q -n WordNet-3.0 -b 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# delete the include/tk dir, since we do not use the included tk headers
rm -rf include/tk

%build
libtoolize && aclocal
autoupdate
autoreconf -i

CFLAGS="%{optflags} -DUSE_INTERP_RESULT"
%configure --enable-static=no --prefix=%{_datadir}/wordnet-%{version}/

make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}

# delete the libWN.la files (reasoning in the packaging guidelines)
rm -f  %{buildroot}%{_libdir}/libWN.la
# Remove duplicate copies of docs installed by make install
rm -rf %{buildroot}%{_datadir}/%{name}-%{version}/doc
# Remove useless Makefiles installed by %%doc
rm -rf doc/{html,ps,pdf}/Makefile*

# REPLACE OLD DIC DATABASE WITH NEW
rm -fr %{buildroot}%{_datadir}/%{name}-%{version}/dict
cp -pr ../dict %{buildroot}%{_datadir}/%{name}-%{version}/dict

%fdupes %{buildroot}%{_datadir}/%{name}-%{version}/dict/

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README doc/{html,ps,pdf}
%{_bindir}/wishwn
%{_bindir}/wn
%{_bindir}/wnb
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man5/*.5%{ext_man}
%{_mandir}/man7/*.7%{ext_man}
%{_datadir}/%{name}-%{version}/

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libWN.so.%{sover}*

%files devel
%defattr(-,root,root,-)
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/wn.h
%{_libdir}/libWN.so

%changelog
