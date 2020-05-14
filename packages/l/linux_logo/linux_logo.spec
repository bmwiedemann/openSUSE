#
# spec file for package linux_logo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           linux_logo
Version:        6.0
Release:        0
Summary:        Prints the linux logo on the text console
License:        GPL-2.0-only
URL:            http://deater.net/weave/vmwprod/linux_logo/
Source:         http://deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz

%description
The Linux logo on the text console, with colors and system information.
Contains a number of built-in logos.

%prep
%setup -q

%build
%configure
%make_build logos-all

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install \
	INSTALL_BINPATH=%{buildroot}%{_bindir} \
	INSTALL_MANPATH=%{buildroot}%{_mandir} \
	INSTALLDIR=%{buildroot}%{_datadir}/locale \
	PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README* TODO USAGE CHANGES* BUGS *.FAQ
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
