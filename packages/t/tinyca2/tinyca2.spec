#
# spec file for package tinyca2
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


%define	libdir		%{_datadir}/TinyCA2/lib
%define	templatesdir	%{_datadir}/TinyCA2/templates
%define	localedir	%{_datadir}/locale/
Name:           tinyca2
Version:        0.7.5
Release:        0
Summary:        A Graphical Tool for Managing a Certification Authority
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://tinyca.sm-zone.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         0001-fix-combobox-strings-for-extended-key-usage.diff
Patch1:         0002-add-support-for-Microsoft-extendedKeyUsage-attributes.diff
Patch2:         0001-fix-paranthesis-use.diff
Patch3:         0002-fix-deprecation-warning.diff
Patch4:         0003-fix-compatibility-with-openssl-1.0.1.diff
Patch5:         0004-fix-perl-deprecation-defined.diff
BuildRequires:  update-desktop-files
Requires:       perl
Requires:       perl-Gtk2
Requires:       perl-MIME-Base64
Provides:       tinyca:%{_bindir}/tinyca
BuildArch:      noarch

%description
TinyCA is a graphical tool to manage a small Certification Authority
(CA) using openssl.

TinyCA supports - creation and revocation of x509 - S/MIME
   certificates.

- PKCS#10 requests.

- exporting certificates as PEM, DER, TXT, and PKCS#12.

- server certificates for use in web servers, email servers, IPsec,
   and more.

- client certificates for use in web browsers, email clients, IPsec,
and more.

%prep
%autosetup -p1

%build
# Configure pristine source
sed -i -e 's:./lib:%{libdir}:g;s:./templates:%{templatesdir}:g' tinyca2
sed -i -e '/bindtextdomain/d' tinyca2
make %{?_smp_mflags} -C po

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{libdir}
install -d -m 755 %{buildroot}%{libdir}/GUI
install -d -m 755 %{buildroot}%{templatesdir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 lib/*.pm %{buildroot}%{libdir}
install -m 644 lib/GUI/*.pm %{buildroot}%{libdir}/GUI
install -m 644 templates/openssl.cnf %{buildroot}%{templatesdir}
install -m 755 tinyca2 %{buildroot}%{_bindir}
pushd locale
for i in *; do
	install -d -m 755 %{buildroot}%{localedir}/$i/LC_MESSAGES
	install -m 644 $i/LC_MESSAGES/tinyca2.mo %{buildroot}%{localedir}/$i/LC_MESSAGES/
done
popd
cat > %{buildroot}%{_datadir}/applications/tinyca2.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
GenericName=Tool to manage a Certification Authority
Name=TinyCA2
Exec=tinyca2
EOF
%suse_update_desktop_file tinyca2 Security Utility
%find_lang %{name}

%files -f %{name}.lang
%doc CHANGES
%dir %{_datadir}/TinyCA2
%dir %{_datadir}/TinyCA2/lib
%dir %{_datadir}/TinyCA2/templates
%{_datadir}/TinyCA2/lib/*
%{_datadir}/TinyCA2/templates/*
%{_bindir}/tinyca2
%{_datadir}/applications/*

%changelog
