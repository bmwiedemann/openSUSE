#
# spec file for package u3-tool
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Guido Berhoerster.
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


%define  _tag   1.0
%define  _rel   60

Name:           u3-tool
Version:        %{_tag}+svn%{_rel}
Release:        0
Summary:        Tool for Controlling the Special Features of an U3 USB Flash disk
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://u3-tool.sourceforge.net/
Source0:        u3-tool-code-%{_rel}-tags-u3-tool-%{_tag}.zip
Patch0:         u3-tool-0.3-fix-manpage-section.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(libusb)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    ppc ppc64

%description
u3-tool is a tool for unlocking and configuring U3 smart USB Flash devices.  It
supports changing the virtual CD partition size, replacing the CD image,
enabling, disabling, and resetting device security, and unlocking the secured
data partition.

%prep
%setup -q -n u3-tool-code-%{_rel}-tags-u3-tool-%{_tag}
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%doc %{_mandir}/man8/u3-tool.8*
%{_sbindir}/u3-tool

%changelog
