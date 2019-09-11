#
# spec file for package nip2
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


Name:           nip2
Version:        8.6.0
Release:        0
Summary:        Interactive tool for working with large images
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Url:            http://www.vips.ecs.soton.ac.uk/
Source0:        https://github.com/jcupitt/nip2/releases/download/v8.6.0/nip2-8.6.0.tar.gz
# Fix broken PNG file: https://github.com/jcupitt/nip2/commit/7bc6212cb51d266f1a6fc3e05260390af4d80c99
Source2:        simp_base.png
# PATCH-FIX-OPENSUSE nip2-doc-path.patch
Patch1:         nip2-doc-path.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flex
BuildRequires:  graphviz-devel
BuildRequires:  gsl-devel
BuildRequires:  gtk2-devel
BuildRequires:  libgsf-devel
BuildRequires:  libvips-devel
BuildRequires:  libxml2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
nip2 is a user interface for the VIPS image processing library.
VIPS library is good with large images (images larger than the amount
of RAM you have available), with many CPUs, for working with colour,
for scientific analysis and for general research & development.

%prep
%setup -q
%patch1 -p1
# Fix broken PNG file
cp %{SOURCE2} share/nip2/data/examples/manual_balance/simp_base.png

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -D share/nip2/data/vips-128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -rf %{buildroot}%{_datadir}/doc/nip2
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%check
make check

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/html doc/pdf AUTHORS ChangeLog COPYING NEWS THANKS
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/nip2.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/nip2.xml
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
