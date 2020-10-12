#
# spec file for package mairix
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mairix
Version:        0.24
Release:        0
Summary:        A maildir indexer and searcher
License:        GPL-2.0
Group:          Productivity/Networking/Email/Utilities
Url:            http://www.rc0.org.uk/mairix/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex

%description
mairix is a tool for indexing email messages stored in maildir format
folders and performing fast searches on the resulting index.  The
output is a new maildir folder containing symbolic links to the matched
messages.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
make %{?_smp_mflags}
strip mairix
# make docs

%install
%make_install
# make DESTDIR=$RPM_BUILD_ROOT install_docs

%files
%doc ACKNOWLEDGEMENTS README COPYING dotmairixrc.eg
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man5/%{name}rc.5%{ext_man}

%changelog
