#
# spec file for package checkmedia
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


Name:           checkmedia
Summary:        Check installation or Live media
License:        GPL-3.0-or-later
Group:          System/Management
Version:        6.2
Release:        0
URL:            https://github.com/openSUSE/checkmedia
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gpg
BuildRequires:  xz
BuildRequires:  rubygem(asciidoctor)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The program checks installation or Live media for errors.

%define libversion %(echo %version | cut -d. -f1)

%package -n     libmediacheck%{libversion}
Summary:        Library for checking installation or Live media
Group:          System/Libraries
Requires:       gpg

%description -n libmediacheck%{libversion}
Library for checking installation or Live media. Used by checkmedia and linuxrc.

%package -n     libmediacheck-devel
Summary:        Library for checking installation or Live media
Group:          Development/Libraries/C and C++
Requires:       libmediacheck%{libversion} = %version

%description -n libmediacheck-devel
Library for checking installation or Live media. Used by checkmedia and linuxrc.

%prep
%setup

%build
make %{?_smp_mflags}

%check
make test

%install
install -d -m 755 %{buildroot}/usr/bin
%make_install
make doc
install -D -m 644 checkmedia.1 %{buildroot}%{_mandir}/man1/checkmedia.1
install -D -m 644 tagmedia.1 %{buildroot}%{_mandir}/man1/tagmedia.1

%post -n libmediacheck%{libversion} -p /sbin/ldconfig

%postun -n libmediacheck%{libversion} -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/bin/checkmedia
/usr/bin/tagmedia
%doc %{_mandir}/man1/checkmedia.*
%doc %{_mandir}/man1/tagmedia.*

%files -n libmediacheck%{libversion}
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc README.*
%doc mediacheck.md
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif

%files -n libmediacheck-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/mediacheck.h

%changelog
