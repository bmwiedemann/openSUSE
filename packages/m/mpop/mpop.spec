#
# spec file for package mpop.
#
# Copyright (c) 2021 Fabrice Bauzac.
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
%bcond_with gnome-keyring

Name:           mpop
Version:        1.4.14
Release:        1

License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libidn-devel
BuildRequires:  pkgconfig
BuildRequires:  libgnutls-devel
BuildRequires:  libsecret-devel
BuildRequires:  libgsasl-devel
%if %{with gnome-keyring}
BuildRequires:  pkgconfig(gnome-keyring-1)
%endif
Url:            https://marlam.de/mpop/
Source:         https://marlam.de/mpop/releases/mpop-1.4.14.tar.xz

Summary:        Lightweight and featureful POP3 Client

%global _description %{expand:
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a
very fast POP3 implementation, many authentication methods, good
TLS/SSL support, IPv6 support, and more.
}

%description %_description

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc %_description

This package contains documentation and sample configuration files.

%prep
%setup -q

%build
%if 0%{?suse_version} > 1000
export CFLAGS="%{optflags} -fstack-protector"
%endif
%configure --with-tls=gnutls --with-libgsasl --docdir="%{_docdir}/%{name}"
%make_build

%install
%makeinstall V=1
%find_lang %{name}

for f in \
COPYING \
; do
    ff="${f##*/}"
    %__install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
done

echo -n >docfiles.lst
for f in \
AUTHORS ChangeLog* NEWS README* THANKS NOTES \
doc/*.example \
; do
    ff="${f##*/}"
    %__install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
    echo "%doc %{_docdir}/%{name}/$ff" >>docfiles.lst
done

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/COPYING
%{_bindir}/mpop
%{_infodir}/mpop.info%{ext_info}
%{_mandir}/man1/mpop.1%{ext_man}

%files doc -f docfiles.lst
%defattr(-,root,root,-)

%changelog
