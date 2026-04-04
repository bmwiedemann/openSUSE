#
# spec file for package chemical-mime-data
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           chemical-mime-data
Version:        0.1.94
Release:        0
Summary:        A collection of data files for various chemical MIME types
License:        LGPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/dleidert/chemical-mime
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  xsltproc
Requires:       shared-mime-info
BuildArch:      noarch

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops, such as KDE and GNOME.

Chemical MIMEs have been proposed in 1995, though it seems they have never
been registered with IANA. However, they are widely used and the project's aim is,
to support these important, but unofficial MIME types.

%prep
%autosetup -p1

%build
export CONVERT=/usr/bin/true
%configure --disable-static \
           --disable-update-database \
           --without-gnome-mime \
           --without-kde-mime \
           --without-pixmaps \
           --without-hicolor-theme \
           --enable-convert=true \
           --docdir=%{_defaultdocdir}/%{name}

%make_build

%install
%make_install
%find_lang %{name}
%fdupes %{buildroot}/%{_prefix}

%files -f %{name}.lang
%doc %{_defaultdocdir}/%{name}
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/pkgconfig/chemical-mime-data.pc

%changelog
