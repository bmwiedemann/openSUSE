#
# spec file for package product-builder
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


Summary:        SUSE Product Builder
License:        GPL-2.0-only
Group:          System/Management
URL:            http://github.com/openSUSE/product-builder
Name:           product-builder
Conflicts:      kiwi
Conflicts:      kiwi-instsource
Version:        1.4.14
Release:        0
Provides:       kiwi-schema = 6.2
Source:         product-builder-%version.tar.xz

Requires:       libxslt
Requires:       perl >= %{perl_version}
Requires:       perl-Class-Singleton
Requires:       perl-Config-IniFiles >= 2.49
Requires:       perl-File-Slurp
Requires:       perl-JSON
Requires:       perl-Readonly
Requires:       perl-XML-LibXML
Requires:       perl-XML-LibXML-Common
Requires:       perl-XML-SAX
Requires:       perl-libwww-perl

Provides:       kiwi-packagemanager:instsource
Provides:       system-packages:kiwi-product
%if 0%{?suse_version}
Requires:       build
%else
Requires:       obs-build
%global debug_package %{nil}
%endif
Requires:       checkmedia
Requires:       inst-source-utils
Requires:       mkisofs
Requires:       product-builder-plugin
%ifarch %ix86 x86_64
Requires:       syslinux
%endif

%description
The SUSE product builder, builds product media (CD/DVD) for
the SUSE product portfolio. Based on kiwi perl implementation.

To be used only for product medias for Leap 15 and SLE 15.

%prep
%setup -q

%build
test -e /.buildenv && . /.buildenv
make CFLAGS="%{optflags}"

%install
make buildroot="%{buildroot}" \
    doc_prefix="%{buildroot}/%{_defaultdocdir}" \
    man_prefix="%{buildroot}/%{_mandir}" \
    install
./.version >"%{buildroot}/%{_datadir}/kiwi/.revision"

%if 0%{?is_opensuse}
mv %{buildroot}%{_bindir}/product-builder{.pl,}
%else
# install SLE wrapper as entry point. It doesn't really harm as the
# build flavor detected is very specific, but to avoid waste...
ln -s product-builder-sle.sh %{buildroot}%{_bindir}/product-builder
%endif

%files
%dir %{_datadir}/kiwi
%license LICENSE
%{_datadir}/kiwi/.revision
%{_datadir}/kiwi/metadata
%{_datadir}/kiwi/modules
%{_datadir}/kiwi/xsl
%{_bindir}/product-builder*

%changelog
