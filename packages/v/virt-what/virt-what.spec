#
# spec file for package virt-what
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           virt-what
Version:        1.15
Release:        0
Summary:        Detect if running in a virtual machine
License:        GPL-2.0+
Group:          System/Console
Url:            http://people.redhat.com/~rjones/virt-what
Source0:        http://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz
Source1:        http://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
%ifarch %{ix86} x86_64 aarch64 %arm
Requires:       dmidecode
%endif
Requires:       util-linux
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# for pod2man
%if 0%{?suse_version}
BuildRequires:  perl
%else
BuildRequires:  perl-podlators
%endif

%description
This is a collection of scripts which you can use to work out what
sort of virtualization you are running inside.  Please read the manual
page virt-what(1) to find out how to use it.  This file is for
developers and people compiling from source.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%doc README COPYING
%{_sbindir}/virt-what
%{_mandir}/man1/virt-what.1%{ext_man}
%{_libexecdir}/virt-what-cpuid-helper

%changelog
