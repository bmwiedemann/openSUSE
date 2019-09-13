#
# spec file for package writerperfect
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


Name:           writerperfect
Version:        0.9.6
Release:        0
Summary:        Tools for converting WordPerfect documents
License:        LGPL-2.1+ OR MPL-2.0+
Group:          Productivity/Text/Convertors
Url:            http://libwpd.sf.net/
Source:         http://downloads.sourceforge.net/project/libwpd/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-fix-build-with-libgsf.patch
Patch1:         0001-Fix-linking-with-newer-tools-by-getting-the-library-.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libeot)
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libgsf-1) >= 1.6.0
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librvngabw-0.0)
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libzmf-0.0)
# Make upgrade smooth with no conflicting files
Provides:       abw2abw = %{version}-%{release}
Obsoletes:      abw2abw < %{version}-%{release}
Provides:       abw2epub = %{version}-%{release}
Obsoletes:      abw2epub < %{version}-%{release}
Provides:       abw2odt = %{version}-%{release}
Obsoletes:      abw2odt < %{version}-%{release}
Provides:       cdr2epub = %{version}-%{release}
Obsoletes:      cdr2epub < %{version}-%{release}
Provides:       cdr2odg = %{version}-%{release}
Obsoletes:      cdr2odg < %{version}-%{release}
Provides:       cmx2epub = %{version}-%{release}
Obsoletes:      cmx2epub < %{version}-%{release}
Provides:       cmx2odg = %{version}-%{release}
Obsoletes:      cmx2odg < %{version}-%{release}
Provides:       ebook2abw = %{version}-%{release}
Obsoletes:      ebook2abw < %{version}-%{release}
Provides:       ebook2epub = %{version}-%{release}
Obsoletes:      ebook2epub < %{version}-%{release}
Provides:       ebook2odt = %{version}-%{release}
Obsoletes:      ebook2odt < %{version}-%{release}
Provides:       fh2epub = %{version}-%{release}
Obsoletes:      fh2epub < %{version}-%{release}
Provides:       fh2odg = %{version}-%{release}
Obsoletes:      fh2odg < %{version}-%{release}
Provides:       key2epub = %{version}-%{release}
Obsoletes:      key2epub < %{version}-%{release}
Provides:       key2odp = %{version}-%{release}
Obsoletes:      key2odp < %{version}-%{release}
Provides:       mwaw2abw = %{version}-%{release}
Obsoletes:      mwaw2abw < %{version}-%{release}
Provides:       mwaw2epub = %{version}-%{release}
Obsoletes:      mwaw2epub < %{version}-%{release}
Provides:       mwaw2odf = %{version}-%{release}
Obsoletes:      mwaw2odf < %{version}-%{release}
Provides:       numbers2ods = %{version}-%{release}
Obsoletes:      numbers2ods < %{version}-%{release}
Provides:       pages2abw = %{version}-%{release}
Obsoletes:      pages2abw < %{version}-%{release}
Provides:       pages2epub = %{version}-%{release}
Obsoletes:      pages2epub < %{version}-%{release}
Provides:       pages2odt = %{version}-%{release}
Obsoletes:      pages2odt < %{version}-%{release}
Provides:       pmd2epub = %{version}-%{release}
Obsoletes:      pmd2epub < %{version}-%{release}
Provides:       pmd2odg = %{version}-%{release}
Obsoletes:      pmd2odg < %{version}-%{release}
Provides:       pub2epub = %{version}-%{release}
Obsoletes:      pub2epub < %{version}-%{release}
Provides:       pub2odg = %{version}-%{release}
Obsoletes:      pub2odg < %{version}-%{release}
Provides:       qxp2epub = %{version}-%{release}
Obsoletes:      qxp2epub < %{version}-%{release}
Provides:       qxp2odg = %{version}-%{release}
Obsoletes:      qxp2odg < %{version}-%{release}
Provides:       sd2abw = %{version}-%{release}
Obsoletes:      sd2abw < %{version}-%{release}
Provides:       sd2epub = %{version}-%{release}
Obsoletes:      sd2epub < %{version}-%{release}
Provides:       sd2odf = %{version}-%{release}
Obsoletes:      sd2odf < %{version}-%{release}
Provides:       vsd2epub = %{version}-%{release}
Obsoletes:      vsd2epub < %{version}-%{release}
Provides:       vsd2odg = %{version}-%{release}
Obsoletes:      vsd2odg < %{version}-%{release}
Provides:       vss2epub = %{version}-%{release}
Obsoletes:      vss2epub < %{version}-%{release}
Provides:       vss2odg = %{version}-%{release}
Obsoletes:      vss2odg < %{version}-%{release}
Provides:       wks2ods = %{version}-%{release}
Obsoletes:      wks2ods < %{version}-%{release}
Provides:       wpd2abw = %{version}-%{release}
Obsoletes:      wpd2abw < %{version}-%{release}
Provides:       wpd2epub = %{version}-%{release}
Obsoletes:      wpd2epub < %{version}-%{release}
Provides:       wpd2odt = %{version}-%{release}
Obsoletes:      wpd2odt < %{version}-%{release}
Provides:       wpft2abw = %{version}-%{release}
Obsoletes:      wpft2abw < %{version}-%{release}
Provides:       wpft2epub = %{version}-%{release}
Obsoletes:      wpft2epub < %{version}-%{release}
Provides:       wpft2odf = %{version}-%{release}
Obsoletes:      wpft2odf < %{version}-%{release}
Provides:       wpg2epub = %{version}-%{release}
Obsoletes:      wpg2epub < %{version}-%{release}
Provides:       wpg2odg = %{version}-%{release}
Obsoletes:      wpg2odg < %{version}-%{release}
Provides:       wps2abw = %{version}-%{release}
Obsoletes:      wps2abw < %{version}-%{release}
Provides:       wps2epub = %{version}-%{release}
Obsoletes:      wps2epub < %{version}-%{release}
Provides:       wps2odt = %{version}-%{release}
Obsoletes:      wps2odt < %{version}-%{release}
Provides:       zmf2epub = %{version}-%{release}
Obsoletes:      zmf2epub < %{version}-%{release}
Provides:       zmf2odg = %{version}-%{release}
Obsoletes:      zmf2odg < %{version}-%{release}

%description
Tools for converting WordPerfect and other documents to various other
formats supported by the helper libraries that are also ie. used in
libreoffice.

%prep
%autosetup -p1

%build
libtoolize --force --copy --install
autoreconf -fi
%configure \
    --disable-werror \
    --disable-silent-rules \
    --with-import-libs \
    --with-export-libs \
    --with-libeot \
    --with-libgsf
make %{?_smp_mflags}

%install
%make_install

%files
%doc NEWS README
%license COPYING.MPL COPYING.LGPL
# Name binaries to be sure we do not lose features due to wrong
# configure checks
%{_bindir}/abw2abw
%{_bindir}/abw2epub
%{_bindir}/abw2odt
%{_bindir}/cdr2epub
%{_bindir}/cdr2odg
%{_bindir}/cmx2epub
%{_bindir}/cmx2odg
%{_bindir}/ebook2abw
%{_bindir}/ebook2epub
%{_bindir}/ebook2odt
%{_bindir}/fh2epub
%{_bindir}/fh2odg
%{_bindir}/key2epub
%{_bindir}/key2odp
%{_bindir}/mwaw2abw
%{_bindir}/mwaw2epub
%{_bindir}/mwaw2odf
%{_bindir}/numbers2ods
%{_bindir}/pages2abw
%{_bindir}/pages2epub
%{_bindir}/pages2odt
%{_bindir}/pmd2epub
%{_bindir}/pmd2odg
%{_bindir}/pub2epub
%{_bindir}/pub2odg
%{_bindir}/qxp2epub
%{_bindir}/qxp2odg
%{_bindir}/sd2abw
%{_bindir}/sd2epub
%{_bindir}/sd2odf
%{_bindir}/vsd2epub
%{_bindir}/vsd2odg
%{_bindir}/vss2epub
%{_bindir}/vss2odg
%{_bindir}/wks2ods
%{_bindir}/wpd2abw
%{_bindir}/wpd2epub
%{_bindir}/wpd2odt
%{_bindir}/wpft2abw
%{_bindir}/wpft2epub
%{_bindir}/wpft2odf
%{_bindir}/wpg2epub
%{_bindir}/wpg2odg
%{_bindir}/wps2abw
%{_bindir}/wps2epub
%{_bindir}/wps2odt
%{_bindir}/zmf2epub
%{_bindir}/zmf2odg

%changelog
