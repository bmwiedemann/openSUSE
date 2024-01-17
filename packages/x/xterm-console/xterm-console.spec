#
# spec file for package xterm-console
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xterm-console
Version:        1.1
Release:        0
Summary:        A Linux vt console look-alike xterm wrapper
License:        MIT
Group:          System/X11/Utilities
URL:            https://github.com/os-autoinst/xterm-console
Source:         xterm-console
Source1:        psf2bdf.pl
BuildRequires:  bdftopcf
BuildRequires:  fontpackages-devel
# the original consolefonts:
BuildRequires:  kbd
Requires:       fonts-config
# svirt, eg. s390x, xen
Supplements:    os-autoinst
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
This package contains the basic X.Org terminal program.

%prep

%setup -q -c -T
cp %{SOURCE1} .

%build
chmod +x ./psf2bdf.pl

for font in %{_datadir}/kbd/consolefonts/*.psfu.gz; do
    fontname="${font##*/}"
    fontname="${fontname%.psfu.gz}"
    gunzip -c $font | ./psf2bdf.pl | sed -e "s,FONT \+-psf-,FONT ${fontname}," > "$fontname".bdf
done

for i in *.bdf; do
    bdftopcf "$i" | gzip -9 >"${i%.bdf}.pcf.gz"
done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/fonts/misc/

install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}
install -m 0644 *.pcf.gz %{buildroot}%{_datadir}/fonts/misc/

%reconfigure_fonts_scriptlets

%files
%{_bindir}/xterm-console
%dir %{_datadir}/fonts/misc
%{_datadir}/fonts/misc/*.pcf.gz

%changelog
