#
# spec file for package virt-what
#
# Copyright (c) 2025 SUSE LLC
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


Name:           virt-what
Version:        1.27
Release:        0
Summary:        Detect if running in a virtual machine
License:        GPL-2.0-or-later
Group:          System/Console
URL:            https://people.redhat.com/~rjones/virt-what
Source0:        https://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz
Source1:        https://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Requires:       util-linux
Requires:       which
%ifarch %{ix86} x86_64 aarch64 %{arm}
Requires:       dmidecode
%endif
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
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc README
%{_sbindir}/virt-what
%{_sbindir}/virt-what-cvm
%{_mandir}/man1/virt-what.1%{?ext_man}
%{_mandir}/man1/virt-what-cvm.1.gz
%{_libexecdir}/virt-what-cpuid-helper

%changelog
