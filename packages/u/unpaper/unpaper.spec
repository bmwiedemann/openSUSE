#
# spec file for package unpaper
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           unpaper
Summary:        Post-Processing Tool for Scanned Text Pages
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Version:        6.1
Release:        0
Url:            https://www.flameeyes.eu/projects/unpaper
Source:         https://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libxslt-tools
BuildRequires:  pkg-config

%description
The unpaper command line tool helps with post-processing scanned text
pages, especially with	book pages scanned from photocopies. unpaper
tries to remove dark edges, corrects the rotation ("deskewing"), and
aligns the centering of pages.

%prep
%setup -q

%build
%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root)
%{_docdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/%{name}.1.gz

%changelog
